from django.db import models
from user.models import *


class Bemor(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='uchirilgan user', related_name='bemor_user')
    first_name = models.CharField(max_length=60, null=True, blank=True)
    last_name = models.CharField(max_length=60, null=True, blank=True)
    dad_name = models.CharField(max_length=60, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}/{self.last_name}'
    
class Tashxis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bemor = models.ForeignKey(Bemor, on_delete=models.CASCADE)
    tashxis = models.TextField(null=True, blank=True)
    lecheniya = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    narx = models.PositiveIntegerField(default=0)
    tuladi = models.PositiveIntegerField(default=0)
    qoldi = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.bemor}{self.narx}'
# Create your models here.
