from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import authenticate
from .models import User_new
from .serializers import UserSerializer , LoginSerializer, RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = User_new.objects.all()
        data_serializer = UserSerializer(data , many = True)
        return Response(data_serializer.data)

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User_new.objects.all()
    serializer_class = RegisterSerializer
    
class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request ,email=email , password=password)
        if user is not None:
            token = RefreshToken.for_user(user)
            detail = UserSerializer(user)
            return Response({
                "refresh": str(token),
                "access": str(token.access_token),
                "user": detail.data
            })
        else:
            return Response({"error": "Invalid credentials"}, status=400)
