from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import PostCreateForm
from .models import Post

# Create your views here.
def blog_home_view(request, *args, **kwargs):
    obj = Post.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "blog.html", context)

@login_required(login_url='/admin/login/')
def post_create_view(request, *args, **kwargs):
    form = PostCreateForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        form = PostCreateForm()

    context = {
        'form': form,
    }
    return render(request, "new.html", context)

def post_edit_view(request, *args, **kwargs):
    return render(request, "edit.html", {})