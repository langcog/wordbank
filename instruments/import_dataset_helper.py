import xlrd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import defaultdict


class ImportHelper:

    def __init__(self, data_file, instrument_model, splitcol=False):

        self.data_file = data_file
        self.instrument_model = instrument_model
        self.splitcol = splitcol

        self.col_map = {}
        self.field_value_mapping = defaultdict(lambda: dict())
        self.children = {}
        self.administrations = {}
        self.datemode = None

        self.missing_values = {'Null', '#NULL!', '', ' ', 'Missing', 'Unknown/other'}

    @staticmethod
    def format_date(date_str, datemode=None):
        return datetime(*xlrd.xldate_as_tuple(date_str, datemode))

    @staticmethod
    def compute_age(date_of_birth, date_of_test):
        age = relativedelta(date_of_test, date_of_birth)
        avg_month = 365.2425/12.0
        return int(age.years*12 + age.months + float(age.days) / avg_month)

    @staticmethod
    def value_typing(value):
        if type(value) == float:
            value = int(value)
        if type(value) == str:
            value = unicode(value, "utf-8")
        elif type(value) == unicode:
            value = value
        else:
            value = unicode(value)
        return value

    def get_field_value(self, column, field_type, group, row_values):
        value = row_values[self.col_map[column]]
        if not value in self.missing_values:
            if field_type in ('study_id', 'study_momed'):
                return value
            elif field_type in ('birth_order', 'data_age'):
                return int(value)
            elif field_type in ('date_of_birth, date_of_test'):
                return self.format_date(value, self.datemode)
            elif field_type in ('ethnicity', 'sex', 'mom_ed') or group == 'item':
                value = self.value_typing(value).lower()
                if self.splitcol and field_type == 'word':
                    value += column[-1]
                return self.field_value_mapping[field_type][value]

    def get_data_fields(self, cols, group, row_values):
        group_cols = cols[group]
        results = defaultdict(lambda: None)
        for column in group_cols.keys():
            field = group_cols[column]['field']
            field_type = group_cols[column]['field_type']
            if field_type == 'mom_ed':
                momed_value = self.get_field_value(column, 'mom_ed', group, row_values)
                results['momed'] = momed_value
                study_momed_value = self.get_field_value(column, 'study_momed', group, row_values)
                results['study_momed'] = study_momed_value
            else:
                field_value = self.get_field_value(column, field_type, group, row_values)
                if self.splitcol and (results[field] == 'produces' or field_value == 'produces'):
                    results[field] = 'produces'
                else:
                    results[field] = field_value
        return results

    def import_data(self):

        book = xlrd.open_workbook(self.data_file)
        self.datemode = book.datemode

        # make a mapping between model value sets and datasheet value sets
        value_mapping_sheet = book.sheet_by_name('value_mapping')
        for row in xrange(1, value_mapping_sheet.nrows):
            row_values = list(value_mapping_sheet.row_values(row))
            field_type, value, data_value = row_values[:3]
            value = self.value_typing(value)
            data_value = self.value_typing(data_value).lower()
            if data_value is not None and data_value != '':
                self.field_value_mapping[field_type][data_value] = value

        # make a mapping between datasheet column names and model field names/types
        field_mapping_sheet = book.sheet_by_name('field_mapping')
        cols = defaultdict(lambda: dict())
        for row in xrange(1, field_mapping_sheet.nrows):
            row_values = list(field_mapping_sheet.row_values(row))
            field, column, group, field_type = row_values[:4]
            if column is not None and column != '':
                columns = [column]
                if group == 'item':
#                    field = 'item_' + string.replace(field, '.', '_')
                    if self.splitcol and field_type == 'word':
                        columns = [column + 'u', column + 'p']
                for column in columns:
                    cols[group][column.lower()] = {'field': field, 'field_type': field_type}

        data_sheet = book.sheet_by_name('data')
        col_names = list(data_sheet.row_values(0))

        # make a mapping between dataset column names and dataset column indexes
        for index, value in enumerate(col_names):
            self.col_map[value.lower()] = index

        # go through the datasheet entries and populate all the data
        for row in xrange(1, data_sheet.nrows):
            row_values = list(data_sheet.row_values(row))

            # get child data
            child = self.get_data_fields(cols, 'child', row_values)
            self.children[row] = child

            # get administration data
            administration = self.get_data_fields(cols, 'admin', row_values)
            if child['date_of_birth'] is not None and administration['date_of_test'] is not None:
                computed_age = self.compute_age(child['date_of_birth'], administration['date_of_test'])
                administration['age'] = computed_age
            else:
                administration['age'] = administration['data_age']

            # get item data
            item_data = self.get_data_fields(cols, 'item', row_values)
            administration['item_data'] = item_data

            self.administrations[row] = administration