from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('authentication/', TokenObtainPairView.as_view(), name='obtain-token'),
    path('authentication/refresh_token/', TokenRefreshView.as_view(), name='refresh-token'),
    path('authentication/verify_token/', TokenVerifyView.as_view(), name='verify-token')
]
