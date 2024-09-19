from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from .models import Asset, Category, CostCenter, RegisterAsset, Supplier
from .serializers import AssetModelSerializer, CategoryModelSerializer, CostCenterModelSerializer, RegisterAssetModelSerializer, SupplierModelSerializer
# Create your views here.


class AssetListCreateView(ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class  = AssetModelSerializer


class AssetRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetModelSerializer


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class CostCenterListCreateView(ListCreateAPIView):
    queryset = CostCenter.objects.all()
    serializer_class = CostCenterModelSerializer


class CostCenterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CostCenter.objects.all()
    serializer_class = CostCenterModelSerializer


class RegisterAssetListCreateView(ListCreateAPIView):
    queryset = RegisterAsset.objects.all()
    serializer_class = RegisterAssetModelSerializer


class RegisterAssetRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = RegisterAsset.objects.all()
    serializer_class = RegisterAssetModelSerializer


class SupplierListCreateView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierModelSerializer


class SupplierRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierModelSerializer
