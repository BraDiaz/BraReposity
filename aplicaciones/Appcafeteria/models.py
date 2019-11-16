from decimal import Decimal

from django.core.validators import MinValueValidator
from .validators import validate_cedula
from django.db import models

# Create your models here.
class Campus(models.Model):
    id_campus = models.AutoField(primary_key=True)
    descripcion = models.CharField('Nombre del campus',max_length=150, null=False,blank=False)
    estado = models.BooleanField('Estado', default=True)
    fecha_Creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = 'Campus'

    def __str__(self):
        return self.descripcion

class Empleados(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre Empleado', max_length=150, null=False, blank=False)
    cedula = models.CharField('Cedula', max_length=13, null=False, blank=False, validators=[validate_cedula])
    TANDAS =(
        ('Matutino','Matutino'),
        ('Vespertino', 'Vespertino'),
        ('Nocturno','Nocturno'),
    )
    tanda_labor = models.CharField('Tanda',max_length=50, choices = TANDAS)
    porciento_comision = models.PositiveIntegerField('Porciento', null=False, blank=False)
    fecha_ingreso = models.DateField('Fecha Ingreso', null=False, blank=False)
    estado = models.BooleanField('Estado', default=True)
    fecha_Creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.nombre


class Cafeteria(models.Model):
    id_cafeteria = models.AutoField(primary_key=True)
    descripcion = models.CharField('Nombre de Cafeteria', max_length=150, null=False, blank=False)
    id_campus = models.ForeignKey(Campus, on_delete= models.CASCADE)
    encargado = models.OneToOneField(Empleados, on_delete= models.CASCADE)
    estado = models.BooleanField('Estado', default=True)
    fecha_Creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Cafeteria'
        verbose_name_plural = 'Cafeterias'

    def __str__(self):
        return self.descripcion

class tipoUsuario(models.Model):
    id_tipoUsuario = models.AutoField(primary_key=True)
    descripcion = models.CharField('Tipo de Usuario', max_length=150, null=False,blank=False)
    estado = models.BooleanField('Estado', default=True)
    fecha_Creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Tipo de Usuario'
        verbose_name_plural = 'Tipos de Usuario'

    def __str__(self):
        return self.descripcion

class Usuario(models.Model):

    def clean(self):
        if self.cedula == 'hoila':
            raise ZeroDivisionError


    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre Usuario', max_length=150, null=False, blank=False)
    cedula = models.CharField('Cedula', max_length=13, null=False, blank=False,validators=[validate_cedula])
    tipo_usuario = models.ForeignKey(tipoUsuario, on_delete=models.CASCADE)
    limiteCredito = models.PositiveIntegerField(null=False,blank=False)
    estado = models.BooleanField('Estado', default=True)
    fecha_Creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    descripcion = models.CharField('Marca', max_length=150, null=False,blank=False)
    estado = models.BooleanField('Estado', default=True)
    fecha_Creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.descripcion

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_comercial = models.CharField('Nombre Comercial', max_length=150, null=False,blank=False)
    estado = models.BooleanField('Estado', default=True)
    fecha_Creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre_comercial

class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    descripcion = models.CharField('Articulo', max_length=150, null=False, blank=False)
    id_marca = models.ForeignKey(Marca, on_delete= models.CASCADE)
    costo = models.DecimalField('Precio',max_digits=10, decimal_places=2,null=False,blank=False, validators=[MinValueValidator(Decimal('0.01'))])
    id_proveedor = models.ForeignKey(Proveedor, on_delete= models.CASCADE)
    existencia = models.PositiveIntegerField('Existencia', null=False,blank=False)
    estado = models.BooleanField('Estado', default=True)
    fecha_Creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        return self.descripcion

class Factura(models.Model,):

    id_facturacion = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,)
    producto = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=150, null=True, blank= True)
    cantidad = models.PositiveIntegerField('Cantidad', null=False, blank=False)
    total = models.DecimalField('Total',max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    fecha_Creacion = models.DateField('Fecha de venta', auto_now=False, auto_now_add=True)
    estado = models.BooleanField('Estado', default=True)


    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return "{} - {}".format(self.id_usuario,self.fecha_Creacion)



