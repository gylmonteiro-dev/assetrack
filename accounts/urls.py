from django.urls import path
from . import views


urlpatterns = [
    path("users/", views.UserCreateApiView.as_view(), name="create-user"),
    path("user_profile/", views.ProfileUserListView.as_view(), name="get-profile"),
    path(
        "user_profile/<int:pk>/",
        views.UserProfileRetrieveUpdateDestroyView.as_view(),
        name="retrieve-update-delete-user_profile",
    ),
]
