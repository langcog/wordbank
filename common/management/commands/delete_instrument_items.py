from django.core.management.base import NoArgsCommand
from common.models import *


class Command(NoArgsCommand):

    def handle(self, *args, **options):

        instrument_language, instrument_form = args[0], args[1]

        if Instrument.objects.filter(language=instrument_language, form=instrument_form).exists():
            instrument_obj = Instrument.objects.get(language=instrument_language, form=instrument_form)

            ItemInfo.objects.filter(instrument_id = instrument_obj.pk).delete()
