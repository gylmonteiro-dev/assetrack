from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("registry_entities.urls")),
    path("api/v1/", include("management_patrimony.urls")),
    path("api/v1/", include("authentication.urls")),
]
