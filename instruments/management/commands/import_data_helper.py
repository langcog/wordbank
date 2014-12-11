import xlrd
import string
from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import defaultdict


class ImportHelper:

    def __init__(self, path_to_data_file, data_file, instrument_model, splitcol=False):

        self.path = path_to_data_file
        self.data_file = data_file
        self.instrument_model = instrument_model
        self.splitcol = splitcol

        self.col_map = {}
        self.field_value_mapping = defaultdict(lambda: dict())
        self.children = {}
        self.administrations = {}
        self.source_name = None
        self.source_dataset = None
        self.datemode = None

    @staticmethod
    def format_date(date_str, datemode=None):
        return datetime(*xlrd.xldate_as_tuple(date_str, datemode))

    @staticmethod
    def compute_age(date_of_birth, date_of_test):
        age = relativedelta(date_of_test, date_of_birth)
        avg_month = 365.2425/12.0
        return int(age.years*12 + age.months + float(age.days) / avg_month)

    def get_field_value(self, column, field_type, group, row_values):
        value = row_values[self.col_map[column]]
        if value != 'Null' and value != '' and value != '#NULL!':
            if field_type in ('study_id',):
                return value
            elif field_type in ('birth_order', 'data_age', 'mom_ed'):
                return int(value)
            elif field_type in ('date_of_birth, date_of_test'):
                return self.format_date(value, self.datemode)
            elif field_type in ('ethnicity', 'sex') or group == 'item':
                if isinstance(value, str):
                    value = value.lower()
                if value in self.field_value_mapping[field_type]:
                    return self.field_value_mapping[field_type][value]

    def get_data_fields(self, cols, group, row_values):
        group_cols = cols[group]
        results = defaultdict(lambda: None)
        for column in group_cols.keys():
            field = group_cols[column]['field']
            field_type = group_cols[column]['field_type']
            field_value = self.get_field_value(column, field_type, group, row_values)
            if self.splitcol and (results[field] == 'produces' or field_value == 'produces'):
                results[field] = 'produces'
            else:
                results[field] = field_value
        return results

    def import_data(self):

        # parse the datasheet's name into the source name and dataset
        dataset = self.data_file.split('_')
        if len(dataset) == 3:
            self.source_name, self.source_dataset = dataset[1:]
        elif len(dataset) == 2:
            self.source_name, self.source_dataset = dataset[1:], ''
        else:
            raise RuntimeError("Invalid dataset filename.")

        book = xlrd.open_workbook(self.path)
        self.datemode = book.datemode

        # make a mapping between model value sets and datasheet value sets
        value_mapping_sheet = book.sheet_by_name('value_mapping')
        for row in xrange(1, value_mapping_sheet.nrows):
            row_values = list(value_mapping_sheet.row_values(row))
            field_type, value, data_value = row_values[:3]
            if isinstance(value, str):
                data_value = data_value.lower()
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
                    field = 'item_' + string.replace(field, '.', '_')
                    if self.splitcol and field_type == 'word':
                        columns = [column + 'u', column + 'p']
                for column in columns:
                    cols[group][column.lower()] = {'field': field, 'field_type': field_type}

        data_sheet = book.sheet_by_name('data')
        col_names = list(data_sheet.row_values(0))

        # make a mapping between dataset column names and dataset column indexes
        for index, value in enumerate(col_names):
            self.col_map[value.lower()] = index
#            if value.lower() in cols['admin'].keys():
#                self.col_map[cols['admin'][value.lower()]['field']] = index
#            elif value.lower() in cols['child'].keys():
#                self.col_map[cols['child'][value.lower()]['field']] = index
#            elif value.lower() in cols['item'].keys():
#                self.col_map[cols['item'][value.lower()]['field']] = index
#        print self.col_map

        # go through the datasheet entries and populate all the data
        for row in xrange(1, data_sheet.nrows):
            row_values = list(data_sheet.row_values(row))

            # get child data
            child = self.get_data_fields(cols, 'child', row_values)
            self.children[row] = child

            # get administration data
            administration = self.get_data_fields(cols, 'admin', row_values)
            administration['source_name'] = self.source_name
            administration['source_dataset'] = self.source_dataset
            if child['date_of_birth'] is not None and administration['date_of_test'] is not None:
                computed_age = self.compute_age(child['date_of_birth'], administration['date_of_test'])
                administration['age'] = computed_age
            else:
                administration['age'] = administration['data_age']

            # get item data
            item_data = self.get_data_fields(cols, 'item', row_values)
            administration['item_data'] = item_data

            self.administrations[row] = administration