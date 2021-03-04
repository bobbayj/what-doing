from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Welcome to Bob's Blog</h1>")
    return render(request, "home.html", {})