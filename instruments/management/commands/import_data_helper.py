import xlrd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import defaultdict


class ImportHelper:

    def __init__(self, path_to_data_file, data_file, instrument_model):
        self.path = path_to_data_file
        self.data_file = data_file
        self.instrument_model = instrument_model
        self.col_map = {}
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

    def valid_field(self, field, row_values):
        if field in self.col_map:
            value = row_values[self.col_map[field]]
            if value != 'Null' and value != '':
                return value

    def process_field_value(self, data_value, field_type, options):
        if not data_value is None:
            if field_type == 'string':
                return data_value
            if field_type == 'int':
                return int(data_value)
            if field_type == 'float':
                return float(data_value)
            if field_type == 'date':
                return self.format_date(data_value, self.datemode)

    def get_data_fields(self, category, cols, row_values):
        results = defaultdict(lambda: None)
        for column in filter(lambda k: cols[k]['category'] == category, cols.keys()):
            field = cols[column]['field']
            data_value = self.valid_field(field, row_values)
            field_value = self.process_field_value(data_value, cols[column]['field_type'], cols[column]['options'])
            results[field] = field_value
        return results

    def import_data(self):

        if '_' in self.data_file:
            self.source_name, self.source_dataset = self.data_file.split('_')
        else:
            self.source_name, self.source_dataset = self.data_file, ''

        book = xlrd.open_workbook(self.path)
        self.datemode = book.datemode
        data_sheet = book.sheet_by_name('data')
        col_names = list(data_sheet.row_values(0))

        mapping_sheet = book.sheet_by_name('mapping')
        cols = {}
        for row in xrange(1, mapping_sheet.nrows):
            row_values = list(mapping_sheet.row_values(row))
            field, column, category, field_type = row_values[:4]
            options = row_values[4:]
            cols[column.lower()] = {'field': field, 'category': category, 'field_type': field_type, 'options': options}

        for index, value in enumerate(col_names):
            if value.lower() in cols.keys():
                self.col_map[cols[value.lower()]['field']] = index

        for row in xrange(1, data_sheet.nrows):
            row_values = list(data_sheet.row_values(row))

            child = self.get_data_fields('child', cols, row_values)
            self.children[row] = child

            administration = self.get_data_fields('admin', cols, row_values)
            administration['source_name'] = self.source_name
            administration['source_dataset'] = self.source_dataset

            if child['date_of_birth'] and administration['date_of_test']:
                computed_age = self.compute_age(administration['date_of_test'], child['date_of_birth'])
                administration['age'] = computed_age

            instrument_data = self.get_data_fields('item', cols, row_values)
            administration['instrument_data'] = instrument_data

            self.administrations[row] = administration