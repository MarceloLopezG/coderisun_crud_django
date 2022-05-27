from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from users.forms import UserForm
from django.http import JsonResponse

class RegisterUsers(APIView):
    #Create
    def post(self, request, format=None):
        register = UserForm(data=request.data)

        if register.is_valid():
            user = register.save()
            pw = user.password
            user.set_password(pw)
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST) 

class UserDetails(APIView):
    permission_classes = (IsAuthenticated, AllowAny)
    #Index
    def get(self, request, id, format=None, *args, **kwargs):
        user = User.objects.get(pk=id)
        userinformation = [{ 'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email }]
        return JsonResponse(userinformation, safe=False)


    #Update
    def put(self, request, id, *args, **kwargs):
        user = User.objects.get(pk=id)
        updateUser = UserForm(request.data, instance=user)

        if updateUser.is_valid():
            user = updateUser.save()
            pw = user.password
            user.set_password(pw)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, id):
        user = User.objects.get(pk=id)
        user.delete()
        return Response(status=status.HTTP_200_OK)
