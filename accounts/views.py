from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class UserCreateApiView(APIView):

    
    def post(self, request):
        username = request.data.get("username")
        print(username)
        return Response(data={'msg': 'teste'}, status=201)
