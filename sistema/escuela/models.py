from django.db import models

# Create your models here.
class Alumnos(models.Model):
    id= models.AutoField(primary_key=True)
    apellidopaterno= models.CharField(max_length=25, verbose_name='Apellido paterno')
    apellidomaterno= models.CharField(max_length=25, verbose_name='Apellido materno')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    ncontrol= models.CharField( max_length=15, verbose_name='N.Control')
    lugarnacimiento= models.CharField(max_length=25, verbose_name='Lugar nacimiento')
    fechanacimiento= models.DateField(verbose_name='Fecha de nacimiento' )
    sexo= models.CharField(max_length=10, verbose_name='Sexo')
    estadocivil= models.CharField(max_length=30, verbose_name='Estado civil')
    imagen= models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    domicilio= models.CharField(max_length=30, verbose_name='Domicilio')
    colonia= models.CharField(max_length=18, verbose_name='Colonia')
    codigopostal= models.CharField(  max_length=5,verbose_name='Codigo postal')
    ciudadolocalidad= models.CharField(max_length=25, verbose_name='Ciudad o localidad')
    entidadfederativa= models.CharField(max_length=20, verbose_name='Entidad federativa')
    telefono= models.CharField( max_length=10, verbose_name='Telefono')
    curp= models.CharField(max_length=18, verbose_name='Curp')
    correoelectronico= models.CharField(max_length=74, verbose_name='Correo electronico', blank=True)
    modalidad= models.CharField(max_length=1, verbose_name='Modalidad')
    escuelasdeprocedencia= models.CharField(max_length=20, verbose_name='Escuela de procedencia')
    direccion= models.CharField(max_length=70, verbose_name='Direccion')
    carrera=models.CharField(max_length=50, verbose_name='Carrera', blank=True)
    modcarrera=models.CharField(max_length=15, verbose_name='Modalidad Carrera', blank=True)
    periododeingreso=models.CharField(max_length=12, verbose_name='Periodo de ingreso', blank=True)

    def __str__(self):
        fila ="Apellido paterno: " + self.apellidopaterno + " - " + "Apellido materno: " + self.apellidomaterno +" - " + "Nombre: " + self.nombre + " - " + "N. Control: " + self.ncontrol + " - " + "Lugar nacimiento: " + self.lugarnacimiento + " - "  + "Sexo: "  + self.sexo + " - " + "Estado civil: " + self.estadocivil + " - " + "Domicilio: " + self.domicilio+ " - " + "Colonia: " + self.colonia + " - " + "Codigo postal: " + self.codigopostal+ " - " + "Ciudad o localidad: " + self.ciudadolocalidad+" - " + "Entidad federativa: " + self.entidadfederativa + " - " + "Telefono: " + self.telefono + " - " + "Curp: " + self.curp + " - " + "Correo electronico: " + self.correoelectronico + " - " + "Modalidad: " + self.modalidad + " - " +  "Escuela de procedencia: " + self.escuelasdeprocedencia + " - " +"Direccion: " + self.direccion + " - " + "Carrera"+self.carrera + " - " + "Modcarrera" + self.modcarrera + " - " + "Periododeingreso" + self.periododeingreso
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Estadocivil(models.Model):
    id = models.AutoField(primary_key=True)
    estcivil = models.CharField(max_length=30, verbose_name='Estado civil')
    def __str__(self) -> str:
        filaest= "Estado civil: " + self.estcivil
        return filaest 

class Sexo(models.Model):
    id = models.AutoField(primary_key=True)
    sex=models.CharField(max_length=10, verbose_name='Sexo')
    def __str__(self) -> str:
        filasex= "Sexo: " + self.sex
        return filasex

class Carrera(models.Model):
    id = models.AutoField(primary_key=True)
    nombrecarrera= models.CharField(max_length=50, verbose_name='Nombre carrera')
    clavecarrera = models.CharField(max_length=18, verbose_name='Clave')
    def __str__(self) -> str:
        filacarrera= "Nombre Carrera: " + " " + self.nombrecarrera + " -- " + "Clave Carrera:  " + " " +self.clavecarrera
        return filacarrera
class Entidadfederativa(models.Model):
    id = models.AutoField(primary_key=True)
    entfederativa = models.CharField(max_length=20, verbose_name='Entidad Federativa')
    def __str__(self) -> str:
        filaestado = "Entidad Federativa: " + self.entfederativa
        return filaestado

class Modcarrera(models.Model):
    id =models.AutoField(primary_key=True)
    modacarrera = models.CharField(max_length=15, verbose_name='Modalidad de carrera')
    def __str__(self) -> str:
        filamodacarrera = "Mod Carrera: " + " - " + self.modacarrera
        return filamodacarrera
    

class Periodoingreso(models.Model):
    id = models.AutoField(primary_key=True)
    periodo= models.CharField(max_length=12, verbose_name='Periodo Ingreso')
    def __str__(self) -> str:
        filaperiodo = "Periodo: " + " - " + self.periodo
        return filaperiodo



class Escuelaprocedencia(models.Model):
    id = models.AutoField(primary_key=True)
    modalidad= models.CharField(max_length=1, verbose_name='Modalidad' )
    escueladeprocedencia= models.CharField(max_length=40, verbose_name='Escuela de Procedencia')
    direccion= models.CharField(max_length=80, verbose_name='Direccion')

    def __str__(self):
        fila="-" "Modalidad: " + self.modalidad + " - " + "Escuela de procedencia: " + self.escueladeprocedencia + " - " + "Direccion: " + self.direccion
        return fila
    
class PlanesdeEstudio(models.Model):
    id = models.AutoField(primary_key=True)
    semestre=models.CharField(max_length=4, verbose_name='Semestre',blank=True)
    carrera=models.CharField(max_length=45,verbose_name='Carrera',blank=True)
    especialidad=models.CharField(max_length=55,verbose_name='Especialidad',blank=True)
    reticula=models.CharField(max_length=13,verbose_name='Reticula', blank=True)
    clave=models.CharField(max_length=16,verbose_name='Clave', blank=True)
    asignatura=models.CharField(max_length=55, verbose_name='Asignatura',blank=True,)
    clave1=models.CharField(max_length=4,verbose_name='Clave1', blank=True)
    clave2=models.CharField(max_length=8, verbose_name='Clave2', blank=True)
    hrsteoria=models.SmallIntegerField(max_length=1, verbose_name='Hrsteoria', blank=True,null=True )
    hrspractica=models.SmallIntegerField(max_length=1, verbose_name='Hrspractica', blank=True,null=True )
    creditos=models.SmallIntegerField(verbose_name='creditos', blank=True)
    nmateria=models.SmallIntegerField(max_length=2, verbose_name='nmateria', blank=True,null=True  )
    prerequisito=models.IntegerField(max_length=8, verbose_name='prerequisito', blank=True,null=True )
    tipomateria=models.CharField(max_length=7,verbose_name='Tipo materia', blank=True)
    
    def __str__(self) -> str:
        return super().__str__()
        
       
class Materiasacursar(models.Model):
    id = models.AutoField(primary_key=True)
    materia1= models.CharField(max_length=45, verbose_name='Materia1',)
    materia2= models.CharField(max_length=45, verbose_name='Materia2',)
    materia3= models.CharField(max_length=45, verbose_name='Materia3',)
    materia4= models.CharField(max_length=45, verbose_name='Materia4',)
    materia5= models.CharField(max_length=45, verbose_name='Materia5',)
    materia6= models.CharField(max_length=45, verbose_name='Materia6',)
    
    def __str__(self) -> str:
        filamaterias="Materia 1"+self.materia1 + " "+ "Materia 2"+self.materia2+" "+"Materia 3"+self.materia3+" "+"Materia 4"+self.materia2 + "Materia 5"+self.materia5+" " +"Materia 6"+self.materia6
        return filamaterias
