from django.core.management.base import NoArgsCommand
from common.models import *


class Command(NoArgsCommand):

    def handle(self, *args, **options):

        ed_levels = {(1, 'None'),
                     (2, 'Primary'),
                     (3, 'Some Secondary'),
                     (4, 'Secondary'),
                     (5, 'Some College'),
                     (6, 'College'),
                     (7, 'Some Graduate'),
                     (8, 'Graduate')}

        for ed_order, ed_level in ed_levels:
            MomEd.objects.create(level=ed_level, order=ed_order)