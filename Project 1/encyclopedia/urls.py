from django.urls import path
from django.views.generic import RedirectView
import random
from . import views, util

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.article, name="article"),
    path('wiki', views.search, name='search'),
]
