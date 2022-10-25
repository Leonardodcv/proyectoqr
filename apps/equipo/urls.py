from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import crearUsuario, listarUsuario, editarUsuario, eliminarUsuario

from .views import ListadoEquipo, ListadoEquipoLibres, ListadoEquipoPrestados, EliminarEquipo, RegistrarEquipo, ActualizarEquipo
from .views import ListadoHistorial, TerminarHistorial, RegistrarHistorial, ActualizarHistorial, ListadoHistorialPrestados, ListadoHistorialDevueltos
from .views import ListadoUsuario, EliminarUsuario, RegistrarUsuario, ActualizarUsuario
urlpatterns = [
    ###########################Equipos###########################
    path("crear_equipo/", login_required(RegistrarEquipo.as_view()), name="crear_equipo"),
    path('listar_equipos/', login_required(ListadoEquipo.as_view()), name = 'listar_equipos'),
    path('listar_equipos_libres/', login_required(ListadoEquipoLibres.as_view()), name = 'listar_equipos_libres'),
    path('listar_equipos_prestados/', login_required(ListadoEquipoPrestados.as_view()), name = 'listar_equipos_prestados'),
    path("editar_equipo/<slug:pk>", login_required(ActualizarEquipo.as_view()), name="editar_equipo"),
    path("eliminar_equipo/<slug:pk>/", login_required(EliminarEquipo.as_view()), name="eliminar_equipo"),

    ###########################Usuarios funciones###########################
    #path("crear_usuario/", crearUsuario, name="crear_usuarios"),
    #path("listar_usuarios/", listarUsuario, name="listar_usuarios"),
    #path("editar_usuarios/<int:id_usuario>", editarUsuario, name="editar_usuario"),
    #path("eliminar_usuario/<int:id_usuario>", eliminarUsuario, name="eliminar_usuario"),
    ###########################Usuarios clases###########################

    path("crear_usuario/", login_required(RegistrarUsuario.as_view()), name="crear_usuario"),
    path("listar_usuarios/", login_required(ListadoUsuario.as_view()), name="listar_usuarios"),
    path("editar_usuarios/<int:pk>", login_required(ActualizarUsuario.as_view()), name="editar_usuario"),
    path("eliminar_usuario/<int:pk>", login_required(EliminarUsuario.as_view()), name="eliminar_usuario"),

    ###########################Historial###########################
    path("crear_prestamo/", login_required(RegistrarHistorial.as_view()), name="crear_prestamo"),
    path('listar_prestamos/', login_required(ListadoHistorial.as_view()), name = 'listar_prestamos'),
    path('listar_prestamos_no_devueltos/', login_required(ListadoHistorialPrestados.as_view()), name = 'listar_prestamos_no_devueltos'),
    path('listar_prestamos_devueltos/', login_required(ListadoHistorialDevueltos.as_view()), name = 'listar_prestamos_devueltos'),
    path("editar_prestamo/<int:pk>", login_required(ActualizarHistorial.as_view()), name="editar_prestamo"),
    path("terminar_prestamo/<int:pk>/", login_required(TerminarHistorial.as_view()), name="terminar_prestamo"),

    ###########################Pruebas###########################
    path("tables-data/", login_required(ListadoUsuario.as_view()), name="tables-data"),

]

