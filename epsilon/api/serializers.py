from rest_framework import serializers
from .models import Item,Item1,Item2,Item3,Item4,Item5

class ItemSerializer(serializers.ModelSerializer):
        class Meta :
                model = Item
                fields = '__all__'

class ItemSerializer1(serializers.ModelSerializer):
        class Meta :
                model = Item1
                fields = '__all__'

class ItemSerializer2(serializers.ModelSerializer):
        class Meta :
                model = Item2
                fields = '__all__'

class ItemSerializer3(serializers.ModelSerializer):
        class Meta :
                model = Item3
                fields = '__all__'

class ItemSerializer4(serializers.ModelSerializer):
        class Meta :
                model = Item4
                fields = '__all__'

class ItemSerializer5(serializers.ModelSerializer):
        class Meta :
                model = Item5
                fields = '__all__'
