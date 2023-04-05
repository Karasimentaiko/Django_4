from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('upload/', views.upload, name='upload'),
    path('success/', views.success, name='success'),
]
