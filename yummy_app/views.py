from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse , HttpResponse , JsonResponse
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@api_view(['GET'])
def chef(request):
   if request.method == 'GET':
      tableData = chef_table.objects.all()
      serializer = chef_tableSerializer(tableData, many=True)
      return JsonResponse(serializer.data , safe=False , status=200)
   
@api_view(['GET'])
def testimonial(request):
   if request.method == 'GET':
      tableData = testimonial_table.objects.all()
      serializer = testimonial_tableSerializer(tableData, many=True)
      return JsonResponse(serializer.data, safe=False, status=200)
   
   
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.data['username'])
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if not user.check_password(request.data['password']):
            return Response({"detail": "Password is wrong"}, status=status.HTTP_400_BAD_REQUEST)
        
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)
        return Response({'token': token.key, 'user': serializer.data})
   
@api_view(['POST'])
def signup(request):
   if(request.method == 'POST'):
      serializer = UserSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         user = User.objects.get(username=request.data['username'])
         user.set_password(request.data['password'])
         user.save()
         token  = Token.objects.create(user = user)
         return  Response({'token': token.key , 'user' : serializer.data})
      return  Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def test(request):
   return Response({"hello": " chutiya api chal rahi h "})

def home(request):
   return render(request, 'index.html')
   
   
