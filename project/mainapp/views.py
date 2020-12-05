from django.db import reset_queries
from django.db.models import query
from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import authentication, permissions
from .models import CustomUser, CustomUserSerializer, UserVerification
from .permissions import AgentPermission, GerantPermission 
from rest_framework import generics

# @api_view(['GET'])
# def TokenVerification(request,token):
#     token = UserVerification.objects.get(token=token)
#     _user=token.user 
#     _user.is_verified= True
#     _user.save()




class AgentViewRetrieveUpdate(generics.RetrieveUpdateAPIView):
    # authentication_classes = [BasicAuthentication]
    permission_classes = [GerantPermission | AgentPermission]
    queryset = CustomUser.objects.none
    serializer_class= CustomUserSerializer
    def retrieve(self, request,pk=None):
        """
        docstring
        """
        queryset=CustomUser.objects.get(pk=request.user.pk)
        
        user = CustomUser.objects.get(pk=request.user.pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    def update(self, request,pk=None):
        """
        docstring
        """
        queryset=CustomUser.objects.get(pk=request.user.pk)
        serializer = CustomUserSerializer
        return Response(request.data)

class AgentViewCreate(generics.CreateAPIView):
    permission_classes = [GerantPermission]
    queryset = CustomUser.objects.none
    serializer_class= CustomUserSerializer
    def create(self, request):
        """
        docstring
        """
        
        


class AgentViewDestroy(generics.DestroyAPIView):
    permission_classes = [GerantPermission]
    queryset = CustomUser.objects.all()
    serializer_class= CustomUserSerializer
    



