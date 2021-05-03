# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    comuna = models.CharField(max_length=200)
    id_provincia = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='id_provincia')

    def __str__(self):
            return self.comuna

    class Meta:
        managed = False
        db_table = 'comuna'


class Domicilio(models.Model):
    id_domicilio = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=200)
    nro = models.FloatField()
    nro_departamento = models.FloatField(blank=True, null=True)
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    id_tipo_domicilio = models.ForeignKey('TipoDomicilio', models.DO_NOTHING, db_column='id_tipo_domicilio')
    rut_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='rut_persona')

    class Meta:
        managed = False
        db_table = 'domicilio'


class FamiliaProducto(models.Model):
    id_familia_producto = models.AutoField(primary_key=True)
    familia_producto = models.CharField(max_length=200)
    imagen_url = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.familia_producto

    class Meta:
        managed = False
        db_table = 'familia_producto'

class Marca(models.Model):
    id_marca = models.FloatField(primary_key=True)
    marca = models.CharField(max_length=200)

    def __str__(self):
        return self.marca

    class Meta:
        managed = False
        db_table = 'marca'


class NotaCredito(models.Model):
    nro_nota_credito = models.FloatField(primary_key=True)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    nro_doc = models.ForeignKey('Recibo', models.DO_NOTHING, db_column='nro_doc')
    rut_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='rut_persona')

    def __str__(self):
        return self.nro_nota_credito

    class Meta:
        managed = False
        db_table = 'nota_credito'


class NotaCreditoDetalle(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    cantidad = models.FloatField()
    nro_nota_credito = models.ForeignKey(NotaCredito, models.DO_NOTHING, db_column='nro_nota_credito')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')

    class Meta:
        managed = False
        db_table = 'nota_credito_detalle'


class OcDetalle(models.Model):
    id_oc_detalle = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.FloatField()
    total = models.FloatField()
    id_orden_compra = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='id_orden_compra')

    class Meta:
        managed = False
        db_table = 'oc_detalle'


class OrdenCompra(models.Model):
    id_orden_compra = models.AutoField(primary_key=True)
    total = models.FloatField()
    estado = models.CharField(max_length=50)
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')

    def __str__(self):
        return self.id_orden_compra

    class Meta:
        managed = False
        db_table = 'orden_compra'


class Persona(models.Model):
    rut_persona = models.CharField(primary_key=True, max_length=10)
    celular = models.FloatField()
    usuario = models.OneToOneField(User, on_delete=models.PROTECT, db_column='usuario')
    
    def __str__(self):
        return self.rut_persona

    class Meta:
        managed = False
        db_table = 'persona'


class Producto(models.Model):
    id_producto = models.FloatField(primary_key=True)
    producto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    precio = models.FloatField()
    precio_proveedor = models.FloatField()
    stock = models.FloatField()
    stock_critico = models.FloatField()
    imagen_url = models.CharField(max_length=500, blank=True, null=True)
    id_tipo_producto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='id_tipo_producto')
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')
    id_marca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='id_marca')

    def __str__(self):
        return self.producto

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    id_proveedor = models.FloatField(primary_key=True)
    nombre_empresa = models.CharField(max_length=200)
    id_rubro = models.ForeignKey('Rubro', models.DO_NOTHING, db_column='id_rubro')
    rut_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='rut_persona')

    def __str__(self):
        return self.nombre_empresa

    class Meta:
        managed = False
        db_table = 'proveedor'


class Provincia(models.Model):
    id_provincia = models.FloatField(primary_key=True)
    provincia = models.CharField(max_length=200)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')

    def __str__(self):
        return self.provincia

    class Meta:
        managed = False
        db_table = 'provincia'


class Recibo(models.Model):
    nro_doc = models.FloatField(primary_key=True)
    fecha = models.DateField()
    subtotal = models.FloatField()
    iva = models.FloatField()
    total = models.FloatField()
    id_tipo_doc = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='id_tipo_doc')
    rut_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='rut_persona')

    def __str__(self):
        return self.nro_doc

    class Meta:
        managed = False
        db_table = 'recibo'


class ReciboDetalle(models.Model):
    id_detalle = models.FloatField(primary_key=True)
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')
    nro_doc = models.ForeignKey(Recibo, models.DO_NOTHING, db_column='nro_doc')
    cantidad = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'recibo_detalle'


class Region(models.Model):
    id_region = models.FloatField(primary_key=True)
    region = models.CharField(max_length=200)

    def __str__(self):
        return self.region

    class Meta:
        managed = False
        db_table = 'region'


class Rubro(models.Model):
    id_rubro = models.FloatField(primary_key=True)
    rubro = models.CharField(max_length=200)

    def __str__(self):
        return self.rubro

    class Meta:
        managed = False
        db_table = 'rubro'


class TipoDocumento(models.Model):
    id_tipo_doc = models.FloatField(primary_key=True)
    tipo_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_doc

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class TipoDomicilio(models.Model):
    id_tipo_domicilio = models.FloatField(primary_key=True)
    tipo_domicilio = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_domicilio

    class Meta:
        managed = False
        db_table = 'tipo_domicilio'

class TipoProducto(models.Model):
    id_tipo_producto = models.FloatField(primary_key=True)
    tipo_producto = models.CharField(max_length=200)
    id_familia_producto = models.ForeignKey(FamiliaProducto, models.DO_NOTHING, db_column='id_familia_producto')

    def __str__(self):
        return self.tipo_producto

    class Meta:
        managed = False
        db_table = 'tipo_producto'
