from django.shortcuts import render

from django.http import JsonResponse
from django.views import View
from .tasks import example_task
from celery.result import AsyncResult



class RunTaskView(View):
    def post(self, request, *args, **kwargs):
        # Uruchomienie zadania asynchronicznego
        duration = int(request.POST.get("duration", 5))  # Pobranie czasu z żądania (domyślnie 5 sekund)
        result = example_task.delay(duration)  # Zadanie dodane do kolejki
        return JsonResponse({"task_id": result.id, "status": "Task started"})

class TaskStatusView(View):
    def get(self, request, task_id, *args, **kwargs):
        # Pobranie informacji o statusie zadania
        result = AsyncResult(task_id)
        response = {"task_id": task_id, "status": result.status}
        
        if result.ready():  # Jeśli zadanie zostało zakończone
            response["result"] = result.get()  # Pobranie wyniku
        
        return JsonResponse(response)