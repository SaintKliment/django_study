from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    # path('news', views.news),
    # path('part', views.part)
]
