from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Department, Division, Sector, Organization
from .serializers import OrganizationModelSerializer, DivisionModelSerializer, SectorModelSerializer, SectorListSerializer, DepartmentModelSerializer
from core.permissions import GlobalPermissionClass
# Create your views here.


class OrganizationListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Organization.objects.all()
    serializer_class = OrganizationModelSerializer


class OrganizationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Organization.objects.all()
    serializer_class = OrganizationModelSerializer


class DivisionListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Division.objects.all()
    serializer_class = DivisionModelSerializer


class DivisionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Division.objects.all()
    serializer_class = DivisionModelSerializer


class SectorListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Sector.objects.all()
    # serializer_class = SectorModelSerializer

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return SectorListSerializer
        return SectorModelSerializer


class SectorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Sector.objects.all()
    serializer_class = SectorModelSerializer


class DepartmentListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer


class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer
