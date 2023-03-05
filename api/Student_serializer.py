from rest_framework import serializers
from .models import student



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ("S_id","ProfilePic")


class RegistrationSerializer2(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ("S_id",)