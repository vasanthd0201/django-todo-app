from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Runs migrations and creates superuser'

    def handle(self, *args, **kwargs):
        call_command('migrate')
        # Optional: create a superuser (without prompt)
        from django.contrib.auth import get_user_model
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'vasanthcyetechnology@gmail.com', 'Vasu@123')
            self.stdout.write("Superuser created")
        else:
            self.stdout.write("Superuser already exists")
