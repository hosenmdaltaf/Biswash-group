
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from django.conf import settings

 
class Blog(models.Model):
    title = models.CharField(max_length=255)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateField(auto_now=True)
    image=models.ImageField(upload_to='blog_images', blank=True, null=True)
    # category = models.ForeignKey('Category',on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.title)
 
    def image_tag(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.image))

    
class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(blank=True, null=True )
    created_date = models.DateTimeField(auto_now_add=True)

    def all_comments(self):
        return self.comment_set.all()

    @property
    def totat_comments_count(self):
        return self.comment_set.all().count()

    # def __str__(self):
    #     return str(self.title)

        




