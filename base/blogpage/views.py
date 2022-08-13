from django.shortcuts import redirect, render,get_object_or_404
from blogpage.models import Blog,Comment
# from servicepage.models import Category,Service

def blog(request):
    blogs = Blog.objects.all()
    latest_blogs = Blog.objects.all().order_by('-post_date')[:3]
    # category = Category.objects.all()
    return render(request,'blogpage/blogs.html',{'blogs':blogs,'latest_blogs':latest_blogs})

def blog_details(request,pk):
    object = Blog.objects.get(pk=pk)
    latest_blogs = Blog.objects.all().order_by('-post_date')[:3]
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        text = request.POST.get("text")
        Comment.objects.create(text=text,post=object)
        return redirect("blogpage:blog_details",pk=post.pk)
    comments=Comment.objects.filter(post=post)
    # category = Category.objects.all()
    
    return render(request,'blogpage/blog_details.html',{'object':object,'latest_blogs':latest_blogs,
    'comments':comments})


