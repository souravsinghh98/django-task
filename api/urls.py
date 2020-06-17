from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('task/', views.view_task, name='task'),
    path('ping/', views.ping, name='ping'),

]