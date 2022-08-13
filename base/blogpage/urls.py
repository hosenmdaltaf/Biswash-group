from django.urls import path
from . import views

app_name='blogpage'

urlpatterns = [ 
    path('', views.blog, name='blog'),
    path('blog_details/<int:pk>', views.blog_details, name='blog_details'),
]