from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki', views.search, name='search'),
    path("wiki/new", views.new, name="new"),

    path("wiki/<str:title>", views.article, name="article"),
]
