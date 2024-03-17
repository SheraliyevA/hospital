from django.shortcuts import render
from django.shortcuts import render
from django.db.models import Q, F, Count, Sum, Min, Max
from django.utils import timezone
from datetime import datetime, timedelta

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser
from django.db.models import Sum

from .models import *
from .serializers import *
from rest_framework import mixins
from rest_framework import generics

class BemorList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset=Bemor.objects.all()
    serializer_class = BemorSer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class BemorDetail(APIView):
    parser_classes = [MultiPartParser, JSONParser]
    def get(self, request, id):
        try:
            bemor = Bemor.objects.get(id=id)
            ser = BemorSer(bemor)
            if Tashxis.objects.filter(bemor=bemor):
                tashxis = Tashxis.objects.filter(bemor=bemor)
                c = {}
                sum_narx = tashxis.aggregate(Sum('narx'))
                sum_tuladi = tashxis.aggregate(Sum('tuladi'))
                sum_qoldi = tashxis.aggregate(Sum('qoldi'))
                sum_tash = Tashxis.objects.filter(bemor=bemor).count()
                c['sum_narx'] = sum_narx['narx__sum']
                c['sum_tuladi'] = sum_tuladi['tuladi__sum']
                c['sum_qoldi'] = sum_qoldi['qoldi__sum']
                c['tashxislar'] = sum_tash
                d = []
                for x in tashxis:
                    found = False
                    for item in d:
                        if item['tashxislar'] == x.lecheniya:
                            item['narx'] += x.narx
                            item['tuladi'] += x.tuladi
                            item['qoldi'] += x.qoldi
                            item['tashxis'] += 1
                            found = True
                            break
                    if not found:
                        d.append({'tashxislar': x.lecheniya, 'narx': x.narx,
                                  'tuladi': x.tuladi, 'qoldi': x.qoldi,
                                  'tashxis_soni': 1,})
                return Response({'data': ser.data,
                                 'all_statistic': c,
                                 'statistic': d})
            return Response({'data': ser.data,
                                 'all_statistic': None,
                                 'statistic': None})
        except:
            return Response({'message': 'Not found'})
    
    def patch(self, request, id):
        xodim = Bemor.objects.filter(id=id).first()
        ser = BemorSer(xodim, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    
    def delete(self, request, id):
        xodim = Bemor.objects.filter(id=id).first()
        xodim.delete()
        return Response({'message': 'Deleted'})
    
class TashxisList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Tashxis.objects.all()
    serializer_class = TashxisGetSer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

# class TashxisList(APIView):
#     parser_classes = (MultiPartParser, JSONParser)
#     def get(self, request):
#         tashxis = Tashxis.objects.all()
#         serializer = TashxisGetSer(tashxis, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = TashxisSer(data=request.data)
#         if serializer.is_valid():
#             a = request.data.get('narx', None)
#             b = request.data.get('tuladi', None)
#             t = serializer.save()
#             if a and b:
#                 t.qoldi = t.narx-t.tuladi
#                 t.save()
#             elif a:
#                 t.qoldi = t.narx
#                 t.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


class TashxisDetail(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request, id):
        tashxis = Tashxis.objects.get(id=id)
        serializer = TashxisGetSer(tashxis)
        return Response(serializer.data)

    def patch(self, request, id):
        tashxis = Tashxis.objects.get(id=id)
        serializer = TashxisSer(tashxis, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        xodim = Tashxis.objects.filter(id=id).first()
        xodim.delete()
        return Response({'message': 'Deleted'})

# Create your views here.
