from rest_framework.response import Response 
from rest_framework.decorators import api_view , action
from rest_framework.views import APIView
from .models import *
from django.http import HttpResponse, JsonResponse
from .serializers import *
import requests

class T_Registration(APIView):
    def post(self,request):
        serializers=RegistrationTeacher(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

@api_view(["GET"])    
def SGET(request):
        if request.method=="GET": 
            data = gardian.objects.all()
            serializers = T_Home(data,many=True)
            return Response(serializers.data)
        
@api_view(["GET"])    
def request_GET(request):
        if request.method=="GET": 
            data = Request.objects.all()
            serializers = Request2(data,many=True)
            return Response(serializers.data)
 

class Make_name(APIView):
       def post(self,request):
        serializers=Accept1(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
       

def Room_name(request,Accept_id,room_name): 
      post_data = {'Accept_id':Accept_id,'room_name':room_name, 'is_accepted': 1}
      if requests.post(url="http://127.0.0.1:8000/chat/makeroom/", data = post_data):
         return JsonResponse(post_data)
      return HttpResponse("Room is Not made")


@api_view(["GET"])    
def GET_room(request):
        if request.method=="GET": 
            data = Accept.objects.all()
            serializers = Accept2(data,many=True)
            return Response(serializers.data)


def get_id(request):
     data = list(teacher.objects.values("T_id"))
     return JsonResponse(data , safe = False)