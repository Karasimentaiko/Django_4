from django.urls import path, include
from . import views

urlpatterns = [
    path('video/', include('video.urls')),
    path('', views.index, name="index"),
    path('frontpage/', views.frontpage, name='frontpage'),

    path('create/', views.post_create, name="post_create"),
    path('<int:pk>/', views.post_detail, name="post_detail"),
    path('<int:pk>/post_Change_Delete', views.post_Change_Delete,
         name="post_Change_Delete"),
]
