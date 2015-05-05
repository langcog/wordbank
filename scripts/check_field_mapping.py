import sys
import xlrd
from collections import defaultdict
from difflib import SequenceMatcher as SM

def check_field_mapping(instrument_file, data_file, threshold=0.7):

    data_book = xlrd.open_workbook(data_file)

    # make a mapping between datasheet column names and model field names/types
    field_mapping_sheet = data_book.sheet_by_name('fields')
    cols = defaultdict(lambda: dict())
    for row in xrange(1, field_mapping_sheet.nrows):
        row_values = list(field_mapping_sheet.row_values(row))
        field, column, group, field_type = row_values[:4]
        if column is not None and column != '' and group == "item":
            cols[field] = column.lower()

    instrument_book = xlrd.open_workbook(instrument_file)

    sheet = instrument_book.sheet_by_index(0)
    col_names = list(sheet.row_values(0))
    items = defaultdict(lambda: dict())

    for row in xrange(1, sheet.nrows):

        row_values = list(sheet.row_values(row))
        itemID = row_values[col_names.index('itemID')]
        item = row_values[col_names.index('item')]
        items[itemID] = item

    assert(set(cols.keys()).issubset(set(items.keys())))

    bad_items = []
    for itemID in sorted(cols.keys()):
        item = items[itemID]
        data_item = cols[itemID]
        match = SM(None, data_item, item).ratio()
        str_data_item = ''.join([i for i in data_item if not i.isdigit()])
        if match < threshold and not (str_data_item in item or item in str_data_item):
            approve = raw_input("Is %s the same as %s?" % (data_item, item))
            if approve == 'n' or approve == 'no':
                bad_items.append((data_item, item))

    if bad_items:
        print "\nProblematic items:"
        data_width = max([len(i) for i in [b[0] for b in bad_items]])
        for data_item, instrument_item in bad_items:
            print data_item, " " * (data_width - len(data_item)), "| ", instrument_item
    else:
        print "\nNo problematic items!"

if __name__ == "__main__":
    check_field_mapping(sys.argv[1], sys.argv[2])