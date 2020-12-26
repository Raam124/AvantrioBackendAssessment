from django.shortcuts import render

from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated 

from rest_framework import permissions
from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveAPIView

from rest_framework import generics, mixins, permissions

from .serializers import UserSerializer,UserAccountUpdateSerializer,JobSerializer

from django.contrib.auth.models import User


# custom permission class
from account.permissions import UserIsOwnerOrReadOnly


# testing welcome view for all the authnticated users
class HelloView(APIView): 
    permission_classes = (IsAuthenticated, ) 
  
    def get(self, request): 
        content = {'message': 'Hello,Welcome to Aviantrio Interview SaaS'} 
        return Response(content) 


class CreateUserView(CreateAPIView):

    model = User
    permission_classes = [
        permissions.AllowAny 
    ]
    serializer_class = UserSerializer



class UserAccountChangeAPIView(generics.RetrieveAPIView,
                               mixins.DestroyModelMixin,
                               mixins.UpdateModelMixin):

    # custom permission class for only owner can edit his profile                         
    permission_classes = (
        permissions.IsAuthenticated,
        UserIsOwnerOrReadOnly,

    )
    serializer_class = UserAccountUpdateSerializer

    def get_object(self):
        username = self.kwargs["username"]
        obj = get_object_or_404(User, username=username)
        return obj

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

