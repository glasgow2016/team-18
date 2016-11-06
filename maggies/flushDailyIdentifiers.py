import os

''' Anonymisation of Visitors Script
        This script empties the DailyIdentifiers table in order to anonymise Visitors.
        Shold be run daily with a cronjob on the server storing the database.
'''

if __name__ == '__main__':
    print("Resetting DailyIdentifier table to keep anonymity...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maggies.settings')
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    from maggies.models import DailyIdentifier
    from django.conf import settings
    DailyIdentifier.objects.all().delete()
