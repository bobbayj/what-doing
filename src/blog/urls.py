from django.urls import path

from .views import blog_home_view, post_create_view, post_edit_view

urlpatterns = [
    path('', blog_home_view, name='main'), 
    path('new/', post_create_view, name='new'),
    path('edit/', post_edit_view, name='edit'),
]