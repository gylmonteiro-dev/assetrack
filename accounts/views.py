from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
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
        queryset = UserProfile.objects.filter(user=user)
        return queryset
    

class ProfileUserListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializar

    def get_queryset(self):
        user = self.request.user
        print(user)
        queryset = UserProfile.objects.filter(user=user)
        return queryset
