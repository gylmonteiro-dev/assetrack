from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from .serializers import UserModelSerializer, UserProfileSerializar
from .models import UserProfile


# Create your views here.
class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    
class UserProfileRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializar

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = UserProfile.objects.all()
        else: 
            queryset = UserProfile.objects.filter(user=user)
        return queryset
    
    def partial_update(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        if data.get('organization') and user.is_staff:
            return super().partial_update(request, *args, **kwargs)
        elif data.get('organization') or data.get('user'):
            raise PermissionDenied("Apenas administradores podem alterar a organização ou usuário")
        return super().partial_update(request, *args, **kwargs)

    

class ProfileUserListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializar

    def get_queryset(self):
        user = self.request.user
        print(user)
        queryset = UserProfile.objects.filter(user=user)
        return queryset


