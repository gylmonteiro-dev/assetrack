from rest_framework import serializers
from .models import Organization, Division, Sector, Department
from management_patrimony.models import RegisterAsset


class OrganizationModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = "__all__"


class DivisionModelSerializer(serializers.ModelSerializer):
    amount_assets = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Division
        fields = "__all__"

    def get_amount_assets(self, obj):
        sectors = obj.sectors.all()
        total_patrimony = 0
        for sector in sectors:
            assets = sector.registros_de_ativos.all()
            for asset in assets:
                total_patrimony += asset.asset.price
        return total_patrimony


class DepartmentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"


class SectorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = "__all__"


class SectorListSerializer(serializers.ModelSerializer):
    division = serializers.SerializerMethodField(read_only=True)
    # division_name = serializers.CharField(source="division.name")
    amount_assets = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Sector
        fields = ["id", "name", "division", "amount_assets"]

    def get_amount_assets(self, obj):
        # print(obj.registros_de_ativos.all().count())
        actives = RegisterAsset.objects.filter(sector=obj)
        dict_actives = [
            {
                "id": active.asset.id,
                "Ativo": active.asset.name,
                "Preço": active.asset.price,
            }
            for active in actives
        ]

        return dict_actives

    def get_division(self, obj):
        return {"id": obj.division.id, "name": obj.division.name}
