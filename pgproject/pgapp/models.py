from django.db import models

# Create your models here.

class Details(models.Model):
    title = models.CharField(max_length=15)
    price = models.IntegerField()
    location_shoot = models.IntegerField()
    print_credit = models.IntegerField()
    digital_files = models.IntegerField()

    def __str__(self):
        return self.title
class Orders(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    city = models.CharField(max_length=15)
    event = models.CharField(max_length=15)
    status = models.BooleanField(default='False')

    def __str__(self):
        return self.name

