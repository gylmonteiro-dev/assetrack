from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Asset, Category, CostCenter, RegisterAsset, Supplier
from .serializers import AssetModelSerializer, CategoryModelSerializer, CostCenterModelSerializer, RegisterAssetModelSerializer, SupplierModelSerializer
# Create your views here.


class AssetListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Asset.objects.all()
    serializer_class  = AssetModelSerializer


class AssetRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Asset.objects.all()
    serializer_class = AssetModelSerializer


class CategoryListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class CostCenterListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CostCenter.objects.all()
    serializer_class = CostCenterModelSerializer


class CostCenterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CostCenter.objects.all()
    serializer_class = CostCenterModelSerializer


class RegisterAssetListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = RegisterAsset.objects.all()
    serializer_class = RegisterAssetModelSerializer


class RegisterAssetRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = RegisterAsset.objects.all()
    serializer_class = RegisterAssetModelSerializer


class SupplierListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Supplier.objects.all()
    serializer_class = SupplierModelSerializer


class SupplierRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Supplier.objects.all()
    serializer_class = SupplierModelSerializer
