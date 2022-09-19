
from django.db import models
from django.urls import reverse

from django.utils.html import mark_safe
from django.conf import settings

from mptt.models import MPTTModel, TreeForeignKey
from homeapp.compress import compress

class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    image=models.ImageField(upload_to='category_img', blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return str(self.name) 

        
    def get_absolute_url(self):
        return reverse('homeapp:categorypage', kwargs={'pk':self.pk})



class Project(models.Model):
    CATEGORY_CHOICES = (
    ("Ongoing", "Ongoing"),
    ("Upcoming", "Upcoming"),
    ("Completed", "Completed"),
    )

    name = models.CharField(max_length=200,help_text="name of the project")
    categories = models.ForeignKey(Category,on_delete=models.CASCADE,help_text="name of the project category")
    project_status = models.CharField(choices=CATEGORY_CHOICES,max_length=10)
    thumnail_image = models.ImageField(upload_to='project_img-thumnails')
    location = models.TextField(null=True,blank=True,help_text="write loaction about your project")
    apartment_type = models.TextField(max_length=500,null=True,blank=True,
    help_text="type of apartments -->example:12 storey luxury 4 bedroom apartments")
    availability= models.CharField(null=True,blank=True,max_length=200,help_text="Sale complete/or not")
    apartment_size = models.IntegerField(null=True,blank=True,help_text='apartment_size in sft')
    total_apartments = models.IntegerField(null=True,blank=True,help_text='how many apartment--->example:20/10 etc')


    def save(self, *args, **kwargs):
        # call the compress function
        new_image = compress(self.thumnail_image)
        # set self.image to new_image
        self.thumnail_image = new_image
        # save
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    def image_tag(self):
        if self.thumnail_image != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.thumnail_image))

class ProjectImages(models.Model): 
    case = models.ForeignKey(Project,on_delete=models.CASCADE,null=True,blank=True)
    images = models.ImageField(upload_to="file_upload", null = True, blank = True,help_text='upload images for project')
    text = models.CharField(max_length=255,help_text='text must be in 255 character')

