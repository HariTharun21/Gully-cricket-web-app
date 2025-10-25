import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cricket.settings")
django.setup()

from django.conf import settings
print(settings.INSTALLED_APPS)