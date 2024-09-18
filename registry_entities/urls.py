from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("organizacoes/", ..., name="list-create-organizations"),
    path("organizacoes/<int:pk>", ..., name="retrieve-update-destroy-organization"),

    path("departments/", ..., name="list-create-departments"),
    path("departments/<int:pk>", ..., name="retrieve-update-destroy-departments"),

    path("divisions/", ..., name="list-create-divisions"),
    path("divisions/<int:pk>", ..., name="retrieve-update-destroy-divisions"),
    
    path("sectors/", ..., name="list-create-sectors"),
    path("sectors/<int:pk>", ..., name="retrieve-update-destroy-sectors"),
]
