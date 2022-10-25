from pyexpat import model
from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
###########################SO###########################
class SoResource(resources.ModelResource):
    class Meta:
        model = So

class SoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class=SoResource
    search_fields = ('id_so','nombre','activo')
    list_display = ('id_so','nombre','activo')

############################FABRICANTE###########################
class FabricanteResource(resources.ModelResource):
    class Meta:
        model = Fabricante

class FabricanteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class=FabricanteResource
    search_fields = ('id_fabricante','nombre','activo')
    list_display = ('id_fabricante','nombre','activo')

############################Tipo###########################
class TipoResource(resources.ModelResource):
    class Meta:
        model = Tipo

class TipoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class=TipoResource
    search_fields = ('id_tipo','nombre','activo')
    list_display = ('id_tipo','nombre','activo')

############################Modelo###########################
class ModeloResource(resources.ModelResource):
    class Meta:
        model = Modelo

class ModeloAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class=ModeloResource
    search_fields = ('id_modelo','id_fabricante',"nombre",'activo')
    list_display = ('id_modelo','id_fabricante',"nombre", 'activo')

############################Departamento###########################
class DepartamentoResource(resources.ModelResource):
    class Meta:
        model = Departamento

class DepartamentoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class=DepartamentoResource
    search_fields = ('id_departamento','nombre','activo')
    list_display = ('id_departamento','nombre','activo')

############################Equipo###########################
class EquipoResource(resources.ModelResource):
    class Meta:
        model = Equipo

class EquipoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class=EquipoResource
    search_fields = ('ns','id_modelo','id_tipo', 'ram','ip_numero','basura_electronica', 'Prestado','activo')
    list_display =  ('ns','id_modelo','id_tipo', 'ram','ip_numero','basura_electronica', 'Prestado','activo')

############################Usuario###########################
class UsuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario

class UsuarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class=UsuarioResource
    search_fields = ('id_usuario','nombre','id_departamento', 'puesto','allow','activo')
    list_display =  ('id_usuario','nombre','id_departamento', 'puesto','allow','activo')

############################Historial###########################
class HistorialResource(resources.ModelResource):
    class Meta:
        model = Historial

class HistorialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class=UsuarioResource
    search_fields = ('ns','id_usuario','fecha_entrega', 'fecha_devolucion','recibido')
    list_display =  ('ns','id_usuario','fecha_entrega', 'fecha_devolucion','recibido')

############################Escaner###########################
class EscanerResource(resources.ModelResource):
    class Meta:
        model = Escaner

class EscanerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class=EscanerResource
    search_fields = ('ns','id_modelo','area','activo')
    list_display =  ('ns','id_modelo','area','activo')

############################Impresora###########################
class ImpresoraResource(resources.ModelResource):
    class Meta:
        model = Impresora

class ImpresoraAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class=ImpresoraResource
    search_fields = ('ns','id_modelo','area','activo')
    list_display =  ('ns','id_modelo','area','activo')

admin.site.register(So, SoAdmin)
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Modelo,ModeloAdmin)
admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Permisos)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Equipo,EquipoAdmin)

admin.site.register(Historial, HistorialAdmin)
admin.site.register(Escaner,EscanerAdmin)
admin.site.register(Impresora, ImpresoraAdmin)