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
# def reticula(request):
#     sem1 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224', semestre='I')
#     sem2 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224', semestre='II')
#     sem3 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224', semestre='III')
#     sem4 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224', semestre='IV')
#     sem5 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224', semestre='V')
#     sem6 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224', semestre='VI')
#     sem7 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224', semestre='VII')
#     sem8 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224', semestre='VIII')
#     sem9 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224', semestre='IX')
#     sem10 = PlanesdeEstudio.objects.filter(reticula='ISIC-2010-224', semestre='X')

#     return render(request, 'escuela/reticula.html', {'sem1':sem1,'sem2':sem2,'sem3':sem3,'sem4':sem4,'sem5':sem5,'sem6':sem6,'sem7':sem7,'sem8':sem8,'sem9':sem9,'sem10':sem10})
def roman_to_int(s):
    roman_map = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9}
    result = 0
    for i in range(len(s)):
        if i > 0 and roman_map[s[i]] > roman_map[s[i-1]]:
            result += roman_map[s[i]] - 2 * roman_map[s[i-1]]
        else:
            result += roman_map[s[i]]
    return result

def reticula(request):
    materias = PlanesdeEstudio.objects.order_by('semestre')
    context = {'materias': materias}
    return render(request, 'escuela/reticula.html', context)