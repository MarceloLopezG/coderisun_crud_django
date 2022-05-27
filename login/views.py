from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

class Login(ObtainAuthToken):    
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        username =  User.objects.get(email=email)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'token': token.key,
                'pk':user.pk,
                }) 
    

class Logout(APIView):
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
