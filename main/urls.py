from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="main-home"),
    path('blog/', views.blog, name="main-blog"),
    path('about/', views.about, name="main-about"),
]
