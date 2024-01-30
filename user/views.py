# user/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import CustomUser
from restapi import settings
import jwt
import datetime
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
           
             #serializer = serializer(username, many=True)
            token = RefreshToken.for_user(user)
           # data["tokens"] = 
            return Response({"username":str(username),"refresh": str(token), "access": str(token.access_token)}, status=status.HTTP_200_OK)
            

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



       
def generate_access_token(user):
    access_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=5),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
                              "asdfasdfasd@#$!!@#$safas#$@#$32!@#!@3", algorithm='HS256')
                            #   .decode('utf-8')
    return access_token



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_okcheck(request):
    if request.method == 'POST':
        return Response("Ok",  status=status.HTTP_200_OK)



@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def password_reset(request):
    if request.method == 'POST':
        u = request.user
        u.set_password(request.POST['password'])
        u.save() # Add this line
        return Response({'message':'Password Updated Successfully'}, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])
@permission_classes((IsAuthenticated, ))
def mobileNo_reset(request):
    if request.method == 'PATCH':
      user = request.user
      serializer = UserSerializer(user, data=request.data, partial=True)
      if serializer.is_valid():
         serializer.save()
         return Response({"status": "success", "data": serializer.data})
      else:
         return Response({"status": "error", "data": serializer.errors})


@api_view(['PATCH'])
@permission_classes((IsAuthenticated, ))
def email_reset(request):
    if request.method == 'PATCH':
      user = request.user
      serializer = UserSerializer(user, data=request.data, partial=True)
      if serializer.is_valid():
         serializer.save()
         return Response({"status": "success", "data": serializer.data})
      else:
         return Response({"status": "error", "data": serializer.errors})

