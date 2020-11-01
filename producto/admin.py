from django.contrib import admin
from .models import Product, Venta

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'precio', 'cantidad', 'categoria')
    list_filter = ['categoria']

class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'pago', 'date_venta', 'get_ventas')
    search_fields = ['cliente']
    list_filter = ['date_venta']

# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(Venta, VentaAdmin)