from django.urls import path
from . import views

app_name = 'bootstrap'

urlpatterns = [
    path('', views.index, name='bindex'),
    path('index/', views.index, name='bindex'),
    path('home/', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('post/', views.post, name='post'),
]
