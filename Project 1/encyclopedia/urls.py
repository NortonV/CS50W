from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki', views.search, name='search'),
    path("new", views.new, name="new"),
    path("random", views.random_article, name="random_article"),
    path("edit/<str:title>", views.edit, name="edit"),

    path("wiki/<str:title>", views.article, name="article"),
]
