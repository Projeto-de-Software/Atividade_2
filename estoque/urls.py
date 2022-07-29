from django.urls import path, include
from .controllers import *


urlpatterns = [
    path("", loadPageGrafo , name='grafoInicial'),
]
