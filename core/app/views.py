from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import User
from django.shortcuts import render


# Create your views here.
class UsersHandler(APIView):
    def get(self, request):
        output_data = User.objects.all().values()
        return Response({output_data})
