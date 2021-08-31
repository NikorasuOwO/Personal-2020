from django.db import models

from .codes import country_codes 
# Create your models here.

class Code(models.Model):

    name = models.CharField(default='', max_length=100)
    code = models.CharField(default='', max_length=4)
    def __str__(self):
        return self.name + ":" + self.code

    def update_database():

        all = country_codes()

        for country_name, country_code in all:

            Code.objects.create(name=country_name, code=country_code).save()