from django.core.management.base import BaseCommand
from common.models import *


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