from django.db import models

# Create tables with their attributes.

class Person (models.Model):
    name = models.CharField(max_length=200, primary_key = True)
    moneyPerMonth = models.FloatField()
    moneyLeft = models.FloatField(null=True)

class Product (models.Model):
    name = models.CharField(max_length=200, primary_key = True)
    price = models.FloatField()
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE)
    productsLeft = models.IntegerField()

class Shop (models.Model):
    shop_name = models.CharField(max_length=200, primary_key = True)
    delivery = models.BooleanField()

class Buying (models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    buying_id = models.AutoField(primary_key=True)