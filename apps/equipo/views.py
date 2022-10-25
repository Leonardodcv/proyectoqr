from multiprocessing import context
import os
import qrcode
import webbrowser
import sys
from ast import Pass
from cmath import e
from distutils.log import error
from pyexpat import model
from re import template
from urllib import request, response
from datetime import datetime
from django.shortcuts import render, redirect
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import View, TemplateView, ListView, DeleteView, UpdateView, CreateView
from django.http import HttpRequest, HttpResponse,JsonResponse
from django.core.files import File as DjangoFile
from io import BytesIO
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer, GappedSquareModuleDrawer, HorizontalBarsDrawer, RoundedModuleDrawer, SquareModuleDrawer, VerticalBarsDrawer
from io import StringIO
from django.core import management
from apps import equipo

from apps.equipo.models import Equipo
from .forms import EquipoForm, UsuarioForm, HistorialForm
from .models import Equipo, Usuario, Historial, Departamento

# Create your views here.
###########################Pruebas###########################
class YourPage():
    def dispatch(self, *args, **kwargs):
        create_fixture('equipo', 'equipo/static/test.csv')
        return super(YourPage, self).dispatch(*args, **kwargs)

def create_fixture(app_name, filename):
    buf = StringIO()
    management.call_command('dumpdata', app_name, stdout=buf)
    buf.seek(0)
    with open(filename, 'w') as f:
        f.write(buf.read())

###########################Indice###########################
def home(request):
    return render(request, "index.html")

class Inicio(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")

def hometest(request):
    return render(request, "test.html")

class Test(View):
    def get(self, request, *args, **kwargs):
        return render(request, "test.html")
###########################Equipos Clases###########################
class ListadoEquipo(View):
    model=Equipo
    form_class=EquipoForm
    template_name="equipo/listar_equipos.html"
    context_object_name="equipos"
    queryset=None

    def get_queryset(self):
        return self.model.objects.filter(activo=True)

    def get_context_data(self, **kwargs):
        contexto={}
        contexto["equipos"]=self.get_queryset()
        contexto["form"]=self.form_class
        return contexto

    def get(self, request, *args,**kwargs):
        return render(request, self.template_name, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("equipo:listar_equipos")

class ListadoEquipoLibres(ListView):
    model=Equipo
    template_name="equipo/listar_equipos_libres.html"
    context_object_name="equipos"
    queryset=Equipo.objects.filter(activo=True).filter(Prestado=False)

class ListadoEquipoPrestados(ListView):
    model=Equipo
    template_name="equipo/listar_equipos_prestados.html"
    context_object_name="equipos"
    queryset=Equipo.objects.filter(activo=True).filter(Prestado=True)

class RegistrarEquipo(CreateView):
    model=Equipo
    form_class=EquipoForm
    template_name="equipo/crear_equipo.html"
    success_url=reverse_lazy("equipo:listar_equipos")

class ActualizarEquipo(UpdateView):
    model=Equipo
    form_class=EquipoForm
    template_name="equipo/crear_equipo.html"
    success_url=reverse_lazy("equipo:listar_equipos")
    reverse_lazy("equipo:listar_equipos")

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["equipos"] =Equipo.objects.filter(activo=True)
        return context

class EliminarEquipo(DeleteView):
    model=Equipo

    def post(self, request, pk, *args, **kwargs):
        object=Equipo.objects.get(ns=pk)
        object.activo=False
        object.save()
        return redirect("equipo:listar_equipos")

###########################Usuairos Clases###########################
class ListadoUsuario(ListView):
    model=Usuario
    template_name="usuarios/listar_usuarios.html"
    context_object_name="usuarios"
    queryset=Usuario.objects.all()

class RegistrarUsuario(CreateView):
    model=Usuario
    form_class=UsuarioForm
    template_name="usuarios/crear_usuario.html"
    success_url=reverse_lazy("equipo:listar_usuarios")

class ActualizarUsuario(UpdateView):
    model=Usuario
    form_class=UsuarioForm
    template_name="usuarios/crear_usuario.html"
    success_url=reverse_lazy("equipo:listar_usuarios")
    reverse_lazy("equipo:listar_usuarios")

class EliminarUsuario(DeleteView):
    model=Usuario
    def post(self, request, pk, *args, **kwargs):
        object=Usuario.objects.get(id_usuario=pk)
        object.activo=False
        object.save()
        return redirect("equipo:listar_usuarios")

###########################Equipos funciones###########################
def crearEquipo(request):
    if request.method =="POST":
        equipo_form = EquipoForm(request.POST)
        if equipo_form.is_valid():
            equipo_form.save()
            return redirect("index") 
    else:
        equipo_form=EquipoForm()
    return render(request, "equipo/crear_equipo.html", {"equipo_form":equipo_form})

def listarEquipos(request):
    equipos=Equipo.objects.filter(activo=True)
    return render(request, "equipo/listar_equipos.html", {"equipos":equipos})

def editarEquipo(request, ns):
    equipo_form=None
    error=None
    try:
        equipo=Equipo.objects.get(ns=ns)
        if request.method=="GET":
            equipo_form=EquipoForm(instance = equipo)
        else:
            equipo_form=EquipoForm(request.POST, instance=equipo)
            if equipo_form.is_valid():
                equipo_form.save()
            redirect("index")
        
    except Exception as e:
        error=e
    return render(request, "equipo/crear_equipo.html", {"equipo_form":equipo_form, "error":error})
    
def eliminarEquipo(request, ns):
    equipo=Equipo.objects.get(ns=ns)
    equipo.activo=False
    equipo.save()
    return redirect("equipo:listar_equipos")
"""
    if request.method=="POST":
        #equipo.delete()
        equipo.activo=False
        equipo.save()
        return redirect("equipo:listar_equipos")
    return render(request, "equipo/eliminar_equipo.html", {"equipo":equipo})
"""



###########################Usuarios funciones###########################
def crearUsuario(request):
    if request.method =="POST":
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect("index")
    else:
        print("No es post")
        usuario_form=UsuarioForm()
    return render(request, "usuarios/crear_usuario.html", {"usuario_form":usuario_form})

def listarUsuario(request):
    usuarios=Usuario.objects.filter(activo=True)
    return render(request, "usuarios/listar_usuarios.html", {"usuarios":usuarios})

def editarUsuario(request, id_usuario):
    usuario_form=None
    error=None
    try:
        usuario=Usuario.objects.get(id_usuario=id_usuario)
        if request.method=="GET":
            usuario_form=UsuarioForm(instance = usuario)
        else:
            usuario_form=UsuarioForm(request.POST, instance=usuario)
            if usuario_form.is_valid():
                usuario_form.save()
            redirect("index")
    except Exception as e:
        error=e
    return render(request, "usuarios/crear_usuario.html", {"usuario_form":usuario_form, "error":error})
    
def eliminarUsuario(request, id_usuario):
    usuario=Usuario.objects.get(id_usuario=id_usuario)
    usuario.activo=False
    usuario.save()
    return redirect("equipo:listar_usuarios")

"""
Notas
dispatch():valida la peticion y elige que metodo HTTP se utilizo para la solicitud
http_method_not allowed(): retorna un error cuando se utiliza un metodo HTTP no soportado o definido
options()
"""

###########################Historial###########################
class ListadoHistorial(ListView):
    model=Historial
    template_name="prestamos/listar_prestamos.html"
    context_object_name="prestamos"
    queryset=Historial.objects.all()
    
class ListadoHistorialPrestados(ListView):
    model=Historial
    template_name="prestamos/listar_prestamos_no_devueltos.html"
    context_object_name="prestamos"
    queryset=Historial.objects.filter(recibido=False)

class ListadoHistorialDevueltos(ListView):
    model=Historial
    template_name="prestamos/listar_prestamos_devueltos.html"
    context_object_name="prestamos"
    queryset=Historial.objects.filter(recibido=True)

def generate_qrcode(request):
    nombre_responsable="Jairo Raul Huerta Vargas"
    departamento="Human Resources"
    computadora="MXLTC9CJF63"
    allow="Si"
    data =  nombre_responsable+"\n" +departamento+"\n" +computadora+"\n"+allow
    img = qrcode.make(data)
    img.save(nombre_responsable+".png")
    buf = BytesIO()		# BytesIO se da cuenta de leer y escribir bytes en la memoria
    img.save(buf)
    image_stream = buf.getvalue()

    response = HttpResponse(image_stream, content_type="image/png")
    return response

class TerminarHistorial(DeleteView):
    model=Historial

    def post(self, request, pk, *args, **kwargs):
        prestamo=Historial.objects.get(id_historial = pk)
        prestamo.fecha_devolucion=datetime.today()
        prestamo.recibido=True
        datos1= str(prestamo.ns)
        datos2 = datos1.split()
        equipo=Equipo.objects.filter(ns=datos2[0]).first()
        equipo.Prestado=False
        equipo.save()
        prestamo.save()
        return redirect("equipo:listar_prestamos")

class RegistrarHistorial(CreateView):
    model=Historial
    form_class=HistorialForm
    template_name="prestamos/crear_prestamo.html"
    success_url=reverse_lazy("equipo:listar_prestamos")
    
    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        equipo=Equipo.objects.filter(ns=request.POST.get("ns")).first()
        usuario=Usuario.objects.filter(id_usuario=request.POST.get("id_usuario")).first()
        print(usuario.id_departamento)
        #departamento=Departamento.objects.filter(id_departamento=usuario.id_departamento).first()
        #print(departamento.nombre)
        
        equipo.Prestado=True
        nombre_responsable=str(usuario.nombre)
        departamento=str(usuario.id_departamento)
        computadora="MXLT"+request.POST.get("ns")
        allow = 'Permitido' if usuario.allow==True else 'No Permitido'
        data =  "Responsable: "+nombre_responsable+"\n"+"Departamento: "+departamento+"\n"+"Usuario computadora: "+computadora+"\n"+"Computadora puede salir de la empresa: "+allow
        img = qrcode.make(data)
        img.save("CodigosQR\\"+str(usuario.id_departamento)+"\\"+nombre_responsable+".png")
        buf = BytesIO()		# BytesIO se da cuenta de leer y escribir bytes en la memoria
        img.save(buf)
        image_stream = buf.getvalue()
        form = self.form_class(request.POST)

        #mrapp = os.path.join(os.getcwd(),nombre_responsable+".png")
        #new_s = mrapp.replace('\\','/')
        file_obj1 = DjangoFile(open("CodigosQR/"+str(usuario.id_departamento)+"/"+nombre_responsable+".png", mode='rb'), name=nombre_responsable+".png")
        #file_obj1 = DjangoFile(open(new_s), name=nombre_responsable+".png")
        #file_obj1 = DjangoFile(open(f"CodigosQR\{str(usuario.id_departamento)}\{nombre_responsable}.png", mode="rb"), name=nombre_responsable+".png")

        chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chromepath))
        webbrowser.get('chrome').open("C:/Users/intern.it/Documents/proyectoqr/CodigosQR\\"+str(usuario.id_departamento)+"\\"+nombre_responsable+".png")
        
        #webbrowser.open_new("CodigosQR\\"+str(usuario.id_departamento)+"\\"+nombre_responsable+".png")
        if form.is_valid():
            nuevo_prestamo=Historial(
                qr_code=file_obj1,
                ns=form.cleaned_data.get("ns"),
                id_usuario=form.cleaned_data.get("id_usuario"),
                fecha_entrega=datetime.today(),
                fecha_devolucion=datetime.today()
            )
            nuevo_prestamo.save()
            
        equipo.save()
        file_obj1.close()
        return redirect("equipo:listar_prestamos")
    


class ActualizarHistorial(UpdateView):
    model=Historial
    form_class=HistorialForm
    template_name="prestamos/crear_prestamo.html"
    success_url=reverse_lazy("equipo:listar_prestamos")


