from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('index/', views.index, name='index'),
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
]