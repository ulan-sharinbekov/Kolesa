from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class City(models.Model):
    title = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Brand(models.Model):
    title = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

class Models(models.Model):
    Automatic = 'Automatic'
    Mechanics = 'Mechanics'
    Robots = 'Robots'
    Trans_CHOICES = [
        (Automatic, 'Automatic'),
        (Mechanics, 'Mechanics'),
        (Robots, 'Robots'),
    ]

    Left = 'Left'
    Right = 'Right'
    steering_CHOICES = [
        (Left, 'Left'),
        (Right, 'Right'),
    ]

    Rear = 'Rear'
    Front = 'Front'
    Drive_CHOICES = [
        (Rear, 'Rear'),
        (Front, 'Front'),
    ]

    title = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    transmission = models.CharField(max_length=200, choices=Trans_CHOICES)
    steering = models.CharField(max_length=200, choices=steering_CHOICES)
    color = models.CharField(max_length=200)
    drive_unit = models.CharField(max_length=200, choices=Drive_CHOICES)
    cleared_RK = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    contacts = models.IntegerField()
    year = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
    car = models.ForeignKey(Models, on_delete=models.CASCADE)
    parent = models.ForeignKey("Comment", on_delete= models.CASCADE, null=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарий"