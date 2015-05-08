from django.core.management.base import NoArgsCommand
from common.models import *
import instruments.models


# deletes all data and administration and child objects for a given instrument (language and form)
class Command(NoArgsCommand):

    def handle(self, *args, **options):

        instrument_language, instrument_form = args[0], args[1]

        instrument_string = '_'.join(instrument_language.split() + [instrument_form])
        instrument_model = getattr(instruments.models, instrument_string)
        instrument_model.objects.all().delete()

        if Instrument.objects.filter(language=instrument_language, form=instrument_form).exists():
            instrument_obj = Instrument.objects.get(language=instrument_language, form=instrument_form)
            for administration in Administration.objects.filter(instrument=instrument_obj.pk):
                if Child.objects.filter(pk=administration.child.pk).exists():
                    Child.objects.filter(pk=administration.child.pk).delete()
                else:
                    administration.delete()
        else:
            raise IOError("Invalid instrument.")