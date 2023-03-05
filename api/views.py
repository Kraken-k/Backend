from rest_framework.response import Response 
from rest_framework.decorators import api_view , action
from rest_framework.views import APIView
from .models import *
from django.http import JsonResponse
from .serializers import *
from django.http import HttpResponse
from django.template import Template
# @api_view(['GET','POST'])
# def Gardian(request):
#     if request.method=='GET':
#         items = gardian.objects.all()
#         serializer = ItemSerializer(items,many = True)
#         return Response(serializer.data)
    
#     if request.method=='POST':
#         serializer = ItemSerializer(data = request.data)
#         if serializer.is_valid():
#            serializer.save()
#         return Response(serializer.data)
    
# @api_view(['GET','POST'])
# def Student(request):
#      if request.method=='GET':
#         items = student.objects.all()
#         serializer = ItemSerializer1(items,many = True)
#         return Response(serializer.data)
    
#      if request.method=='POST':
#         serializer = ItemSerializer1(data = request.data)
#         if serializer.is_valid():
#            serializer.save()
#         return Response(serializer.data)

# @api_view(['GET','POST'])
# def Teacher(request):
#    if request.method=='GET':
#         items = teacher.objects.all()
#         serializer = T_Registration(items,many = True)
#         return Response(serializer.data)

@api_view(['GET','POST'])
def Admin(request):
    if request.method=='GET':
        items = admin.objects.all()
        serializer = ItemSerializer3(items,many = True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer = ItemSerializer3(data = request.data)
        if serializer.is_valid():
           serializer.save()
        return Response(serializer.data) 

@api_view(['GET','POST'])
def Subject(request):
    if request.method=='GET':
        items = subject.objects.all()
        serializer = ItemSerializer4(items,many = True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer = ItemSerializer4(data = request.data)
        if serializer.is_valid():
           serializer.save()
        return Response(serializer.data)

@api_view(['GET','POST'])
def Schedule(request):
    if request.method=='GET':
        items = schedule.objects.all()
        serializer = ItemSerializer5(items,many = True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer = ItemSerializer5(data = request.data)
        if serializer.is_valid():
           serializer.save()
        return Response(serializer.data)

   
@api_view(["POST","GET"])
def Disabilitys(request):
    if request.method == 'POST':
        serializers = DiabilitySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors) 
    if request.method =='GET':
        items = Disability.objects.all()
        serializers = DiabilitySerializer(items,many=True)
        return Response(serializers.data)
    
    

       



    




    




    
   


    
