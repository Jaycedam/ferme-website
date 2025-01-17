# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Delivery(models.Model):
    id_delivery = models.FloatField(primary_key=True)
    nro_orden = models.ForeignKey("Orden", models.DO_NOTHING, db_column="nro_orden")
    calle = models.CharField(max_length=200)
    nro = models.FloatField()
    nro_departamento = models.FloatField(blank=True, null=True)

    def __str__(self):
        if self.nro_departamento is not None:
            return (
                self.calle
                + ", N°"
                + str(self.nro)
                + " "
                + " departamento"
                + str(self.nro_departamento)
            )
        if self.nro_departamento is None:
            return self.calle + ", N°" + str(self.nro)

    class Meta:
        managed = False
        db_table = "delivery"


class Domicilio(models.Model):
    id_domicilio = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=200)
    nro = models.FloatField()
    nro_departamento = models.FloatField(blank=True, null=True)
    rut_persona = models.OneToOneField(
        "Persona", models.DO_NOTHING, db_column="rut_persona"
    )

    def __str__(self):
        if self.nro_departamento is not None:
            return (
                self.calle
                + ", N°"
                + str(self.nro)
                + " "
                + " departamento"
                + str(self.nro_departamento)
            )
        if self.nro_departamento is None:
            return self.calle + ", N°" + str(self.nro)

    class Meta:
        managed = False
        db_table = "domicilio"


class Estado(models.Model):
    id_estado = models.FloatField(primary_key=True)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.estado

    class Meta:
        managed = False
        db_table = "estado"


class FamiliaProducto(models.Model):
    id_familia_producto = models.AutoField(primary_key=True)
    familia_producto = models.CharField(max_length=200)
    imagen_url = models.ImageField(blank=True, null=True, upload_to="product-family/")

    def __str__(self):
        return self.familia_producto

    class Meta:
        managed = False
        db_table = "familia_producto"


class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=200)

    def __str__(self):
        return self.marca.capitalize()

    class Meta:
        managed = False
        db_table = "marca"


class Motivo(models.Model):
    id_motivo = models.FloatField(primary_key=True)
    motivo = models.CharField(max_length=200)

    def __str__(self):
        return self.motivo

    class Meta:
        managed = False
        db_table = "motivo"


class NcDetalle(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(
        "Producto", models.DO_NOTHING, db_column="id_producto"
    )
    precio = models.FloatField()
    cantidad = models.FloatField()
    total = models.FloatField()
    nro_nota_credito = models.ForeignKey(
        "NotaCredito", models.DO_NOTHING, db_column="nro_nota_credito"
    )

    class Meta:
        managed = False
        db_table = "nc_detalle"

    def __str__(self):
        return (
            "Solicitud "
            + str(self.nro_nota_credito)
            + ", producto "
            + str(self.id_producto.get_name())
            + " (x"
            + str(self.cantidad)
            + "), total $"
            + str(self.total)
            + ". "
            + str(self.nro_nota_credito.get_status())
        )

    def get_id_product(self):
        return self.id_producto


class NotaCredito(models.Model):
    nro_nota_credito = models.AutoField(primary_key=True)
    fecha = models.DateField()
    total = models.FloatField()
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column="id_estado")
    id_motivo = models.ForeignKey(Motivo, models.DO_NOTHING, db_column="id_motivo")
    nro_orden = models.ForeignKey("Orden", models.DO_NOTHING, db_column="nro_orden")

    def __str__(self):
        return str(self.nro_nota_credito)

    def get_status(self):
        return self.id_estado

    class Meta:
        ordering = ["-fecha", "-nro_nota_credito"]
        managed = False
        db_table = "nota_credito"


class Orden(models.Model):
    nro_orden = models.AutoField(primary_key=True)
    fecha = models.DateField()
    total = models.FloatField()
    rut_persona = models.ForeignKey(
        "Persona", models.DO_NOTHING, db_column="rut_persona"
    )
    id_tipo = models.ForeignKey("TipoOrden", models.DO_NOTHING, db_column="id_tipo")
    id_proveedor = models.ForeignKey(
        "Proveedor", models.DO_NOTHING, db_column="id_proveedor", blank=True, null=True
    )
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column="id_estado")

    def __str__(self):
        return str(self.nro_orden)

    def get_id(self):
        return self.nro_orden

    class Meta:
        managed = False
        db_table = "orden"
        verbose_name_plural = "Ordenes"
        ordering = ["-fecha", "-nro_orden"]


class OrdenDetalle(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(
        "Producto", models.DO_NOTHING, db_column="id_producto"
    )
    precio = models.FloatField()
    cantidad = models.FloatField()
    total = models.FloatField()
    nro_orden = models.ForeignKey(Orden, models.DO_NOTHING, db_column="nro_orden")

    class Meta:
        managed = False
        db_table = "orden_detalle"


class Persona(models.Model):
    rut_persona = models.CharField(primary_key=True, max_length=10)
    celular = models.FloatField()
    usuario = models.OneToOneField(User, on_delete=models.PROTECT, db_column="usuario")

    def __str__(self):
        return self.rut_persona

    class Meta:
        managed = False
        db_table = "persona"


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    precio = models.FloatField()
    precio_proveedor = models.FloatField()
    stock = models.FloatField()
    stock_critico = models.FloatField()
    imagen_url = models.ImageField(blank=True, null=True, upload_to="products/")
    fecha_vencimiento = models.DateField(blank=True, null=True)
    id_tipo_producto = models.ForeignKey(
        "TipoProducto", models.DO_NOTHING, db_column="id_tipo_producto"
    )
    id_proveedor = models.ForeignKey(
        "Proveedor", models.DO_NOTHING, db_column="id_proveedor"
    )
    id_marca = models.ForeignKey(Marca, models.DO_NOTHING, db_column="id_marca")

    def __str__(self):
        return str(self.id_producto)

    class Meta:
        managed = False
        db_table = "producto"

    def get_name(self):
        return self.producto


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=200)
    id_rubro = models.ForeignKey("Rubro", models.DO_NOTHING, db_column="id_rubro")
    rut_persona = models.OneToOneField(
        Persona, models.DO_NOTHING, db_column="rut_persona"
    )

    def __str__(self):
        return self.nombre_empresa

    class Meta:
        managed = False
        db_table = "proveedor"


class Recibo(models.Model):
    nro_recibo = models.AutoField(primary_key=True)
    fecha = models.DateField()
    subtotal = models.FloatField()
    iva = models.FloatField()
    total = models.FloatField()
    id_tipo = models.ForeignKey("TipoDocumento", models.DO_NOTHING, db_column="id_tipo")
    nro_orden = models.OneToOneField(Orden, models.DO_NOTHING, db_column="nro_orden")

    def __str__(self):
        return str(self.nro_recibo)

    class Meta:
        managed = False
        db_table = "recibo"


class Rubro(models.Model):
    id_rubro = models.AutoField(primary_key=True)
    rubro = models.CharField(max_length=200)

    def __str__(self):
        return self.rubro

    class Meta:
        managed = False
        db_table = "rubro"


class TipoDocumento(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_documento

    class Meta:
        managed = False
        db_table = "tipo_documento"


class TipoOrden(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo

    class Meta:
        managed = False
        db_table = "tipo_orden"


class TipoProducto(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)
    tipo_producto = models.CharField(max_length=200)
    id_familia_producto = models.ForeignKey(
        FamiliaProducto, models.DO_NOTHING, db_column="id_familia_producto"
    )

    def __str__(self):
        return self.tipo_producto.capitalize()

    class Meta:
        managed = False
        db_table = "tipo_producto"
