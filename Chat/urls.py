from django.urls import include, path, re_path
from . import views
from .consumers import ChatConsumer
from api.Teacher_view import *

urlpatterns = [
    path('<str:Accept_id>/<str:room_name>/', Room_name, name='chat'),
    path('makeroom/',Make_name.as_view()),
    path('getroom/',GET_room)

]
    

