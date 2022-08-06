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

def project_status_filter(request,pk):
    all_projects = Project.objects.all()
    print(all_projects)

    # object = Category.objects.get(pk=pk)
    # projects=object.project.filter(project_status="Ongoing")

    category = Category.objects.get(pk=pk)
    projects = category.project_set.all().filter(project_status='Ongoing')
    print(projects)

    return render(request,'projectapp/project_status.html',{'projects':projects,'all_projects':all_projects}) 




# def gallery(request):

#     category = request.GET.get('category')
#     if category == None:
#          gallerys = Project.objects.select_related('categorys').all()

#     else:
#          gallerys = Gallery.objects.filter(categorys__name=category)

#     categories = Category.objects.all() 
#     return render(request,'homeapp/gallery.html',{'gallerys':page_obj,'categories':categories})

#     if project.object.filter(cat=category)

   