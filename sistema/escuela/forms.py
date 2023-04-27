from django import forms
from .models import Alumnos
from .models import Materiasacursar

class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['apellidopaterno','apellidomaterno','nombre','ncontrol',
                  'lugarnacimiento','fechanacimiento','sexo','estadocivil',
                  'imagen','domicilio','colonia','codigopostal','ciudadolocalidad',
                  'entidadfederativa','telefono','curp','correoelectronico','modalidad',
                  'escuelasdeprocedencia','direccion','carrera', 'modcarrera', 'periododeingreso']
        #Se establecen los parametros para la generacion los campos con propiedades especificas en el formulario.
        widgets = {
            'apellidopaterno': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'minlength' : '5',
                    'maxlength' : '25',
                    'autofocus':'autofocus',
                    'value':""
                   
                }
            ),
            'apellidomaterno': forms.TextInput(
                attrs={
                    'class' : 'form-control  ',
                    'minlength' : '5',
                    'maxlength' : '25'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class' : 'form-control  ',
                    'minlength' : '5',
                    'maxlength' : '25'
                }
            ),
            'ncontrol': forms.TextInput(
                attrs={
                    'class' : 'form-control ',
                    'minlength' : '8',
                    'maxlength' : '16',
                    'required': 'required'
                }
            ),
            'lugarnacimiento': forms.TextInput(
                attrs={
                    'class' : 'form-control ',
                    'minlength' : '5',
                    'maxlength' : '25'
                    
                }
            ),
            'fechanacimiento':forms.DateInput(

                attrs={
                    'class': ' form-control',
                    'type': 'date',
                    'value':'',
                    'required':'True'
                }
            ),
            'curp':forms.TextInput(
                
                attrs={
                    'class': ' form-control ',
                    'minlength' : '18',
                    'maxlength' : '18'
                    
                }
            ),
            'sexo':forms.TextInput(
                
                attrs={
                    'class': ' form-control ',
                    'list' : 'sexo',
                    'minlength' : '10',
                    'maxlength' : '10'
                    
                }
            ),
            'estadocivil':forms.TextInput(
                
                attrs={
                    'class': ' form-control ',
                    'list' : 'estadocivil',
                    'minlength' : '5',
                    'maxlength' : '30'
                    
                }
            ),
            'imagen':forms.FileInput(
                
                attrs={
                    'class': ' form-control',
                    
                }
            ),
            'domicilio':forms.TextInput(
                
                attrs={
                    'class': ' form-control ',
                    'minlength' : '6',
                    'maxlength' : '30'
                }
            ),
            'colonia':forms.TextInput(
                
                attrs={
                    'class': ' form-control ',
                    'minlength' : '4',
                    'maxlength' : '18'
                }
            ),
            'codigopostal':forms.TextInput(
                
                attrs={
                    'class': ' form-control ',
                     'type':'text',
                    'minlength' : '5',
                    'maxlength' : '5'
                }
            ),
            'ciudadolocalidad':forms.TextInput(
                
                attrs={
                    'class': ' form-control ',
                    'minlength' : '8',
                    'maxlength' : '25'
                    
                }
            ),
            'entidadfederativa':forms.TextInput(
                
                attrs={
                    'class': ' form-control ',
                    'list' : 'entidadfederativa',
                    'minlength' : '6',
                    'maxlength' : '20'
                }   
            ),
            'sexo':forms.TextInput(
                
                attrs={
                    'class': ' form-control ',
                    'minlength' : '8',
                    'maxlength' : '10' 
                }
            ),
            'telefono':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'minlength' : '10',
                    'maxlength' : '10'
                    
                }
            ),
            'correoelectronico':forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'type': 'email' 
                }
            ),
            'escuelasdeprocedencia':forms.TextInput (
                attrs={
                    'class': 'form-control',
                    'list' : 'escuelas'
                    
                }
            ),
            'modalidad':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'tel',
                    'minlength' : '1',
                    'maxlength' : '1'
                }
            ),
            'direccion':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'minlength' : '5',
                    'maxlength' : '30'
                }
            ),
            'carrera':forms.TextInput(
                attrs={
                    'class': 'form-control col-md-10',
                    'list': 'carrera',
                    'minlength' : '5',
                    'maxlength' : '30'
                }
            )
            ,
            'modcarrera':forms.TextInput(
                attrs={
                    'class': 'form-control col-md-10',
                    'list' : 'modcarrera',
                    'minlength' : '5',
                    'maxlength' : '15'
                }
            ),
            'periododeingreso':forms.TextInput(
                attrs={
                    'class': 'form-control col-md-10',
                    'list' : 'periodoingreso',
                    'minlength' : '12',
                    'maxlength' : '12'
                }
            )
        }
class MateriasCursarForm(forms.ModelForm):
    class Meta:
        model = Materiasacursar
        fields=['materia1','materia2','materia3','materia4','materia5','materia6']
        widgets={
            'materia1': forms.TextInput(
                attrs={
                    'class':"form-control",
                    'id':'materia1',
                    'type':"text",
                    'list':"selecionarmaterias",
                    'placeholder':"SELECCIONAR MATERIA"
                }
            ),
            'materia2': forms.TextInput(
                attrs={
                    'class':"form-control",
                    'id':'materia2',
                    'type':"text",
                    'list':"selecionarmaterias",
                    'placeholder':"SELECCIONAR MATERIA"
                }
            ),
            'materia3': forms.TextInput(
                attrs={
                    'class':"form-control",
                    'id':'materia3',
                    'type':"text",
                    'list':"selecionarmaterias",
                    'placeholder':"SELECCIONAR MATERIA"
                }
            ),
            'materia4': forms.TextInput(
                attrs={
                    'class':"form-control",
                    'id':'materia4',
                    'type':"text",
                    'list':"selecionarmaterias",
                    'placeholder':"SELECCIONAR MATERIA"
                }
            ),
            'materia5': forms.TextInput(
                attrs={
                    'class':"form-control",
                    'id':'materia5',
                    'type':"text",
                    'list':"selecionarmaterias",
                    'placeholder':"SELECCIONAR MATERIA"
                }
            ),
            'materia6': forms.TextInput(
                attrs={
                    'class':"form-control",
                    'id':'materia6',
                    'type':"text",
                    'list':"selecionarmaterias",
                    'placeholder':"SELECCIONAR MATERIA"
                }
            )
        }