from django.urls import path
from usuarios.views import login, cadastro
from galeria.views import index,imagem, buscar

urlpatterns = [
    path('login', login, name = 'login'),
    path('cadastro', cadastro, name = 'cadastro'),
    path('', index, name = 'home'),
    
]