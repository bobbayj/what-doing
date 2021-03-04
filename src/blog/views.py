from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
def main_blog_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Bob's Blog Posts</h1>")
    return render(request, "blog.html", {})