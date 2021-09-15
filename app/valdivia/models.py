from django.db import models
from datetime import datetime
# Create your models here.
class TiposDeEmpleados(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre del tipo de Empleado')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name= 'TipoDeEmpleado'
        verbose_name_plural= 'TiposDeEmpleados'
        db_table= 'TipoDeEmpleado'
        ordering = ['id'] #ascendente, con rayita descendente

class Categorias(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre de categoria')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name= 'Categoria'
        verbose_name_plural= 'Categorias'
        db_table= 'Categoria'
        ordering = ['id'] #ascendente, con rayita descendente


class Empleados(models.Model):
    categoria = models.ManyToManyField(Categorias)
    tipo = models.ForeignKey(TiposDeEmpleados, on_delete=models.CASCADE, null=True)
    nombres = models.CharField(max_length=150, verbose_name='Nombres')
    apellidos = models.CharField(max_length=150, verbose_name='Apellidos')
    rut = models.CharField(max_length=15, unique=True, verbose_name='Rut')
    fecha_actual = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    fecha_creacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de creacion')
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualizacion')
    edad = models.PositiveIntegerField(default=0)
    altura = models.DecimalField(default=0.0, max_digits=9, decimal_places=1)
    peso = models.DecimalField(default=0.0, max_digits=9, decimal_places=1)
    remuneracion = models.DecimalField(default=0.0, max_digits=20, decimal_places=1)
    estado = models.BooleanField(default=True)
    sexo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='empleados_fotos/%Y/%m/%d', null=True, blank=True)
    cv = models.ImageField(upload_to='empleados_cv/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.nombres

    class Meta:
        verbose_name= 'Empleado'
        verbose_name_plural= 'Empleados'
        db_table= 'Empleado'
        ordering = ['-id'] #descendente, sin rayita ascendente
