from django.shortcuts import render
from projectapp.models import Category
from homeapp.models import Contact,Career

# Create your views here.

def homepage(request):
    projects_cat = Category.objects.all()
    
    context ={
        'projects_cat':projects_cat
    }
    return render(request,'homeapp/index.html',context) 


def contactpage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        email = request.POST.get("email")
        Contact.objects.create(name=name,message=message,email=email,)
        return render(request,'global/thankyou.html')
    return render(request,'homeapp/contact.html') 



def biswasTextile(request):
    return render(request,'homeapp/biswastextile.html') 

def biswasMaterials(request):
    return render(request,'homeapp/biswasmaterial.html') 

def biswasDeveloper(request):
    return render(request,'homeapp/biswasdeveloper.html') 

def biswasExportimport(request):
    return render(request,'homeapp/biswasexportimport.html') 

def biswasGarments(request):
    return render(request,'homeapp/biswasgarments.html') 

def biswasConsultant(request):
    return render(request,'homeapp/biswasconsultant.html') 



def Landwanted(request):
    return render(request,'homeapp/Landwanted.html') 

def customerReviews(request):
    return render(request,'homeapp/CustomerReview.html') 
   
def careerOpportunity(request):
    if request.method=="POST":
        name = request.POST.get("name")
        position = request.POST.get("PositionName")
        email = request.POST.get("email")
        phone = request.POST.get('number')
        message = request.POST.get("message")
        file = request.POST.get("file")
        Career.objects.create(name=name,message=message,email=email,position=position,phone=phone,file=file)
        return render(request,'global/thankyou.html')

    return render(request,'homeapp/Careeropportunity.html') 

def visionMission(request):
    return render(request,'homeapp/Vision&Mission.html') 

def affiliation(request):
    return render(request,'homeapp/Affiliation.html') 

def award(request):
    return render(request,'homeapp/Award.html') 

def certification(request):
    return render(request,'homeapp/Certifecate.html') 

def corporateStructure(request):
    return render(request,'homeapp/CorporateStructure.html') 

def companyProfile(request):
    return render(request,'homeapp/CompanProfile.html') 

def team(request):
    return render(request,'homeapp/team.html') 




def event(request):
    return render(request,'homeapp/Event.html') 