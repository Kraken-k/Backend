from rest_framework.response import Response
from .models import help
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view

class HelpView(APIView):
    def post(self,request):
        serializers=HelpSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)


@api_view(["GET"])    
def helpres(request):
       if request.method=="GET": 
        data = help.objects.all()
        serializers = ResHelp(data,many=True)
        return Response(serializers.data)