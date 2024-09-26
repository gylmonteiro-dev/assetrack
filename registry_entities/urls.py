from django.urls import path
from . import views

urlpatterns = [
    path("organizations/", views.OrganizationListCreateView.as_view(), name="list-create-organizations"),
    path("organizations/<int:pk>/", views.OrganizationRetrieveUpdateDestroyView.as_view(), name="retrieve-update-destroy-organization"),

    path("departments/", views.DepartmentListCreateView.as_view(), name="list-create-departments"),
    path("departments/<int:pk>/", views.DepartmentRetrieveUpdateDestroyView.as_view(), name="retrieve-update-destroy-departments"),

    path("divisions/", views.DivisionListCreateView.as_view(), name="list-create-divisions"),
    path("divisions/<int:pk>/", views.DivisionRetrieveUpdateDestroyView.as_view(), name="retrieve-update-destroy-divisions"),

    path("sectors/", views.SectorListCreateView.as_view(), name="list-create-sectors"),
    path("sectors/<int:pk>/", views.SectorRetrieveUpdateDestroyView.as_view(), name="retrieve-update-destroy-sectors"),
]
