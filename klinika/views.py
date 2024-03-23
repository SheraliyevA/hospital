from django.shortcuts import render
from django.utils import timezone
from datetime import datetime, timedelta

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser
from django.db.models import Count, Sum

from .models import *
from .serializers import *
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Bemor, Tashxis
from django.db.models import Count, Sum
from datetime import datetime
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractWeekDay, ExtractDay,ExtractWeek,ExtractHour,ExtractMinute



@api_view(['GET'])
def get_statistics(request, id):
    bemor = Bemor.objects.get(id=id)
    tashxis_list = Tashxis.objects.filter(bemor=bemor)
    
    tashxis_by_year = tashxis_list.annotate(year=ExtractYear('created_at')).values('year').annotate(count=Count('id'))
    tashxis_by_month = tashxis_list.annotate(month=ExtractMonth('created_at')).values('month').annotate(count=Count('id'))
    tashxis_by_week = tashxis_list.annotate(week=ExtractWeek('created_at')).values('week').annotate(count=Count('id'))
    tashxis_by_day = tashxis_list.annotate(day=ExtractDay('created_at')).values('day').annotate(count=Count('id'))

    statistics = {
        'bemor': f'{bemor.ism} {bemor.familiya}',
        'address': bemor.address,
        'tashxis_by_year': list(tashxis_by_year),
        'tashxis_by_month': list(tashxis_by_month),
        'tashxis_by_week': list(tashxis_by_week),
        'tashxis_by_day': list(tashxis_by_day)
    }
    
    return Response(statistics)

class TashxisDetail(APIView):
    def get(self, request, pk):
        bemor = Bemor.objects.get(pk=pk)
        ser = BemorSerializer(bemor)
        tashxis_list = Tashxis.objects.filter(bemor=bemor)
    
        tashxis_by_year = tashxis_list.annotate(year=ExtractYear('created')).values('year').annotate(
        count=Count('id'),
        tashxis=Count('tashxis', distinct=True),
        licheniya=Count('licheniya', distinct=True),
        # t_name=Count('tashxis__nomi', distinct=True),
        # l_name=Count('licheniya__nomi', distinct=True)
    )
        tashxis_by_month = tashxis_list.annotate(month=ExtractMonth('created')).values('month').annotate(
        count=Count('id'),
        tashxis=Count('tashxis', distinct=True),
        licheniya=Count('licheniya', distinct=True),
        # t_name=Count('tashxis__nomi', distinct=True),
        # l_name=Count('licheniya__nomi', distinct=True)
    )
        tashxis_by_week = tashxis_list.annotate(week=ExtractWeek('created')).values('week').annotate(
        count=Count('id'),
        tashxis=Count('tashxis', distinct=True),
        licheniya=Count('licheniya', distinct=True),
        # t_name=Count('tashxis__nomi', distinct=True),
        # l_name=Count('licheniya__nomi', distinct=True)
    )
        tashxis_by_day = tashxis_list.annotate(day=ExtractDay('created')).values('day').annotate(
        count=Count('id'),
        tashxis=Count('tashxis', distinct=True),
        licheniya=Count('licheniya', distinct=True),
    #     t_name=Count('tashxis__nomi', distinct=True),
    #     l_name=Count('licheniya__nomi', distinct=True)
    )
        statistics = {
        'bemor': f'{bemor.ism} {bemor.familiya}',
        'address': bemor.address,
        'tashxis_by_year': list(tashxis_by_year),
        'tashxis_by_month': list(tashxis_by_month),
        'tashxis_by_week': list(tashxis_by_week),
        'tashxis_by_day': list(tashxis_by_day)
    }
    
        if Tashxis.objects.filter(bemor=bemor):
            tashxis = Tashxis.objects.filter(bemor=bemor)
            c = {}
            sum_narx = tashxis.aggregate(Sum('jami_narxi'))
            sum_tuladi = tashxis.aggregate(Sum('tolagan_narxi'))
            sum_qoldi = tashxis.aggregate(Sum('qolgan_narxi'))
            sum_tash = Tashxis.objects.filter(bemor=bemor).count()
            c['sum_narx'] = sum_narx['jami_narxi__sum']
            c['sum_tuladi'] = sum_tuladi['tolagan_narxi__sum']
            c['sum_qoldi'] = sum_qoldi['qolgan_narxi__sum']
            c['tashxislar'] = sum_tash
            d = []
            for x in tashxis:
                found = False
                for item in d:
                    if item['tashxislar'] == x.tashxis:
                        item['licheniya']+=x.licheniya,
                        item['narx'] += x.jami_narxi
                        item['tuladi'] += x.tolagan_narxi
                        item['qoldi'] += x.qolgan_narxi
                        item['tashxis'] += 1
                        found = True
                        break
                if not found:
                    d.append({'tashxislar': x.tashxis,'licheniya':x.licheniya,'jami':x.jami_narxi,
                                  'tuladi': x.tolagan_narxi, 'qoldi': x.qolgan_narxi,
                                  'tashxis_soni': 1,})
                return Response({'data': ser.data,
                                 'all_statistic': c,
                                 'statistic': d,
                                 'tashxislar yil oy hafta kun ko\'rinishida':statistics})
            return Response({'data': ser.data,
                                 'all_statistic': None,
                                 'statistic': None})
      
        
class St(APIView):
    def get(self,request):
        data = Tashxis.objects.annotate(
        year=ExtractYear('sana'),
        month=ExtractMonth('sana'),
        week=ExtractWeekDay('sana'),
        day=ExtractDay('sana'),
        hour=ExtractHour('created'),
        minut=ExtractMinute('created'),
    ).values('year', 'month', 'week', 'day', 'hour','minut','bemor__ism','bemor_id', 'tashxis','licheniya').annotate(
        tashxis_count=Count('tashxis'),
        licheniya_count=Count('licheniya'),
        total_tolangan_narxi=Sum('tolagan_narxi'),
        total_qolgan_narxi=Sum('qolgan_narxi')
    )

        result = []
        for item in data:
            result.append({
            'year': item['year'],
            'month': item['month'],
            'week': item['week'],
            'day': item['day'],
            'hour':item['hour'],
            'minut':item['minut'],
            'bemor_ism': item['bemor__ism'],
            'bemor_id':item['bemor_id'],
            'tashxis': item['tashxis'],
            'tashxis_count': item['tashxis_count'],
            'licheniya':item['licheniya'],
            'licheniya_count':item['licheniya_count'],
            'total_tolangan_narxi': item['total_tolangan_narxi'],
            'total_qolgan_narxi': item['total_qolgan_narxi']
        })

        return Response(result)

        


@api_view(['GET'])
def statistika(request):
    data = Tashxis.objects.annotate(
        year=ExtractYear('sana'),
        month=ExtractMonth('sana'),
        week=ExtractWeekDay('sana'),
        day=ExtractDay('sana')
    ).values('year', 'month', 'week', 'day', 'bemor__ism', 'tashxis').annotate(
        tashxis_count=Count('tashxis'),
        total_tolangan_narxi=Sum('tolagan_narxi'),
        total_qolgan_narxi=Sum('qolgan_narxi')
    )

    result = []
    for item in data:
        result.append({
            'year': item['year'],
            'month': item['month'],
            'week': item['week'],
            'day': item['day'],
            'bemor_ism': item['bemor__ism'],
            'tashxis': item['tashxis'],
            'tashxis_count': item['tashxis_count'],
            'total_tolangan_narxi': item['total_tolangan_narxi'],
            'total_qolgan_narxi': item['total_qolgan_narxi']
        })

    return Response(result)


    return Response(result)    
class TashxisStats(APIView):
    def get(self, request, format=None):
        year = request.query_params.get('year', None)
        month = request.query_params.get('month', None)
        week = request.query_params.get('week', None)
        day = request.query_params.get('day', None)

        tashxislar = Tashxis.objects.all()
        tashxislar_soni = len(tashxislar)

        if year:
            tashxislar = tashxislar.filter(sana__year=year)
        if month:
            tashxislar = tashxislar.filter(sana__month=month)
        if week:
            tashxislar = tashxislar.annotate(week=ExtractWeek('sana')).filter(week=week)
        if day:
            tashxislar = tashxislar.filter(sana=day)

        tashxis_soni = tashxislar.count()
        talab_narxi = tashxislar.aggregate(Sum('tolagan_narxi'))['tolagan_narxi__sum']
        qolgan_narxi = tashxislar.aggregate(Sum('qolgan_narxi'))['qolgan_narxi__sum']
        tashxislar_list = list(tashxislar.values('tashxis', 'licheniya'))
        tashxis_ismi = set([t.tashxis for t in tashxislar])
        licheniya_ismi = set([t.licheniya for t in tashxislar])
        bemor_ismi = set([t.bemor.ism for t in tashxislar])

        response_data = {
            'tashxis_soni': tashxis_soni,
            'talab_narxi': talab_narxi,
            'qolgan_narxi': qolgan_narxi,
            'tashxislar': tashxislar_list,
        }

        return Response(response_data)
    

class Statistikaa(APIView):
    def get(self, request):
        tashxislar = Tashxis.objects.all()
        bemorlar_soni = len(set([t.bemor for t in tashxislar]))
        tashxislar_soni = len(tashxislar)
        
        tolagan_narxi_jami = sum([t.tolagan_narxi for t in tashxislar])
        qolgan_narxi_jami = sum([t.qolgan_narxi for t in tashxislar])
        tashxis_ismi = set([t.tashxis for t in tashxislar])
        licheniya_ismi = set([t.licheniya for t in tashxislar])
        bemor_ismi = set([t.bemor.ism for t in tashxislar])

        return Response({
            'bemorlar_soni': bemorlar_soni,
            'tashxislar_soni': tashxislar_soni,
            'jami_tolagan_narxi': tolagan_narxi_jami,
            'jami_qolgan_narxi ': qolgan_narxi_jami,
            'qo\'yilgan_tashxislar': list(tashxis_ismi),
            'berilgan_licheniyalar': list(licheniya_ismi),
            'bemorlarning_ismi': list(bemor_ismi),
        })

       
# class Statistika(APIView):
    # def get(self, request, pk):
    #     bemor = Bemor.objects.get(pk=pk)
    #     tashxis_list = Tashxis.objects.filter(bemor=bemor)
    
    #     tashxis_by_year = tashxis_list.annotate(year=ExtractYear('created')).values('year').annotate(
    #     count=Count('id'),
    #     tashxis=Count('tashxis', distinct=True),
    #     licheniya=Count('licheniya', distinct=True),
    #     # t_name=Count('tashxis__nomi', distinct=True),
    #     # l_name=Count('licheniya__nomi', distinct=True)
    # )
    #     tashxis_by_month = tashxis_list.annotate(month=ExtractMonth('created')).values('month').annotate(
    #     count=Count('id'),
    #     tashxis=Count('tashxis', distinct=True),
    #     licheniya=Count('licheniya', distinct=True),
    #     # t_name=Count('tashxis__nomi', distinct=True),
    #     # l_name=Count('licheniya__nomi', distinct=True)
    # )
    #     tashxis_by_week = tashxis_list.annotate(week=ExtractWeek('created')).values('week').annotate(
    #     count=Count('id'),
    #     tashxis=Count('tashxis', distinct=True),
    #     licheniya=Count('licheniya', distinct=True),
    #     # t_name=Count('tashxis__nomi', distinct=True),
    #     # l_name=Count('licheniya__nomi', distinct=True)
    # )
    #     tashxis_by_day = tashxis_list.annotate(day=ExtractDay('created')).values('day').annotate(
    #     count=Count('id'),
    #     tashxis=Count('tashxis', distinct=True),
    #     licheniya=Count('licheniya', distinct=True),
    # #     t_name=Count('tashxis__nomi', distinct=True),
    # #     l_name=Count('licheniya__nomi', distinct=True)
    # )
    

    #     statistics = {
    #     'bemor': f'{bemor.ism} {bemor.familiya}',
    #     'address': bemor.address,
    #     'tashxis_by_year': list(tashxis_by_year),
    #     'tashxis_by_month': list(tashxis_by_month),
    #     'tashxis_by_week': list(tashxis_by_week),
    #     'tashxis_by_day': list(tashxis_by_day)
    # }
    
    #     return Response(statistics)
     


# class BemorCreateAPIView(APIView):
#     def post(self, request):
#         serializer = BemorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def get(self,request):
#         bemor=Bemor.objects.all()
#         serializers=BemorSerializer(bemor,many=True)
#         return Response(serializers.data)

# class TashxisCreateAPIView(APIView):
#     def post(self, request):
#         # JSON formatidagi so'rovdan bemor ma'lumotlarini olish
#         ism = request.data.get('ism')
#         familiya = request.data.get('familiya')
#         otasining_ismi = request.data.get('otasining_ismi')
        
#         # Bemor obyektini yaratish
#         bemor = Bemor.objects.create(ism=ism, familiya=familiya, otasining_ismi=otasining_ismi)
        
#         # Tashxis ma'lumotlarini olish
#         jami_narxi = request.data.get('jami_narxi')
#         tolagan_narxi=request.data.get('tolagan_narxi')
#         qoldi=request.data.get('qoldi')
#         tashxis=request.data.get('tashxis')
#         licheniya=request.data.get('licheniya')
        
#         # Tashxis obyektini bemor bilan bog'lash
#         tashxis = Tashxis.objects.create(bemor=bemor, jami_narxi=jami_narxi,tolagan_narxi=tolagan_narxi,tashxis=tashxis,licheniya=licheniya)
        
#         # Yangi bemor va tashxis ma'lumotlarini JSON formatida qaytarish
#         return Response({
#             'bemor': {
#                 'id': bemor.id,
#                 'ism': bemor.ism,
#                 'familiya': bemor.familiya,
#                 'otasining_ismi': bemor.otasining_ismi,
#             },
#             'tashxis': {
#                 'id': tashxis.id,
#                 'tolangan_summa': tashxis.jami_narxi,
#                  'tolangan_summa':tashxis.tolagan_narxi,
#                  'qoldi':tashxis.qoldi,
#                  'tashxis':tashxis.tashxis,
#                  'licheniya':tashxis.licheniya,


#                 'bemor_id': tashxis.bemor,
#             }
#         }, status=status.HTTP_201_CREATED)


#     def get(self,request):
#         tashxis=Tashxis.objects.all()
#         serializers=TashxisSerializer(tashxis,many=True)
#         return Response(serializers.data)

# class BemorDetailAPIView(APIView):
#     def get(self, request, pk):
#         bemor = Bemor.objects.get(pk=pk)
#         serializer = BemorSerializer(bemor)
#         return Response(serializer.data)

# class TashxisDetailAPIView(APIView):
#     def get(self, request, pk):
#         try:
#             tashxis = Tashxis.objects.get(pk=pk)
#             serializer = TashxisSerializer(tashxis)
            
#             return Response({"data":serializer.data
#                              })
#         except:
#             return Response({'message': "bu id xato"})

# class TashxisSoniView(APIView):
#     def get(self, request, bemor_id):
#         # Oxirgi 1 yilda, 1 oyda, 1 haftada va 1 kunda nechta tashxis qo'yilganini hisoblovchi funksiya
#         hozir = timezone.now()
#         yillik = hozir - timezone.timedelta(days=365)
#         oylik = hozir - timezone.timedelta(days=30)
#         haftalik = hozir - timezone.timedelta(days=7)
#         kunlik = hozir - timezone.timedelta(days=1)
        
#         yillik_tashxislar = Tashxis.objects.filter(bemor=bemor_id, vaqt__gte=yillik).count()
#         oylik_tashxislar = Tashxis.objects.filter(bemor=bemor_id, vaqt__gte=oylik).count()
#         haftalik_tashxislar = Tashxis.objects.filter(bemor=bemor_id, vaqt__gte=haftalik).count()
#         kunlik_tashxislar = Tashxis.objects.filter(bemor=bemor_id, vaqt__gte=kunlik).count()
        
#         return Response({
#             'yillik_tashxislar': yillik_tashxislar,
#             'oylik_tashxislar': oylik_tashxislar,
#             'haftalik_tashxislar': haftalik_tashxislar,
#             'kunlik_tashxislar': kunlik_tashxislar,
#         }, status=status.HTTP_200_OK)

    
# class TashxisStatisticsAPIView(APIView):
#     def get(self, request):
#         bemorlar = Tashxis.objects.values('bemor').distinct()
#         statistics = []
#         for bemor in bemorlar:
#             bemor_id = bemor['bemor']
#             bemor_tashxis = Tashxis.objects.filter(bemor=bemor_id)
#             jami_narxi = bemor_tashxis.aggregate(Sum('jami_narxi'))['jami_narxi__sum']
#             tolagan_narxi = bemor_tashxis.aggregate(Sum('tolagan_narxi'))['tolagan_narxi__sum']
#             qolgan_narxi = bemor_tashxis.aggregate(Sum('qoldi'))['qoldi__sum']

#             data = {
#                 'bemor': bemor_id,
#                 'jami_narxi': jami_narxi,
#                 'tolagan_narxi': tolagan_narxi,
#                 'qoldi': qolgan_narxi,
                
#             }
#             statistics.append(data)

#         return Response(statistics)
    

# class TashxisDetail(APIView):
#     def get(self, request, pk):
#         try:
#             bemor = Bemor.objects.get(id=id)
#             ser = BemorSerializer(bemor)
#             if Tashxis.objects.filter(bemor=bemor):
#                 tashxis = Tashxis.objects.filter(bemor=bemor)
#                 c = {}
#                 sum_narx = tashxis.aggregate(Sum('jami_narx'))
#                 sum_tuladi = tashxis.aggregate(Sum('tolagan_narxi'))
#                 sum_qoldi = tashxis.aggregate(Sum('qoldi'))
#                 sum_tash = Tashxis.objects.filter(bemor=bemor).count()
#                 c['sum_narx'] = sum_narx['narx__sum']
#                 c['sum_tuladi'] = sum_tuladi['tuladi__sum']
#                 c['sum_qoldi'] = sum_qoldi['qoldi__sum']
#                 c['tashxislar'] = sum_tash
#                 d = []
#                 for x in tashxis:
#                     found = False
#                     for item in d:
#                         if item['tashxislar'] == x.licheniya:
#                             item['narx'] += x.jami_narxi
#                             item['tuladi'] += x.tolagan_narxi
#                             item['qoldi'] += x.qoldi
#                             item['tashxis'] += 1
#                             found = True
#                             break
#                 if not found:
#                     d.append({'tashxislar': x.licheniya, 'narx': x.jami_narxi,
#                                   'tuladi': x.tolagan_narxi, 'qoldi': x.qoldi,
#                                   'tashxis_soni': 1,})
#                 return Response({'data': ser.data,
#                                  'all_statistic': c,
#                                  'statistic': d})
#             return Response({'data': ser.data,
#                                  'all_statistic': None,
#                                  'statistic': None})
#         except:
#             return Response({'message': 'Not found'})
        

       
