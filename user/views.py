from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q, F, Sum, Min, Max

from .serializers import *
from .models import *
# from klinika.models import Tashxis

class ChangePasswordView(APIView):
    parser_classes = [MultiPartParser, JSONParser]
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            user = self.request.user
            old_password = serializer.data.get('old_password')
            new_password = serializer.data.get('new_password')

            if not user.check_password(old_password):
                return Response({'detail': 'Old password is incorrect.'})

            user.set_password(new_password)
            user.save()
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)
            return Response({'detail': 'Password changed successfully.',
                             'access_token': access,
                             'refresh_token': str(refresh)
                             })

        return Response(serializer.errors)

class SignUp(APIView):
    parser_classes = [MultiPartParser, JSONParser]
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        user = User.objects.all()
        ser = UserSer(user, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = UserSer(data=request.data)
        if ser.is_valid():
            status_d = ser.validated_data.get('status')
            if status_d in ['Direktor']:
                if User.objects.filter(status=status_d).exists():
                    return Response({'message': f'Bunday {status_d} Tayinlab Bulingan'})
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

# Create your views here.

# Create your views here.
