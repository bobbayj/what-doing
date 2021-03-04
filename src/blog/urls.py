from django.urls import path

from .views import main_blog_view

urlpatterns = [
    path('', main_blog_view, name='main_blog')
]