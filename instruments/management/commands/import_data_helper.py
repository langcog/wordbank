import xlrd
import string
from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import defaultdict


class ImportHelper:

    def __init__(self, path_to_data_file, data_file, instrument_model):
        self.path = path_to_data_file
        self.data_file = data_file
        self.instrument_model = instrument_model
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

    def get_field_value(self, field, field_type, row_values):
        if field in self.col_map:
            value = row_values[self.col_map[field]]
            if value != 'Null' and value != '':
                if field in ('study_id'):
                    return value
                elif field_type in ('birth_order', 'data_age', 'mom_ed'):
                    return int(value)
                elif field_type in ('date_of_birth, date_of_test'):
                    return self.format_date(value, self.datemode)
                elif field_type in ('ethnicity', 'sex', 'word', 'usage', 'word_form', 'combine', 'complexity'):
                    if value in self.field_value_mapping[field_type]:
                        return self.field_value_mapping[field_type][value]

    def get_data_fields(self, cols, row_values):
        results = defaultdict(lambda: None)
        for column in cols.keys():
            field = cols[column]['field']
            field_type = cols[column]['field_type']
            field_value = self.get_field_value(field, field_type, row_values)
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

        value_mapping_sheet = book.sheet_by_name('value_mapping')
        for row in xrange(1, value_mapping_sheet.nrows):
            row_values = list(value_mapping_sheet.row_values(row))
            field_type, value, data_value = row_values[:3]
            self.field_value_mapping[field_type][data_value] = value

        field_mapping_sheet = book.sheet_by_name('field_mapping')
        cols = defaultdict(lambda: dict())
        for row in xrange(1, field_mapping_sheet.nrows):
            row_values = list(field_mapping_sheet.row_values(row))
            field, column, category, field_type = row_values[:4]
            if category == 'item':
                field = 'item_' + string.replace(field, '.', '_')
            cols[category][column.lower()] = {'field': field, 'field_type': field_type}

        for index, value in enumerate(col_names):
            if value.lower() in cols['admin'].keys():
                    self.col_map[cols['admin'][value.lower()]['field']] = index
            elif value.lower() in cols['child'].keys():
                self.col_map[cols['child'][value.lower()]['field']] = index
            elif value.lower() in cols['item'].keys():
                self.col_map[cols['item'][value.lower()]['field']] = index

        for row in xrange(1, data_sheet.nrows):
            row_values = list(data_sheet.row_values(row))

            child = self.get_data_fields(cols['child'], row_values)
            self.children[row] = child

            administration = self.get_data_fields(cols['admin'], row_values)
            administration['source_name'] = self.source_name
            administration['source_dataset'] = self.source_dataset

            if child['date_of_birth'] and administration['date_of_test']:
                computed_age = self.compute_age(administration['date_of_test'], child['date_of_birth'])
                administration['age'] = computed_age

            instrument_data = self.get_data_fields(cols['item'], row_values)
            administration['instrument_data'] = instrument_data

            self.administrations[row] = administration