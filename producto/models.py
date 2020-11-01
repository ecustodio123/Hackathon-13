from django.db import models

CATEGORIAS_CHOICES = (
    ("Abarrotes", "Abarrotes"),
    ("Frutas", "Frutas"),
    ("Verduras", "Verduras"),
)

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20, blank=False, null=False)
    nombre_producto = models.CharField(max_length=200, blank=False, null=False)
    precio = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    cantidad = models.IntegerField(blank=False,null=False)
    categoria = models.CharField(max_length=200, blank=False, null=False, choices=CATEGORIAS_CHOICES, default='Abarrotes',)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre_producto']

    def __str__(self):
        return self.nombre_producto
    
class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField('Nombre', max_length=200, blank=False, null=False)
    pago = models.DecimalField('Pago', max_digits=10,decimal_places=2,blank=False,null=False)
    date_venta = models.DateField('Fecha de Venta', blank=False, null=False)
    producto_id = models.ManyToManyField(Product)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['cliente']
    
    def __str__(self):
        return self.cliente

    def get_ventas(self):
        return ','.join([str(p) for p in self.producto_id.all()])
