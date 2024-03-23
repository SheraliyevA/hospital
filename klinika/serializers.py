from rest_framework import serializers
from .models import *
from user.serializers import UserSer

class BemorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bemor
        fields = '__all__'

class TashxisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tashxis
        fields = '__all__'
