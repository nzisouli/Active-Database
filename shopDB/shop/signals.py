from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from shop import models

@receiver(pre_save, sender=models.Person)
def people_handler(sender, instance, **kwargs):
    '''
    Trigger for insert person.
    '''
    
    num = models.Person.objects.filter(name=instance.name).count()
    if num == 0 :
        instance.moneyLeft = instance.moneyPerMonth

@receiver(post_save, sender=models.Buying)
def shop_handler(sender, instance, **kwargs):
    '''
    Trigger for update buying: Reduce moneyLeft from person and productsLeft 
    from products.
    '''
    
    buying_person = models.Person.objects.filter(name=instance.person.name)[0]
    buying_object = models.Product.objects.filter(name=instance.product.name)[0]

    buying_person.moneyLeft -= buying_object.price
    buying_person.save()

    buying_object.productsLeft -= 1
    buying_object.save()

@receiver(pre_save, sender=models.Product)
def delivery_handler(sender, instance, **kwargs):
    '''
    Trigger for update product: Make shop delivery True if productsLeft = 0.
    '''
    
    if instance.productsLeft == 0:
        instance.shop.delivery = True
        instance.shop.save()