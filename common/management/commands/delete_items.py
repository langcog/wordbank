from django.core.management.base import BaseCommand
from common.models import *


# Given no arguments, deletes all ItemInfo objects and ItemMap objects.
# Given a language with -l and a form with -f, deletes the ItemInfo objects that correspond to their Instrument object.
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-l', '--language', type=str)
        parser.add_argument('-f', '--form', type=str)

    def handle(self, *args, **options):

        if options['language'] and options['form']:

            input_language, input_form = options['language'], options['form']

            if Instrument.objects.filter(language=input_language, form=input_form).exists():
                instrument_obj = Instrument.objects.get(language=input_language, form=input_form)

                ItemInfo.objects.filter(instrument_id = instrument_obj.pk).delete()

        else:

            ItemInfo.objects.all().delete()
            ItemMap.objects.all().delete()