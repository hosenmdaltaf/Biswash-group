from django.contrib import admin
from .models import Blog,Comment
from django_summernote.admin import SummernoteModelAdmin
class Bloglist(SummernoteModelAdmin):
    list_display = ('title','writer','post_date','image_tag')
    summernote_fields = ('content',)
admin.site.register(Blog,Bloglist)


admin.site.register(Comment) 


