from django.core.management.base import NoArgsCommand
from common.models import *


# deletes all administration and child objects for a given instrument (language and form)
class Command(NoArgsCommand):

    def handle(self, *args, **options):

        instrument_language, instrument_form = args[0], args[1]

        if InstrumentsMap.objects.filter(language=instrument_language, form=instrument_form).exists():
            instrument_obj = InstrumentsMap.objects.get(language=instrument_language, form=instrument_form)
            for administration in Administration.objects.filter(instrument=instrument_obj.pk):
                if Child.objects.filter(pk=administration.child.pk).exists():
                    Child.objects.filter(pk=administration.child.pk).delete()
                else:
                    administration.delete()
        else:
            raise IOError("Invalid instrument.")