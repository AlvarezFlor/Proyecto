from django.shortcuts import render,redirect,HttpResponse
from .models import Alumnos
from .forms import AlumnosForm
from .forms import MateriasCursarForm
from .models import Escuelaprocedencia
from .models import Carrera
from .models import Sexo
from .models import Periodoingreso
from .models import Estadocivil
from .models import Modcarrera
from .models import Entidadfederativa
from .models import PlanesdeEstudio
import datetime

# Create your views here.
#Esta es una vista 
def inicio(request):#pasamos el tipo de request como primer argumento.
    return render(request, 'paginas/inicio.html')#el return render nos permite renderizar una ventana la cual contiene el codigo html.
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def alumnos(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'escuela/indexalumnos.html', {'alumnos':alumnos})
def crearestudiante(request):
    alumnos= AlumnosForm(request.POST or None, request.FILES or None)
    escuelas = Escuelaprocedencia.objects.all()
    carreras = Carrera.objects.all()
    estadoc  = Estadocivil.objects.all()
    entidadfederativas = Entidadfederativa.objects.all()
    modc = Modcarrera.objects.all()
    periodos= Periodoingreso.objects.all()
    sexos = Sexo.objects.all()
    if alumnos.is_valid():
        alumnos.save()  
        return redirect('alumnos')
    return render(request, 'escuela/crearestudiantes.html', {'escuelas' : escuelas , 'carreras' :carreras , 'modc' : modc , 'sexos' : sexos , 'periodos': periodos , 'estadoc' : estadoc , 'entidadfederativas' : entidadfederativas, 'alumnos':alumnos})
def editarestudiante(request, id):
    alumno=Alumnos.objects.get(id=id)
    alumnos=AlumnosForm(request.POST or None, request.FILES or None, instance=alumno)
    if alumnos.is_valid() and request.POST:
        alumnos.save()
        return redirect('alumnos')
    return render(request, 'escuela/editarestudiantes.html', {'alumno':alumno,'alumnos':alumnos})
#Con esta funcion un usuario puede eliminar a un alumno mediante delete where
def eliminarestudiate(request,id):
    alumno=Alumnos.objects.get(id=id)
    alumno.delete()
    return redirect('alumnos')
#Aqui se va a programar la visualiazacion de la interfaz para dar de alta las materias por alumno
def daraltamaterias(request):
    materias=PlanesdeEstudio.objects.all()
    materia=MateriasCursarForm(request.POST or None)
    if materia.is_valid():
        materia.save()
        return redirect('inicio')
    return render(request, 'escuela/dardealtamaterias.html',{'materias':materias, 'materia':materia})
#metodo para visualizar la reticula
def reticula(request):
    mat1 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='I',clave1='EGG1')
    mat2 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='I',clave1='CGG1')
    mat3 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='I',clave1='DGG1')
    mat4 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='I',clave1='DBB1')
    mat5 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='I',clave1='EBB1')
    mat6 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='I',clave1='FBB1')
    mat7 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='II',clave1='ABB2')
    mat8 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='II',clave1='BBB2')
    mat9 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='II', clave1='CBB2')
    mat10 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='II', clave1='DBB2')
    mat11= PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='II', clave1='EBB2')
    mat12= PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='II', clave1='FBB2')
    mat13 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='III', clave1='ABB3')
    mat14 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='III', clave1='BBB3')
    mat15 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='III', clave1='CBB3')
    mat16 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='III', clave1='DBB3')
    mat17 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='III', clave1='ABB5')
    mat18 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='III', clave1='FBB3')
    mat19 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='IV', clave1='ABB4')
    mat20 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='IV', clave1='BBB4')
    mat21 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='IV', clave1='CBB4')
    mat22 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='IV', clave1='DBB4')
    mat23 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='IV', clave1='DBB5')
    mat24 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='IV', clave1='FBB4')
    mat25 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='V', clave1='DBB6')
    mat26 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='V', clave1='BBB5')
    mat27 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='V', clave1='EBB3')
    mat28 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='V', clave1='CBB5')
    mat29 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='V', clave1='EBB5')
    mat30 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='V', clave1='FBB5')
    mat31 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VI', clave1='ABB6')
    mat32 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VI', clave1='BBB6')
    mat33 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VI', clave1='EBB4')
    mat34 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VI', clave1='CBB6')
    mat35 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VI', clave1='EBB6')
    mat36 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VI', clave1='FBB6')
    mat37 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VII', clave1='ABB7')
    mat38 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VII', clave1='BBB7')
    mat39 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VII', clave1='CBB7')
    mat40 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VII', clave1='DBB7')
    mat41 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VII', clave1='EBB7')
    mat42 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VII', clave1='FBB7')
    mat43 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VIII', clave1='ABB8')
    mat44 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VIII', clave1='BBB8')
    mat45 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VIII', clave1='CBB8')
    mat46 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VIII', clave1='EBB8')
    mat47 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VIII', clave1='DBB8')
    mat48 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='VIII', clave2='TIF-1302')
    mat49 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='IX', clave1='ABB9')
    mat50 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='IX', clave2='TIF-1306')
    mat51 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='IX', clave2='TIF-1307')
    mat52 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='?', clave1='BGG9')
    mat53 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='IX', clave1='FBB9')
    mat54 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224',semestre='IX', clave1='BBB9')
    return render(request, 'escuela/reticula.html', {
        'mat1':mat1,'mat2':mat2,'mat3':mat3,'mat4':mat4,'mat5':mat5,'mat6':mat6,
        'mat7':mat7,'mat8':mat8,'mat9':mat9,'mat10':mat10,'mat11':mat11,'mat12':mat12,
        'mat13':mat13,'mat14':mat14,'mat15':mat15,'mat16':mat16,'mat17':mat17,'mat18':mat18,
        'mat19':mat19,'mat20':mat20,'mat21':mat21,'mat22':mat22,'mat23':mat23,'mat24':mat24,
        'mat25':mat25,'mat26':mat26,'mat27':mat27,'mat28':mat28,'mat29':mat29,'mat30':mat30,
        'mat31':mat31,'mat32':mat32,'mat33':mat33,'mat34':mat34,'mat35':mat35,'mat36':mat36,
        'mat37':mat37,'mat38':mat38,'mat39':mat39,'mat40':mat40,'mat41':mat41,'mat42':mat42,
        'mat43':mat43,'mat44':mat44,'mat45':mat45,'mat46':mat46,'mat47':mat47,'mat48':mat48,
        'mat49':mat49,'mat50':mat50,'mat51':mat51,'mat52':mat52,'mat53':mat53,'mat54':mat54,
        })