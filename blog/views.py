from django.shortcuts import render

def blog(request):
    return render(request, "blog/blog.html")

def blog_details(request):
    return render(request, "blog/blog-details.html")