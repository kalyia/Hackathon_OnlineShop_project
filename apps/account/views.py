from django.shortcuts import get_object_or_404
# from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import CustomUser
from .serializers import CustomAuthTokenSerializer, RegisterSerializer, ForgotSerializer
from .services.utils import send_activate_code, send_new_password
class LoginView(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
class RegisterView(APIView):
    def post(self, request):
        data = request.POST  # (email=adadsd@mail.ru, password =!@#!@$@)
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # serializer.validated_data #dict <---- is_valid()
        user: CustomUser = serializer.save()
        send_activate_code(user.activate_code, user.email)
        return Response(serializer.data)
class ActivateView(APIView):
    # http://127.0.0.1:8000/api/v1/account/activate/afghaffafsada
    def get(self, request, activate_code):
        user = get_object_or_404(CustomUser, activate_code=activate_code)
        user.is_active = True
        user.save()
        return Response("activated!")
    class LogoutAPIView(APIView):
        permission_classes = [IsAuthenticated, ]
        def get(self, request):
            user = request.user
            token = ObtainAuthToken.objects.get(user=user)
            token.delete()
            return Response('You are logged out', status=status.HTTP_401_UNAUTHORIZED)
class ForgotPasswordView(APIView):
    def post(self, request):
        data = request.POST
        serializer = ForgotSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        user: CustomUser = CustomUser.objects.get(email=email)
        new_password = user.generate_activation_code(10, 'qwertydfghjk543')
        user.set_password(new_password)  # lazy request
        user.save()
        send_new_password(email, new_password)
        return Response({'message': 'your new password we send your email'}, status=status.HTTP_200_OK)