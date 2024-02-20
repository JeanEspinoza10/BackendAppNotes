from django.shortcuts import render
from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework import status
from .models import UserApp
from .serializers import UserSerializer,UserCreateSerializer


'''
View => Para el modelo de UserAPP
'''

class RegisterUserView(generics.GenericAPIView):
    serializer_class = UserCreateSerializer

    def post(self,request):
    
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


