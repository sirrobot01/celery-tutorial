from django.http.response import HttpResponse
from django.http import JsonResponse
from celeryapp.utils import TaskRunner
from .tasks import send_email
import json
# Create your views here.

def home(request):

    data = {"result": {
        "a": [1, 2, 3, 4],
        "b": [5, 6, 7, 8]
    }}

    task = TaskRunner('send_email', send_email, args=["akeremukhtar10@gmail.com"]).run()

    return JsonResponse(data=data)

