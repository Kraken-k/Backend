from rest_framework.response import Response 
from rest_framework.decorators import api_view , action
from rest_framework.views import APIView
from .models import *
from django.http import JsonResponse
from .serializers import *
from .Student_serializer import *
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser


class S_Registration(APIView):
    def post(self,request):
        serializers=RegistrationStudent(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
class G_Registration(APIView):
    def post(self,request):
        serializers=RegistrationGardian(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
@api_view(["GET"])    
def TGET(request):
       if request.method=="GET": 
        data = teacher.objects.all()
        serializers = S_Home(data,many=True)
        return Response(serializers.data)

@api_view(["Post"])
def Student_Request(request):
    serializers=Request1(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors) 


class T_Attendence(APIView):
    def post(self,request):
        serializers=Attented(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    

class Uplode_ProfilePic(APIView):
    def put(self,request):
        serializers=ProfileSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    


class Uplode_ProfilePic(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = 'S_id'

    def get_queryset(self):
        return student.objects.filter(S_id=self.kwargs['S_id'])

    def put(self, request, *args, **kwargs):
        student = self.get_object()
        student.ProfilePic = request.data.get('ProfilePic')
        student.save()
        serializer = self.serializer_class(student)
        return Response(serializer.data)

@api_view(['GET'])
def getid(request):
    if request.method=="GET": 
        data = student.objects.all()
        serializers = RegistrationSerializer2(data,many=True)
        return Response(serializers.data)