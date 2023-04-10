from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('upload/', views.upload, name='upload'),
    path('success/', views.success, name='success'),
    # path('blog/', include('blog.urls')),
]
