from django.db import models
from user.models import *
from django.utils import timezone



class Bemor(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.ism

class Tashxis(models.Model):
    bemor = models.ForeignKey(Bemor, on_delete=models.CASCADE,related_name='bemor')
    tashxis = models.CharField(max_length=100)
    licheniya = models.CharField(max_length=100)
    jami_narxi=models.DecimalField(max_digits=10,decimal_places=2)
    tolagan_narxi = models.DecimalField(max_digits=10, decimal_places=2)
    qolgan_narxi = models.DecimalField(max_digits=10, decimal_places=2)
    sana = models.DateField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.bemor}"






# class Bemor(models.Model):
#     ism = models.CharField(max_length=50,blank=True,null=True)
#     familiya = models.CharField(max_length=50,blank=True,null=True)
#     otasining_ismi = models.CharField(max_length=50,blank=True,null=True)
#     phone = models.CharField(max_length=15,blank=True,null=True)
#     address = models.CharField(max_length=100,blank=True,null=True)
#     date_created = models.DateField(default=timezone.now())
#     yosh = models.IntegerField()

#     def __str__(self):
#         return f'{self.ism}/{self.familiya}'
    
# class Tashxis(models.Model):
#     bemor = models.ForeignKey(Bemor, on_delete=models.CASCADE,related_name='bemori')
#     tashxis=models.TextField()
#     licheniya = models.CharField(max_length=50,blank=True,null=True)
#     jami_narxi = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
#     tolagan_narxi = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
#     qoldi = models.PositiveIntegerField(default=0)
#     vaqt=models.DateTimeField(default=timezone.now())

#     def __str__(self):
#         return f'{self.bemor} | {self.jami_narxi}'
    
#     def tashxis_soni(bemor_id):
#     # Oxirgi 1 yilda 1 oyda 1 haftada 1 kunda nechta tashxis qo'yilganini hisoblovchi funksiya
#         hozir = timezone.now()
#         yillik = hozir - timezone.timedelta(days=365)
#         oylik = hozir - timezone.timedelta(days=30)
#         haftalik = hozir - timezone.timedelta(days=7)
#         kunlik = hozir - timezone.timedelta(days=1)
    
#         yillik_tashxislar = Tashxis.objects.filter(bemor=bemor_id, vaqt__gte=yillik).count()
#         oylik_tashxislar = Tashxis.objects.filter(bemor=bemor_id, vaqt__gte=oylik).count()
#         haftalik_tashxislar = Tashxis.objects.filter(bemor=bemor_id, vaqt__gte=haftalik).count()
#         kunlik_tashxislar = Tashxis.objects.filter(bemor=bemor_id, vaqt__gte=kunlik).count()
    
#         return {
#         'yillik_tashxislar': yillik_tashxislar,
#         'oylik_tashxislar': oylik_tashxislar,
#         'haftalik_tashxislar': haftalik_tashxislar,
#         'kunlik_tashxislar': kunlik_tashxislar,
#     }
# # Create your models here.
