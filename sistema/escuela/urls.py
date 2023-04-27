from django.urls import path
from.import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns= [
    path('',views.inicio, name='inicio'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('alumnos',views.alumnos, name='alumnos'),
    path('escuela/crearestudiantes', views.crearestudiante, name='crearestudiantes'),
    path('escuela/editarestudiantes/<int:id>', views.editarestudiante, name='editarestudiantes'),
    path('eliminarestudiantes/<int:id>',views.eliminarestudiate, name='eliminarestudiantes'),
    path('seleccionarmaterias',views.daraltamaterias, name='seleccionarmaterias'),
    path('reticula',views.reticula, name='reticula'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
