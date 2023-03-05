from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
import requests


def get(request,room_name):
        post_data = {"room_name":room_name}
        requests.get("http://127.0.0.1:8000/chat/rooms",post_data)
           