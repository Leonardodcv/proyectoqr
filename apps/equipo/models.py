from dataclasses import Field
from email.policy import default
from tabnanny import verbose
from django.db import models
from django.db.models.signals import post_save,pre_save

# Create your models here.
class Fabricante(models.Model):
    id_fabricante = models.AutoField(primary_key = True)
    nombre= models.CharField(max_length=200, blank=False, null=False, verbose_name="Nombre del fabricante")
    activo=models.BooleanField(default=True)

    class Meta:
        verbose_name ="Fabricante"
        verbose_name_plural ="Fabricantes"

    def __str__(self):
        return f"{self.nombre}"

class Modelo(models.Model): 
    id_modelo = models.AutoField(primary_key = True)
    id_fabricante=models.ForeignKey("Fabricante", on_delete=models.CASCADE)   
    nombre= models.CharField(max_length=200, blank=False, null=False, verbose_name="Modelo de la computadora", help_text="Modelo")
    activo=models.BooleanField(default=True)
    
    class Meta:
        verbose_name ="Modelo de la computadora"
        verbose_name_plural ="Modelos de las computadoras"

    def __str__(self):
        return f"{self.id_fabricante} {self.nombre}"

class So(models.Model): 
    id_so = models.AutoField(primary_key = True)
    nombre= models.CharField(max_length=200, blank=False, null=False, verbose_name="Sistema operativo")
    activo=models.BooleanField(default=True)

    class Meta:
        verbose_name ="Sistema operativo"
        verbose_name_plural ="Sistemas operativos"

    def __str__(self):
        return f"{self.nombre}"

class Tipo(models.Model): 
    id_tipo = models.AutoField(primary_key = True)
    nombre= models.CharField(max_length=200, blank=False, null=False, verbose_name="Tipo de computadora")
    activo=models.BooleanField(default=True)

    class Meta:
        verbose_name ="Tipo de computadora"
        verbose_name_plural ="Tipos de computadoras"

    def __str__(self):
        return f"{self.nombre}"

class Departamento(models.Model): 
    id_departamento = models.AutoField(primary_key = True)
    nombre= models.CharField(max_length=200, blank=False, null=False)
    activo=models.BooleanField(default=True)    

    class Meta:
        verbose_name ="Departamento"
        verbose_name_plural ="Departamentos"

    def __str__(self):
        return f"{self.nombre}"        

class Permisos(models.Model): 
    id_permisos = models.AutoField(primary_key = True)
    nombre= models.CharField(max_length=200, blank=False, null=False)
    activo=models.BooleanField(default=True)    

    class Meta:
        verbose_name ="Permiso"
        verbose_name_plural ="Permisos"

    def __str__(self):
        return f"{self.nombre}"

###########################Equipo, usuarios e historial###########################

class Equipo(models.Model):
    ns=models.CharField(primary_key=True, max_length=30, blank=False, null=False)
    id_modelo=models.ForeignKey("Modelo", on_delete=models.CASCADE)
    id_tipo=models.ForeignKey("Tipo", on_delete=models.CASCADE)
    discoDuro=models.CharField(max_length=30, blank=False, null=False)
    id_so=models.ForeignKey("So", on_delete=models.CASCADE)
    folio=models.CharField(max_length=15, blank=True, null=True, default="N/A")
    ram=models.CharField(max_length=10, blank=False, null=False)
    ip_numero=models.CharField(max_length=15, blank=False, null=False)
    basura_electronica=models.BooleanField(default=False)
    Prestado=models.BooleanField(default=False)
    activo=models.BooleanField(default=True)
    
    class Meta:
        verbose_name ="Equipo"
        verbose_name_plural ="Equipos"
        ordering=["ns"]

    def __str__(self):
        return f"{self.ns} {self.id_modelo}"

class Usuario(models.Model):
    id_usuario=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50, blank=False, null=False)
    id_departamento=models.ForeignKey("Departamento", on_delete=models.CASCADE)
    puesto=models.CharField(max_length=50, blank=False, null=False, default="Estandar")
    allow=models.BooleanField(default=False)
    activo=models.BooleanField(default=True)

    class Meta:
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"
    
    def __str__(self):
        return f"{self.nombre}"

class Historial(models.Model):
    id_historial=models.AutoField(primary_key=True)
    ns=models.ForeignKey("Equipo", on_delete=models.CASCADE, verbose_name="Numero Serial de la computadora")
    id_usuario=models.ForeignKey("Usuario", on_delete=models.CASCADE, verbose_name="Nombre del usuario")
    fecha_entrega = models.DateField ('Fecha de entrega', auto_now=True , auto_now_add=False)
    fecha_devolucion = models.DateField('Fecha de devolucion', auto_now=True , auto_now_add=False)
    qr_code = models.ImageField(upload_to="CodigosQR")
    recibido=models.BooleanField(default=False)

    class Meta:
        verbose_name="Historial"
        verbose_name_plural="Historial"

    def __str__(self):
        return f"{self.ns} {self.id_usuario} {self.fecha_entrega} {self.fecha_devolucion}"
        
###########################Impresoras y escaneres###########################

class Impresora(models.Model):
    ns=models.CharField(primary_key=True, max_length=30, blank=False, null=False)
    id_modelo=models.ForeignKey("Modelo", on_delete=models.CASCADE)
    folio=models.CharField(max_length=15, blank=True, null=True, default="N/A")
    area=models.ForeignKey("Departamento", on_delete=models.CASCADE)
    activo=models.BooleanField(default=True)

    class Meta:
        verbose_name ="Impresora"
        verbose_name_plural ="Impresoras"
        ordering=["ns"]

    def __str__(self):
        return f"{self.ns} {self.fabricante} {self.modelo}"

class Escaner(models.Model):
    ns=models.CharField(primary_key=True, max_length=30, blank=False, null=False)
    id_modelo=models.ForeignKey("Modelo", on_delete=models.CASCADE)
    folio=models.CharField(max_length=15, blank=True, null=True, default="N/A")
    area=models.ForeignKey("Departamento", on_delete=models.CASCADE)
    activo=models.BooleanField(default=True)

    class Meta:
        verbose_name ="Escaner"
        verbose_name_plural ="Escaneres"
        ordering=["ns"]

    def __str__(self):
        return f"{self.ns} {self.fabricante} {self.modelo}"

"""  
def cambiar_estado(sender,instance,**kwargs):
    equipo = instance.equipo
    if equipo.Prestado == False:
        equipo.Prestado == True
        equipo.save()


post_save.connect(cambiar_estado, sender=Historial)
"""