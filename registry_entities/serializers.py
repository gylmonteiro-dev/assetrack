from rest_framework import serializers
from .models import Organization, Division, Sector, Department


class OrganizationModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'


class DivisionModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Division
        fields = '__all__'


class DepartmentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class SectorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = '__all__'
