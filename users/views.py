from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from users.forms import UserForm
from django.http import JsonResponse
import hashlib



class RegisterUsers(APIView):
    #Create
    def post(self, request, format=None):
        datas = request.data

        email = datas['email']
        username = hashlib.md5(email.encode()).hexdigest()
        first_name = datas['first_name']
        last_name = datas['last_name']
        password = datas['password']

        new_data = {'username': str(username),'first_name': first_name,'last_name': last_name,'email':email,'password': password}
        register = UserForm(data=new_data)

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
    def get(self, request, username, *args, **kwargs):
        user = User.objects.get(username=username)
        userinformation = [{ 'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email }]
        return JsonResponse(userinformation, safe=False)



    #Update
    def put(self, request, username, *args, **kwargs):
        datas = request.data
        email = datas['email']
        first_name = datas['first_name']
        last_name = datas['last_name']
        password = datas['password']

        user = User.objects.get(username=username)
        
        if username == user.username:
            new_data = {'username': user.username,'first_name': first_name,'last_name': last_name,'email':email,'password': password}
        else:
            username = hashlib.md5(email.encode()).hexdigest()
            new_data = {'username': str(username),'first_name': first_name,'last_name': last_name,'email':email,'password': password}

        updateUser = UserForm(new_data, instance=user)
        if updateUser.is_valid():
            user = updateUser.save()
            pw = user.password
            user.set_password(pw)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, username):
        user = User.objects.get(username=username)
        user.delete()
        return Response(status=status.HTTP_200_OK)