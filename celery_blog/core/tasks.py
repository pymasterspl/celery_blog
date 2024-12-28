from celery import shared_task
import time

@shared_task
def example_task(duration):
    """Proste zadanie symulujące długotrwały proces."""
    time.sleep(duration)  # Symulacja opóźnienia
    return f"Zadanie zakończone po {duration} sekundach"