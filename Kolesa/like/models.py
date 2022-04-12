from django.db import models
from api.models import  Models
from django.contrib.auth.models import User
# Create your models here.

class Like(models.Model):
    car = models.ForeignKey(Models, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"