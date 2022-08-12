from django.urls import path
from . import views

app_name='homeapp'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact/', views.contactpage, name='contactpage'), 
    path('biswasTextile/', views.biswasTextile, name='biswasTextilepage'), 
    path('biswasMaterials/', views.biswasMaterials, name='biswasMaterialspage'), 
    path('biswasDeveloper/', views.biswasDeveloper, name='biswasDeveloperpage'),
    path('biswasExportimport/', views.biswasExportimport, name='biswasExportimportpage'), 
    path('biswasGarments/', views.biswasGarments, name='biswasGarmentspage'), 
    path('biswasConsultant/', views.biswasConsultant, name='biswasConsultantpage'),  

    path('Landwanted/', views.Landwanted, name='Landwantedpage'), 
    path('customerReviews/', views.customerReviews, name='customerReviewspage'), 
    path('careerOpportunity/', views.careerOpportunity, name='careerOpportunitypage'), 
    path('visionMission/', views.visionMission, name='visionMissionpage'), 
    path('affiliation/', views.affiliation, name='affiliationpage'), 
    path('award/', views.award, name='awardpage'), 
    path('certification/', views.certification, name='certificationpage'), 
    path('corporateStructure/', views.corporateStructure, name='corporateStructurepage'), 
    path('companyProfile/', views.companyProfile, name='companyProfilepage'), 
    path('team/', views.team, name='teampage'),  


    path('events/', views.event, name='eventpage'), 
]
