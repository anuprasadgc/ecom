from django.contrib import admin
from .models import Order, Products
# Register your models here.
admin.site.site_header = "E-commerce Site"
admin.site.site_title = "Outfit-Hub"
admin.site.index_title = "Manage Outfit-Hub"


class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")

    
    list_display = ('title','discription','original_price','discound_price','category')
    search_fields = ('title','original_price','discound_price','category')
    change_category_to_default.short_description ="Default Category"
    actions = ('change_category_to_default',)
    list_editable = ('original_price','discound_price','category')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('items','name','email','address','city','state','zipcode','total')
    search_fields = ('name',)


admin.site.register(Products,ProductAdmin)
admin.site.register(Order,OrderAdmin)