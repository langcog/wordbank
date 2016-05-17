import xlrd
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import defaultdict


class ImportHelper:

    def __init__(self, data_file, date_format, norming, splitcol=False):

        self.data_file = data_file
        self.ftype = self.data_file.split('.')[-1]
        self.splitcol = splitcol
        self.norming = norming
        self.date_format = date_format

        self.children = {}
        self.administrations = {}

        self.datemode = None
        self.missing_values = {u'Null', u'#NULL!', u'', u' ', u'Missing', u'Unknown/other', u'?', u'NA', u'99'}

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

    def format_date(self, date_str):
        if self.ftype == "csv":
            return datetime.strptime(date_str, self.date_format)
        elif self.ftype == 'xlsx' or self.ftype == 'xls':
            return datetime(*xlrd.xldate_as_tuple(date_str, self.datemode))

    def get_field_value(self, column, field_type, group, row_values):
        value = row_values[self.col_map[column]]
        if type(value) == str or type(value) == unicode:
            value = value.strip()
        if not value in self.missing_values:
            if field_type in ('study_id', 'study_momed', 'study_family_id'):
                return value
            elif field_type in ('birth_order', 'data_age'):
                return int(float(value))
            elif field_type in ('norming'):
                return value == 'TRUE'
            elif field_type in ('date_of_birth, date_of_test'):
                return self.format_date(value)
            elif field_type in ('ethnicity', 'sex', 'mom_ed', 'zygosity') or group == 'item':
                value = self.value_typing(value).lower()
                if self.splitcol and field_type == 'word':
                    value += column[-1]
                try:
                    return self.value_mapping[field_type][value]
                except:
                    raise KeyError("Value mapping doesn't have entry for field type %s and value %s" % (field_type, value))

    def resolve_values(self, value0, value1):
        if value0 == 'produces' or value1 == 'produces':
            return 'produces'
        if value0 == 'understands' or value1 == 'understands':
            return 'understands'
        return ''

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
                if self.splitcol and field in results:
                    results[field] = self.resolve_values(results[field], field_value)
                else:
                    results[field] = field_value
        return results

    # make a mapping between model value sets and datasheet value sets
    def map_values(self):
        value_mapping = defaultdict(dict)
        for row in xrange(1, self.value_mapping_nrows):
            row_values = self.get_value_mapping_row(row)
            if len(row_values) > 1:
                field_type, value, data_value = row_values[:3]
                value = self.value_typing(value)
                data_value = self.value_typing(data_value).lower()
                if data_value is not None and data_value != '':
                    value_mapping[field_type][data_value] = value
        return value_mapping

    # make a mapping between datasheet column names and model field names/types
    def map_fields(self):
        field_mapping = defaultdict(dict)
        for row in xrange(1, self.field_mapping_nrows):
            row_values = self.get_field_mapping_row(row)
            if len(row_values) > 1:
                field, column, group, field_type = row_values[:4]
                if column is not None and column != '':
                    columns = [column]
                    if group == 'item':
                        if self.splitcol and field_type == 'word':
                            columns = [column + 'u', column + 'p']
                    for column in columns:
                        field_mapping[group][column.lower()] = {'field': field, 'field_type': field_type}
        return field_mapping

    # make a mapping between dataset column names and dataset column indexes
    def map_cols(self):
        col_map = {}
        for index, value in enumerate(self.col_names):
            col_map[value.lower()] = index
        return col_map

    def get_meta_data(self):

        if self.ftype == 'xlsx' or self.ftype == 'xls':

            book = xlrd.open_workbook(self.data_file)
            self.datemode = book.datemode

            value_mapping_sheet = book.sheet_by_name('values')
            self.value_mapping_nrows = value_mapping_sheet.nrows
            self.get_value_mapping_row = lambda row: list(value_mapping_sheet.row_values(row))

            field_mapping_sheet = book.sheet_by_name('fields')
            self.field_mapping_nrows = field_mapping_sheet.nrows
            self.get_field_mapping_row = lambda row: list(field_mapping_sheet.row_values(row))

            data_sheet = book.sheet_by_name('data')
            self.data_nrows = data_sheet.nrows
            self.get_data_row = lambda row: list(data_sheet.row_values(row))
            self.col_names = list(data_sheet.row_values(0))

        elif self.ftype == 'csv':

            value_mapping_file = open('.'.join(self.data_file.split('.')[:-1]) + '_values.csv', 'rU')
            value_mapping_reader = list(csv.reader(value_mapping_file))
            self.value_mapping_nrows = len(value_mapping_reader)
            self.get_value_mapping_row = lambda row: value_mapping_reader[row]

            field_mapping_file = open('.'.join(self.data_file.split('.')[:-1]) + '_fields.csv', 'rU')
            field_mapping_reader = list(csv.reader(field_mapping_file))
            self.field_mapping_nrows = len(field_mapping_reader)
            self.get_field_mapping_row = lambda row: field_mapping_reader[row]

            data_file = open('.'.join(self.data_file.split('.')[:-1]) + '_data.csv', 'rU')
            data_reader = list(csv.reader(data_file))
            self.data_nrows = len(data_reader)
            self.get_data_row = lambda row: data_reader[row]
            self.col_names = data_reader[0]

        else:
            raise IOError("Instrument file must be xlsx, xls, or csv.")

    def get_row_data(self, row):

        row_values = self.get_data_row(row)
        if len(row_values) > 1:

            # get child data
            child = self.get_data_fields(self.field_mapping, 'child', row_values)

            # get administration data
            administration = self.get_data_fields(self.field_mapping, 'admin', row_values)
            if child['date_of_birth'] is not None and administration['date_of_test'] is not None:
                computed_age = self.compute_age(child['date_of_birth'], administration['date_of_test'])
                administration['age'] = computed_age
            else:
                administration['age'] = administration['data_age']
            if not 'norming' in administration:
                administration['norming'] = self.norming

            # get item data
            item_data = self.get_data_fields(self.field_mapping, 'item', row_values)
            administration['item_data'] = item_data

            return child, administration

    def import_data(self):

        self.get_meta_data()
        self.value_mapping = self.map_values()
        self.field_mapping = self.map_fields()
        self.col_map = self.map_cols()

        # go through the datasheet entries and populate all the data
        for row in xrange(1, self.data_nrows):
            child, administration = self.get_row_data(row)
            self.children[row] = child
            self.administrations[row] = administration
