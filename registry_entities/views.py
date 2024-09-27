from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Department, Division, Sector, Organization
from .serializers import OrganizationModelSerializer, DivisionModelSerializer, SectorModelSerializer, DepartmentModelSerializer
from core.permissions import GlobalPermissionClass, GlobalUserObjectPermission
# Create your views here.


class OrganizationListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Organization.objects.all()
    serializer_class = OrganizationModelSerializer


class OrganizationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalUserObjectPermission)
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
    permission_classes = (IsAuthenticated)
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer


class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalUserObjectPermission)
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer
