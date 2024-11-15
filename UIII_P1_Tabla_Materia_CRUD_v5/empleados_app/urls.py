from django.urls import path 
from empleados_app import views 

urlpatterns = [
    path("", views.inicio_vista,name="inicio_vista"),
    path("registrarEmpleados/",views.registrarEmpleados,name="registrarEmpleados"),
    path("seleccionarEmpleados/<id>",views.seleccionarEmpleados,name="seleccionarEmpleados"),
    path("editarEmpleados/",views.editarEmpleados,name="editarEmpleados"),
    path("borrarEmpleados/<id>",views.borrarEmpleados,name="borrarEmpleados")
    
]
