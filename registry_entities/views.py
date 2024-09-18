from rest_framework import generics
from .models import Department, Division, Sector, Organization
from .serializers import OrganizationModelSerializer, DivisionModelSerializer, SectorModelSerializer, DepartmentModelSerializer
# Create your views here.


class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationModelSerializer


class OrganizationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationModelSerializer


class DivisionListCreateView(generics.ListCreateAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionModelSerializer


class DivisionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionModelSerializer


class SectorListCreateView(generics.ListCreateAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorModelSerializer


class SectorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorModelSerializer


class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer


class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer
