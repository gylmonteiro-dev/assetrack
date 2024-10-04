from rest_framework import serializers
from .models import Asset, Category, CostCenter, RegisterAsset, Supplier


class AssetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = "__all__"


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CostCenterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = "__all__"


class RegisterAssetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterAsset
        fields = "__all__"


class SupplierModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
