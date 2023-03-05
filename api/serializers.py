from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):
        class Meta :
                model = gardian
                fields = '__all__'

class ItemSerializer1(serializers.ModelSerializer):
        class Meta :
                model = student
                fields = '__all__'
                
                
class ItemSerializer3(serializers.ModelSerializer):
        class Meta :
                model = admin
                fields = '__all__'

class ItemSerializer4(serializers.ModelSerializer):
        class Meta :
                model = subject
                fields = '__all__'

class ItemSerializer5(serializers.ModelSerializer):
        class Meta :
                model = schedule
                fields = '__all__'

class S_Home(serializers.ModelSerializer):
        class Meta:
                model = teacher
                fields = ("T_id","Name","Expert_IN","Review","Photo","Payment",)

class RegistrationTeacher(serializers.ModelSerializer):
        class Meta:
                model= teacher
                fields = '__all__'
class T_Home(serializers.ModelSerializer):
        class Meta:
                model = gardian
                fields = '__all__'
                depth = 1

class RegistrationStudent(serializers.ModelSerializer):
        class Meta:
                model= student
                fields = '__all__'

class DiabilitySerializer(serializers.ModelSerializer):
        class Meta:
                model = Disability
                fields = '__all__'

class RegistrationGardian(serializers.ModelSerializer):
        class Meta:
                model= gardian
                fields = ("S_id","G_Name","contact_number","Relationship","Gender","Addresse","gmail")

class Attented(serializers.ModelSerializer):
        class Meta:
                model = Attendence
                fields = ("T_id","Fingerprint","Date","Start_time","End_time")

class Request1(serializers.ModelSerializer):
        class Meta:
                model = Request
                fields = '__all__'
class Request2(serializers.ModelSerializer):
        class Meta:
                model = Request
                fields = '__all__'
                depth = 1


class Accept2(serializers.ModelSerializer):
        class Meta:
                model = Accept
                fields = ("Accept_id","room_name","is_accepted")
                depth = 1

class Accept1(serializers.ModelSerializer):
        class Meta:
                model = Accept
                fields = ("Accept_id","room_name","is_accepted")


