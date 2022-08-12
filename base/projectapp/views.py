from django.http import HttpResponse
from django.shortcuts import render

from projectapp.models import Category,Project

# Create your views here.

def projectpage(request,pk):
    object = Category.objects.get(pk=pk)
    ongoingProjects = object.project_set.all().filter(project_status='Ongoing')
    upcomingProjects = object.project_set.all().filter(project_status='Upcoming')
    complatedProjects = object.project_set.all().filter(project_status='Complated')
    context={
       'object':object,
       'ongoingProjects':ongoingProjects,
       'upcomingProjects':upcomingProjects,
       'complatedProjects':complatedProjects 
    }
    return render(request,'projectapp/category_details.html',context) 

def projectdetails(request,pk):
    details =Project.objects.get(pk=pk)
    return render(request,'projectapp/projectDetails.html',{'details':details}) 

