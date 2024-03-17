from rest_framework import serializers
from .models import *
from user.serializers import UserSer

class BemorSer(serializers.ModelSerializer):
    class Meta:
        model = Bemor
        fields = ('id', 'first_name', 'last_name', 'dad_name', 'phone', 'address', 'date', 'created_at', 'user')


class BemorGetSer(serializers.ModelSerializer):
    user = UserSer()
    class Meta:
        model = Bemor
        fields = ('id', 'first_name', 'last_name', 'dad_name', 'phone', 'address', 'date', 'created_at', 'user')

class TashxisSer(serializers.ModelSerializer):
    class Meta:
        model = Tashxis
        fields = '__all__'
    

class TashxisGetSer(serializers.ModelSerializer):
    user = UserSer()
    bemor = BemorSer()
    class Meta:
        model = Tashxis
        fields = ['id', 'user', 'bemor', 'tashxis',"lecheniya",'date', 'created_at', 'narx', 'tuladi', 'qoldi']