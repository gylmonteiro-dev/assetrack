from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from .models import Asset, Category, CostCenter, RegisterAsset, Supplier
# Create your views here.


class AssetListCreateView(ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class  = None


class AssetRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = None


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = None


class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = None


class CostCenterListCreateView(ListCreateAPIView):
    queryset = CostCenter.objects.all()
    serializer_class = None


class CostCenterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CostCenter.objects.all()
    serializer_class = None


class RegisterAssetListCreateView(ListCreateAPIView):
    queryset = RegisterAsset.objects.all()
    serializer_class = None


class RegisterAssetRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = RegisterAsset.objects.all()
    serializer_class = None


class SupplierAssetListCreateView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = None


class SupplierRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = None
