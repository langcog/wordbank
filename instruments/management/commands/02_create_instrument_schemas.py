import xlrd
import codecs
import json
import string
from django.core.management.base import BaseCommand
import csv


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-l", "--language", type=str)
        parser.add_argument("-f", "--form", type=str)

    def handle(self, *args, **options):
        instruments = json.load(open("static/json/instruments.json"))

        if options["language"] and options["form"]:
            input_language, input_form = options["language"], options["form"]
            input_instruments = [
                instrument
                for instrument in instruments
                if instrument["language"] == input_language
                and instrument["form"] == input_form
            ]
            models_file = open("instruments/models.py", "a")
        else:
            input_instruments = instruments
            models_file = open("instruments/models.py", "w")

        print(f"Input Intruments: {input_instruments}")
        print(f"Language: {input_language}; Form: {input_form}")
        for instrument in input_instruments:
            var_safe = lambda s: "".join(
                [c for c in "_".join(s.split()) if c in string.ascii_letters + "_"]
            )
            instr = (
                var_safe(instrument["language"]) + "_" + var_safe(instrument["form"])
            )
            instrument_file = open("instruments/schemas/%s.py" % (instr), "w")

            instrument_file.write("from django.db import models\n")
            instrument_file.write("from instruments.base import BaseTable\n")

            ftype = instrument["file"].split(".")[-1]

            if ftype == "xlsx" or ftype == "xls":
                sheet = xlrd.open_workbook(instrument["file"]).sheet_by_index(0)
                col_names = list(sheet.row_values(0))
                nrows = sheet.nrows
                get_row = lambda row: list(sheet.row_values(row))
            elif ftype == "csv":
                with open(
                    instrument["file"], newline="", encoding="utf-8-sig"
                ) as csvfile:
                    reader = csv.reader(csvfile, delimiter=",", quotechar='"')
                    lines = [row for row in reader]
                    col_names = lines[0]
                    nrows = len(lines)
                    get_row = lambda row: lines[row]
            else:
                raise IOError("Instrument file must be xlsx, xls, or csv.")

            instrument_file.write("\n\nclass %s(BaseTable):\n" % instr)

            if nrows <= 1:
                instrument_file.write("    pass\n")

            for row in range(1, nrows):
                row_values = get_row(row)
                if len(row_values) > 1:
                    itemID = row_values[col_names.index("itemID")]
                    # Override max_length and ignore choices
                    """
                    choices = row_values[col_names.index('choices')].split(';')
                    max_length = max(len(c) for c in choices)  
                    instrument_file.write('    %s_choices = %s\n' % (itemID, [(c.lstrip().rstrip(),c.lstrip().rstrip()) for c in choices]))
                    """
                    max_length = 11
                    instrument_file.write(
                        f"    {itemID} = models.CharField(max_length={max_length}, null=True)\n"
                    )

            instrument_file.close()
            models_file.write("from .schemas.%s import *\n" % (instr))

        models_file.close()
