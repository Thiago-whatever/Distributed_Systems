from django.urls import path
from . import views

app_name = "myfirstapp" #Me permite poner urls de forma mas elegante    

urlpatterns = [
    path("", views.index, name="index"),

    # ejemplo: /myfirstapp/5/detalles/
    path("<int:estudiante_id>/detalles/", views.detalles, name="detalles"),

    # ejemplo: /myfirstapp/5/carreras/
    path("<int:estudiante_id>/carreras/", views.carreras, name="carreras"),
    
    # ejemplo: /myfirstapp/5/agrega_carrera/
    path("<int:estudiante_id>/agrega_carrera/", views.agrega_carrera, name="agrega_carrera"),

    path("asincrono/", views.asincrono, name="asincrono"),

]

