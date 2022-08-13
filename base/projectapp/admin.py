from django.contrib import admin
from projectapp.models import Category,Project,ProjectImages

from mptt.admin import MPTTModelAdmin

# Register your models here.

admin.site.register(Category, MPTTModelAdmin)


class Projectlist(admin.ModelAdmin):
    list_display = ('name','categories','image_tag','project_status','location')
admin.site.register(Project,Projectlist)

