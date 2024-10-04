from django.db.models import Avg, Count, F
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalPermissionClass
from .models import Asset, Category, CostCenter, RegisterAsset, Supplier
from .serializers import AssetModelSerializer, CategoryModelSerializer, CostCenterModelSerializer, RegisterAssetModelSerializer, SupplierModelSerializer
# Create your views here.


class AssetListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Asset.objects.all()
    serializer_class  = AssetModelSerializer


class AssetRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Asset.objects.all()
    serializer_class = AssetModelSerializer


class AssetStatisticsView(APIView):
    # permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Asset.objects.all()

    def get (self, request):
        average_price = self.queryset.aggregate(Avg('price'))['price__avg']
        category_counts = self.queryset.values(category_counts=F("category__name")).annotate(
            count=Count("id")
        )
        print(self.queryset.values("category__name"))
        most_expensive = self.queryset.order_by('-price').first().name

        data = {'average_price': average_price,
                'category_counts': category_counts,
                'most_expensive': most_expensive
                }
        return Response(data)

class CategoryListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class CostCenterListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = CostCenter.objects.all()
    serializer_class = CostCenterModelSerializer


class CostCenterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = CostCenter.objects.all()
    serializer_class = CostCenterModelSerializer


class RegisterAssetListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = RegisterAsset.objects.all()
    serializer_class = RegisterAssetModelSerializer


class RegisterAssetRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = RegisterAsset.objects.all()
    serializer_class = RegisterAssetModelSerializer


class SupplierListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Supplier.objects.all()
    serializer_class = SupplierModelSerializer


class SupplierRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Supplier.objects.all()
    serializer_class = SupplierModelSerializer
