from django.core.management.base import NoArgsCommand
from common.models import *
import instruments.models


class Command(NoArgsCommand):

    def handle(self, *args, **options):

        instrument_language, instrument_form = args[0], args[1]

        instrument_model = getattr(instruments.models, '_'.join([instrument_language, instrument_form]))
        instrument_obj = InstrumentsMap.objects.get(language=instrument_language, form=instrument_form)

        # broken for now, do not use
        # for administration in Administration.objects.filter(instrument=instrument_obj.pk):
        #     Child.objects.get(pk=administration.child.pk).delete()
        #     administration.delete()
        #
        # for word_map in WordMapping.objects.filter(instrument=instrument_obj.pk):
        #     WordInfo.objects.get(pk=word_map.word_info.pk).delete()
        #     word_map.delete()
        #
        # instrument_obj.delete()