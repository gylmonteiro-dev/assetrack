from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserCreateApiView.as_view(), name='create-user'),
]
