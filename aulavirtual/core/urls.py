from django.urls import path, re_path
from . import views #cuando pongo el punto me refiero al mismo directorio

urlpatterns = [
    path('', views.index, name='index'), #url, nombre de la vista que lo atiende y un name
    path('alumnos_listado', views.alumnos_listado, name='alumnos_listado'),
    path('alumnos/detalle/<str:nombre_alumno>', views.alumno_detalle, name='alumnos_detalle'), # para pasar parametros atravez de url
    re_path(r'alumnos/historico/(?P<year>[0-9]{4})/$', views.alumnos_historico, name='alumnos_historico'),  # para filtrar url 
    path('alumnos/activos', views.alumnos_estado, {'estado': 'activo'},name='alumnos_estados'), # con los parametros de esta manera una misma vista puede atender dos parametros distintos
    path('alumnos/inactivos', views.alumnos_estado, {'estado': 'inactivo'},name='alumnos_estados'),

]
