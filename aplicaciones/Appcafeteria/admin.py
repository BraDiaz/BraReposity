from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class campusResource(resources.ModelResource):
    class Meta:
        model = Campus
class campusAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['descripcion']
    list_display = ('id_campus','descripcion', 'estado', 'fecha_Creacion')
    resource_class = campusResource

class empleadosResource(resources.ModelResource):
    class Meta:
        model = Empleados
class empleadosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['descripcion','cedula','tanda']
    list_display = ('id_empleado','nombre', 'cedula', 'tanda_labor','porciento_comision','fecha_ingreso','estado','fecha_Creacion')
    resource_class = empleadosResource

class cafeteriaResource(resources.ModelResource):
    class Meta:
        model = Cafeteria
class cafeteriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['descripcion','encargado']
    list_display = ('id_cafeteria','descripcion','id_campus','encargado','estado','fecha_Creacion')
    resource_class = cafeteriaResource

class usuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario
class usuarioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre','cedula']
    list_display = ('id_usuario','nombre','cedula','tipo_usuario','limiteCredito','estado','fecha_Creacion')
    resource_class = usuarioResource

class marcaResource(resources.ModelResource):
    class Meta:
        model = Marca
class marcaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['descripcion']
    list_display = ('id_marca','descripcion','estado','fecha_Creacion')
    resource_class = marcaResource

class proveedoresResource(resources.ModelResource):
    class Meta:
        model = Proveedor
class proveedoresAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre_comercial']
    list_display = ('id_proveedor','nombre_comercial','estado','fecha_Creacion')
    resource_class = proveedoresResource

class articuloResource(resources.ModelResource):
    class Meta:
        model = Articulo
class articuloAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['descripcion']
    list_display = ('id_articulo','descripcion','id_marca','costo','id_proveedor','existencia','estado','fecha_Creacion')
    resource_class = articuloResource

class facturaResource(resources.ModelResource):
    class Meta:
        model = Factura
class facturaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id_facturacion','producto_comprado']
    list_display = ('id_facturacion','id_empleado','id_usuario','producto','cantidad','comentario','total','fecha_Creacion','estado')
    resource_class = facturaResource

class tipoUsuarioResource(resources.ModelResource):
    class Meta:
        model = tipoUsuario
class tipoUsuarioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['descripcion']
    list_display = ('id_tipoUsuario','descripcion','estado','fecha_Creacion')
    resource_class = tipoUsuarioResource


admin.site.register(Campus, campusAdmin)
admin.site.register(Empleados, empleadosAdmin)
admin.site.register(Cafeteria, cafeteriaAdmin)
admin.site.register(Usuario, usuarioAdmin)
admin.site.register(tipoUsuario, tipoUsuarioAdmin)
admin.site.register(Articulo, articuloAdmin)
admin.site.register(Marca, marcaAdmin)
admin.site.register(Proveedor, proveedoresAdmin)
admin.site.register(Factura, facturaAdmin)