from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        default_admin = "hjsmehta@gmail.com"
        if not User.objects.filter(username=default_admin).exists():
            User.objects.create_superuser(default_admin, password="admin")
