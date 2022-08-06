from django.shortcuts import render

from projectapp.models import Category

# Create your views here.

def homepage(request):
    projects_cat = Category.objects.all()
    
    context ={
        'projects_cat':projects_cat
    }
    return render(request,'homeapp/index.html',context) 