import os
from celery import Celery

# Ustawienie domyślnego modułu ustawień Django dla aplikacji Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_blog.settings')

app = Celery('celery_blog')

# Ładowanie konfiguracji z pliku settings.py z prefiksem CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatyczne wykrywanie zadań we wszystkich aplikacjach Django
app.autodiscover_tasks()
