from rest_framework import serializers
from .models import help

class HelpSerializer(serializers.ModelSerializer):
   class Meta: 
    model = help
    fields = '__all__'


class ResHelp(serializers.ModelSerializer):
   class Meta: 
    model = help
    fields = ('ids',"send")


