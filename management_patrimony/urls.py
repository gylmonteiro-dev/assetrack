from django. urls import path
from . import views


urlpatterns = [
    path('assets/', views.AssetListCreateView.as_view(), name='list-create-asserts'),
    path('assets/<int:pk>/', views.AssetRetrieveUpdateDestroyView.as_view(), name='retrieve-update-destroy-asset'),
    path('assets/statistics/', views.AssetStatisticsView.as_view(), name='data-statistics'),
    
    path('categorys/', views.CategoryListCreateView.as_view(), name='list-create-categorys'),
    path('categorys/<int:pk>', views.CategoryRetrieveUpdateDestroyView.as_view(), name='retrieve-update-destroy-category'),

    path('cost_centers/', views.CostCenterListCreateView.as_view(), name='list-create-cost_centers'),
    path('cost_centers/<int:pk>', views.CostCenterRetrieveUpdateDestroyView.as_view(), name='retrieve-update-destroy-cost_center'),

    path('register_assets/', views.RegisterAssetListCreateView.as_view(), name='list-create-register_assets'),
    path('register_assets/<int:pk>', views.RegisterAssetRetrieveUpdateDestroyView.as_view(), name='retrieve-update-destroy-register_asset'),

    path('suppliers/', views.SupplierListCreateView.as_view(), name='list-create-suppliers'),
    path('suppliers/<int:pk>', views.SupplierRetrieveUpdateDestroyView.as_view(), name='retrieve-update-destroy-suppliers'),
]
