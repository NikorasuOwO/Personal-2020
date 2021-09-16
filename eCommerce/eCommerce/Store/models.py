from django.db import models

# Create your models here.

class Product(models.Model):

    image = models.ImageField()
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.FloatField(default=0)

    color1 = models.CharField(max_length=20, default='black')
    color2 = models.CharField(max_length=20, default='black')
    use = models.CharField(max_length=30, default='running')
    type = models.CharField(max_length=30, default='sneakers')

    def __str__(self):
        return self.name