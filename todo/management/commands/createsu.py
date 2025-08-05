from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Create a superuser if not exists'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username=os.environ['DJANGO_SUPERUSER_USERNAME']).exists():
            User.objects.create_superuser(
                username=os.environ['DJANGO_SUPERUSER_USERNAME'],
                email=os.environ['DJANGO_SUPERUSER_EMAIL'],
                password=os.environ['DJANGO_SUPERUSER_PASSWORD']
            )
