from django.core.management.base import BaseCommand
from common.models import *
import instruments.models
import string


# deletes all data and administration and child objects for a given instrument (language and form)
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-l', '--language', type=str)
        parser.add_argument('-f', '--form', type=str)

    def handle(self, *args, **options):

        input_language, input_form = options['language'], options['form']
        if not input_language or not input_form:
            print ("You must specify both a language and a form")
            return

        var_safe = lambda s: ''.join([c for c in '_'.join(s.split()) if c in string.ascii_letters + '_'])
        instrument_string = var_safe(input_language) + '_' + var_safe(input_form)
        #instrument_string = '_'.join(input_language.split() + [input_form])
        instrument_model = getattr(instruments.models, instrument_string)
        instrument_model.objects.all().delete()

        if Instrument.objects.filter(language=input_language, form=input_form).exists():
            instrument = Instrument.objects.get(language=input_language, form=input_form)
            print(f'instrument: {instrument}')
            for administration in Administration.objects.filter(instrument=instrument):
                print(f'   administration: {administration}')
                try:
                    if administration.child:
                        print(f'        child: {administration.child.administration_set.all()}')
                        administration.child.delete()
                except:
                    pass
                administration.delete()
        else:
            raise IOError("Invalid instrument.")
