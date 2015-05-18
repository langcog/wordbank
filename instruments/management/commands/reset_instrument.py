from django.core.management.base import BaseCommand
from common.models import *
import instruments.models


# deletes all data and administration and child objects for a given instrument (language and form)
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-l', '--language', type=str)
        parser.add_argument('-f', '--form', type=str)

    def handle(self, *args, **options):

        input_language, input_form = options['language'], options['form']

        instrument_string = '_'.join(input_language.split() + [input_form])
        instrument_model = getattr(instruments.models, instrument_string)
        instrument_model.objects.all().delete()

        if Instrument.objects.filter(language=input_language, form=input_form).exists():
            instrument_obj = Instrument.objects.get(language=input_language, form=input_form)
            for administration in Administration.objects.filter(instrument=instrument_obj.pk):
                if Child.objects.filter(pk=administration.child.pk).exists():
                    Child.objects.filter(pk=administration.child.pk).delete()
                else:
                    administration.delete()
        else:
            raise IOError("Invalid instrument.")