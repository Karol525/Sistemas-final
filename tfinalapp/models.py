# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Boleta(models.Model):
    id_boleta = models.CharField(primary_key=True, max_length=4)
    id_pdetalle6 = models.ForeignKey('PedidoDetalle', models.DO_NOTHING, db_column='id_pdetalle6')
    fec_boleta = models.DateField()

    class Meta:
        managed = False
        db_table = 'boleta'


class Categorias(models.Model):
    id_categoria = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'categorias'


class Comentarios(models.Model):
    id_coment = models.CharField(primary_key=True, max_length=4)
    comentario = models.TextField()
    id_prod2 = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_prod2')
    id_usuario2 = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario2')

    def __str__(self):
        return self.id_coment

    class Meta:
        managed = False
        db_table = 'comentarios'


class Descuentos(models.Model):
    id_descuento = models.CharField(primary_key=True, max_length=4)
    fec_inicio = models.DateField()
    fec_venc = models.DateField()
    valor = models.IntegerField()

    def __str__(self):
        return self.id_descuento
    
    class Meta:
        managed = False
        db_table = 'descuentos'


class Envios(models.Model):
    id_envios = models.CharField(primary_key=True, max_length=4)
    fec_envio = models.DateField()
    id_boleta7 = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='id_boleta7')
    delivery = models.CharField(max_length=20)

    def __str__(self):
        return self.id_boleta7

    class Meta:
        managed = False
        db_table = 'envios'


class Pedido(models.Model):
    id_pedido = models.CharField(primary_key=True, max_length=4)
    id_usuario3 = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario3')
    id_desc3 = models.ForeignKey(Descuentos, models.DO_NOTHING, db_column='id_desc3')

    def __str__(self):
        return self.id_pedido

    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoDetalle(models.Model):
    id_pdetalle = models.CharField(primary_key=True, max_length=4)
    id_pedido5 = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='id_pedido5')
    id_producto5 = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto5')
    cantidad = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.id_pdetalle

    class Meta:
        managed = False
        db_table = 'pedido-detalle'


class Productos(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=4)
    nom_prod = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=30)
    precio = models.IntegerField()
    stock = models.IntegerField()
    id_prov4 = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='id_prov4')
    cod_cate4 = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='cod_cate4')

    def __str__(self):
        return self.nom_prod
    
    class Meta:
        managed = False
        db_table = 'productos'


class Proveedores(models.Model):
    id_proveedor = models.CharField(primary_key=True, max_length=4)
    nom_prov = models.CharField(max_length=20)
    celular = models.CharField(max_length=9)
    nom_empresa = models.CharField(max_length=20)

    def __str__(self):
        return self.nom_prov

    class Meta:
        managed = False
        db_table = 'proveedores'


class Usuarios(models.Model):
    id_usuario = models.CharField(primary_key=True, max_length=4)
    nom_usuario = models.CharField(max_length=20)
    apell_usuario = models.CharField(max_length=20)
    fec_nac = models.DateField()
    direccion = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    celular = models.CharField(max_length=9)
    contrasena = models.CharField(max_length=20)

    def __str__(self):
        return self.nom_usuario

    class Meta:
        managed = False
        db_table = 'usuarios'


