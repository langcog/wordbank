import xlrd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import defaultdict


class ImportHelper:

    def __init__(self, path_to_data_file, data_file, instrument_model):
        self.path = path_to_data_file
        self.data_file = data_file
        self.instrument_model = instrument_model
        self.special_col_map = {}
        self.children = {}
        self.administrations = {}
        self.source_name = None
        self.source_dataset = None

    @staticmethod
    def get_ethnicity(ethnic):
        if ethnic == 'A':
            return 1
        if ethnic == 'B':
            return 2
        if ethnic == 'H':
            return 3
        if ethnic == 'W':
            return 4
        else:
            val = int(ethnic)
            if 0 < val < 6:
                return val
            return 5

    @staticmethod
    def format_date(date_str, datemode=None):
        return datetime(*xlrd.xldate_as_tuple(date_str, datemode))

    @staticmethod
    def compute_age(date_of_birth, date_of_test):
        age = relativedelta(date_of_test, date_of_birth)
        avg_month = 365.2425/12.0
        return int(age.years*12 + age.months + float(age.days) / avg_month)

    def valid_field(self, field, row_values):
        if field in self.special_col_map:
            value = row_values[self.special_col_map[field]]
            if value != 'Null' and value != '':
                return value

    def import_data(self):

        if '_' in self.data_file:
            self.source_name, self.source_dataset = self.data_file.split('_')
        else:
            self.source_name, self.source_dataset = self.data_file, ''

        book = xlrd.open_workbook(self.path)
        data_sheet = book.sheet_by_name('data')
        col_names = list(data_sheet.row_values(0))

        mapping_sheet = book.sheet_by_name('mapping')
        special_cols = {}
        for row in xrange(mapping_sheet.nrows):
            k, v = list(mapping_sheet.row_values(row))
            special_cols[k] = v

        for special_col in special_cols:
            for index, value in enumerate(col_names):
                if value.lower() == special_cols[special_col].lower():
                    self.special_col_map[special_col] = index
                    break

        for row in xrange(1, data_sheet.nrows):
            row_values = list(data_sheet.row_values(row))

            child = defaultdict(lambda: None)

            study_id = self.valid_field('study_id', row_values)
            if study_id:
                child['study_id'] = study_id

            date_of_birth = self.valid_field('date_of_birth', row_values)
            if date_of_birth:
                child['date_of_birth'] = self.format_date(date_of_birth, book.datemode)

            gender = self.valid_field('gender', row_values)
            if gender:
                child['gender'] = gender

            birth_order = self.valid_field('birth_order', row_values)
            if birth_order:
                child['birth_order'] = int(birth_order)

            mom_ed = self.valid_field('mom_ed', row_values)
            if mom_ed:
                child['mom_ed'] = int(mom_ed)

            ethnic = self.valid_field('ethnic', row_values)
            if ethnic:
                ethnic_num = self.get_ethnicity(ethnic)
                child['ethnic_num'] = ethnic_num

            self.children[row] = child

            administration = defaultdict(lambda: None)

            date_of_test = self.valid_field('date_of_test', row_values)
            if date_of_test:
                administration['date_of_test'] = self.format_date(date_of_test, book.datemode)

            data_age = self.valid_field('age', row_values)
            if data_age:
                administration['data_age'] = int(data_age)

            if date_of_birth and date_of_test:
                computed_age = self.compute_age(administration['date_of_test'], child['date_of_birth'])
                administration['age'] = computed_age

            administration['source_name'] = self.source_name
            administration['source_dataset'] = self.source_dataset

            # Parse all the fields for the given data entry here.
            instrument_data = {}
            col_name_index = 0
            existing_col_names = [d.name for d in self.instrument_model._meta.fields]
            for value in row_values:
                column_name = 'col_'+col_names[col_name_index].lower()
                if column_name in existing_col_names:
                    instrument_data[column_name] = int(value)
                col_name_index += 1

            administration['instrument_data'] = instrument_data

            self.administrations[row] = administration