from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django import forms
from django.db.models import Q
from .models import *

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            "ns", "id_modelo", 
            "id_tipo", "discoDuro", 
            "id_so", "folio", 
            "ram", "ip_numero",
            "basura_electronica" 
        ]
        labels={
            "ns":"Numero serial",
            "id_modelo": "Modelo de computadora",
            "id_tipo":"Tipo de computadora",
            "discoDuro":"Tamaño del disco duro",
            "id_so":"Sistema operativo instalado",
            "folio":"Folio de la computadora",
            "ram":"Ram instalada",
            "ip_numero":"IP de la computadora",
            "basura_electronica":"El equipo es actualmente es basura electronica"
        }

        Widgets={
            "ns" : forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),
            "discoDuro" : forms.TextInput(
                attrs={
                    'class':'form-control',
                    "placeholder":"Tamaño del disco duro instalado en la computadora"
                }
            ),
            "folio" : forms.TextInput(
                attrs={
                    'class':'form-control',
                    "placeholder":"Escribr el folio de la computadora"
                }
            ),
            "ram" : forms.TextInput(
                attrs={
                    'class':'form-control',
                    "placeholder":"Ram instalada en la computadora"
                }
            ),
            "ip_numero" : forms.TextInput(
                attrs={
                    'class':'form-control',
                    "placeholder":"IP de la computadora"
                }
            ),
        }


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            "nombre", "id_departamento",
            "puesto","allow"
        ]

        labels={
            "nombre":"Nombre del usuario",
            "id_departamento": "Departamento",
            "puesto":"Puesto que actualmente posee",
            "allow":"Permiso para sacar una computadora de la empresa",
        }

        Widgets={
            "nombre" : forms.TextInput(
                attrs={
                    'class':'form-control',
                    "placeholder":"Nombre de la persona que puede usar una computadora"
                }
            ),
            "id_departamento" : forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),
            "puesto" : forms.TextInput(
                attrs={
                    'class':'form-control',
                    "placeholder":"Nombre del puesto actual"
                }
            ),
            "allow" : forms.TextInput(
                attrs={
                    'class':'form-control',
                    "placeholder":"Selecione la casilla  si el usuario puede sacar la computadora de la empresa"
                }
            ),
        }

class HistorialForm(forms.ModelForm):
    class Meta:
        model=Historial
        fields= [
            "ns","id_usuario",
        ]
        labels = {
            'ns': 'Numero serial de la computadora',
            'id_usuario': 'Nombre del usuario ',
        }

        Widgets={
            "ns" : forms.TextInput(
                attrs={
                    'class':'form-control',
                    "placeholder":"Nombre de la persona que puede usar una computadora"
                }
            ),
            "id_usuario" : forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),
        }

    ns = forms.ModelChoiceField(queryset=Equipo.objects.filter(Prestado=False))
    ns.widget.attrs['placeholder'] = 'Numero serial'
    ns.widget.attrs['class'] = 'form-control'

    ns.widget.attrs.update({'class': 'form-control'})
    ns.widget.attrs.update({'label': 'Numero serial de la computadora'})
    ns.widget.attrs.update({'verbose_name': 'Numero serial de la computadora'})
    #ns.label("Numero serial de la computadoras")

    id_usuario = forms.ModelChoiceField(queryset=Usuario.objects.filter(allow=True))
    id_usuario.widget.attrs['placeholder'] = 'Nombre del usuario'
    id_usuario.widget.attrs['class'] = 'form-control'
    
    id_usuario.widget.attrs.update({'class': 'form-control'})
    id_usuario.widget.attrs.update({'label': 'Nombre del usuario'})
    ns.widget.attrs.update({'verbose_name': 'Nombre del usuario'})

    