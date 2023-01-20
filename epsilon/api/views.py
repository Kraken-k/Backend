from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item,Item5,Item1,Item2,Item3,Item4
from .serializers import ItemSerializer,ItemSerializer2,ItemSerializer3,ItemSerializer1,ItemSerializer4,ItemSerializer5

@api_view(['GET','PUT'])
def getdata(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getdata1(request):
    items = Item1.objects.all()
    serializer = ItemSerializer1(items,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getdata3(request):
    items = Item3.objects.all()
    serializer = ItemSerializer2(items,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getdata2(request):
    items = Item2.objects.all()
    serializer = ItemSerializer3(items,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getdata4(request):
    items = Item4.objects.all()
    serializer = ItemSerializer4(items,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getdata5(request):
    items = Item5.objects.all()
    serializer = ItemSerializer5(items,many = True)
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addItem1(request):
    serializer = ItemSerializer1(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addItem2(request):
    serializer = ItemSerializer2(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addItem3(request):
    serializer = ItemSerializer3(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addItem4(request):
    serializer = ItemSerializer4(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addItem5(request):
    serializer = ItemSerializer5(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
