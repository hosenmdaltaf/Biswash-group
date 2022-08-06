from django.urls import path
from . import views

app_name='projectapp'

urlpatterns = [
    path('cat/<int:pk>/', views.projectpage, name='catDetailspage'),
    path('status/<int:pk>/', views.project_status_filter, name='project_statuspage'),  
    
]