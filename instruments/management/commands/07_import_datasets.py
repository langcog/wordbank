import json
from django.core.management.base import BaseCommand
from instruments.import_dataset import import_dataset
from django.core.mail import send_mail
from django.db.models import Q
from common.models import Administration, Dataset, Instrument


# Given no arguments, imports all datasets in 'static/json/datasets.json'.
# Given a language with -l and a form with -f imports datasets in 'static/json/datasets.json' that have the matching
# `instrument_language` and `instrument_form`.
# Given a file with --file, imports the dataset in 'static/json/datasets.json' that has the matching `file`.
class Command(BaseCommand):
    send_email = False

    def add_arguments(self, parser):
        parser.add_argument("-l", "--language", type=str)
        parser.add_argument("-f", "--form", type=str)
        parser.add_argument("-d", "--dataset", type=str)
        parser.add_argument("-o", "--origin", type=str)
        parser.add_argument("-a", "--file", type=str)
        parser.add_argument("-e", "--email", type=str)

    def handle(self, *args, **options):
        if options["email"]:
            self.send_email = True

        query = Q()

        if (
            options["language"]
            or options["form"]
            or options["dataset"]
            or options["file"]
            or options["origin"]
        ):
            if options["language"]:
                query = Q(query) & Q(instrument__language=options["language"])

            if options["form"]:
                query = Q(query) & Q(instrument__form=options["form"])

            if options["dataset"]:
                query = Q(query) & Q(source=options["dataset"])

            if options["file"]:
                query = Q(query) & Q(file_location=options["file"])

            if options["origin"]:
                query = Q(query) & Q(dataset_origin=options["origin"])

        datasets = Dataset.objects.filter(query)

        print(f'Datasets: {datasets}')

        for dataset in datasets:
            
            msg = f"Importing dataset {dataset}"
            print(msg)

            administrations = Administration.objects.filter(dataset=dataset)
                
            print(f"   Deleting {len(administrations)} exisiting records")
            for admin in administrations:
                try:
                    if admin.content_object:
                        admin.content_object.delete()
                except:
                    pass
                admin.delete()
            print("   Importing records")
            import_dataset(
                dataset.dataset_name,
                dataset.source,
                dataset.file_location,
                dataset.instrument.language,
                dataset.instrument.form,
                dataset.splitcol,
                dataset.norming,
                dataset.date_format,
                dataset.dataset_origin,
            )

            if self.send_email:
                send_mail(
                    msg,
                    msg,
                    "webcdi-contact@gmail.com",
                    ["hjsmehta@gmail.com", "henrymehta@hotmail.com"],
                    fail_silently=False,
                )
