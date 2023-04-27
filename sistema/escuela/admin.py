from django.contrib import admin
from .models import Alumnos
from .models import Carrera
from .models import Entidadfederativa
from .models import Estadocivil
from .models import Escuelaprocedencia
from .models import Modcarrera
from .models import Periodoingreso
from .models import Sexo
from .models import PlanesdeEstudio
from .models import Materiasacursar
# Register your models here.
admin.site.register(Alumnos)
admin.site.register(Carrera)
admin.site.register(Entidadfederativa)
admin.site.register(Escuelaprocedencia)
admin.site.register(Estadocivil)
admin.site.register(Modcarrera)
admin.site.register(Periodoingreso)
admin.site.register(Sexo)
#admin.site.register(SeleccionarMaterias)
@admin.register(PlanesdeEstudio)
class PlanesdeEstudio(admin.ModelAdmin):
    list_display= ('id','semestre','carrera','especialidad','reticula','clave','asignatura','clave1','clave2','creditos','nmateria','prerequisito','tipomateria',)
#admin.site.register(Materiasacursar)
@admin.register(Materiasacursar)
class MateriasacursarAdmin(admin.ModelAdmin):
    list_display= ('id','materia1','materia2','materia3','materia4','materia5','materia6')
