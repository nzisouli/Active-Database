from django.contrib import admin
from .models import Person, Shop, Buying, Product

#Define fields seen by Admin

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = ["name", "moneyPerMonth", "moneyLeft"]
    search_fields = ["name"]
    readonly_fields = ["moneyLeft"]

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    fields = ["shop_name", "delivery"]
    search_fields = ["shop_name"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ["name", "price", "shop", "productsLeft"]
    search_fields = ["name", "shop"]

@admin.register(Buying)
class BuyingAdmin(admin.ModelAdmin):
    fields = ["person", "product"]
    search_fields = ["buying_id", "person", "product"]
