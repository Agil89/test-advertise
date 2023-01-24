from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

# class Admin(models.Model):
#     user = models.OneToOneField(
#         User, verbose_name=_("user"), related_name="admin", on_delete=models.CASCADE
#     )



class Autor(models.Model):
    balance = models.PositiveIntegerField(default=0)
    is_admin = models.BooleanField(default=False)
    user = models.OneToOneField(
        User, verbose_name=_("user"), related_name="autor", on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.user}'

class Advertise(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255,null=True, blank=True)
    status = models.CharField(max_length=64,null=True, blank=True)
    is_checked = models.BooleanField(default=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='advertises')

    def __str__(self):
        return f'{self.title}'

class PayAmount(models.Model):
    sum = models.PositiveIntegerField()