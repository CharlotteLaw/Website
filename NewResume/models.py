from django.db import models


class Product(models.Model):  #inherit from models class
    name = models.CharField(max_length=255) #an instance of CharField, field that takes chars
    price = models.FloatField() #a field that can include floats
    stock = models.IntegerField()
    image_url = models.CharField(max_length = 2083)  #standard max lenght for URLs

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()




#create model
#create new migration
#run new migration
#python3 manage.py migrate
