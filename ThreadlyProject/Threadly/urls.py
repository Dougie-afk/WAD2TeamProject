from django.urls import include
from django.urls import path
from Threadly import views
app_name= 'Threadly'
urlpatterns = [
    path('', views.base, name='base'),
    path('index/',views.index,name='index'),
    
    
    
]