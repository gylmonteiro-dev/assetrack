from rest_framework import generics
from .models import Department, Division, Sector, Organization
from .serializers import OrganizationModelSerializer
# Create your views here.


class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationModelSerializer