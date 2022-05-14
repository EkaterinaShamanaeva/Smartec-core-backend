import uuid

from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import User
from app.validator import Validator

# Create your views here.
class UsersHandler(APIView):
    request = False
    def get(self, request):
        output_data = User.objects.all().values()
        return Response({output_data})

    def post(self, request):
        self.request = Validator(request.data)
        response = 'User has been added'
        if self.request.valid():
            User.objects.create(
                name=request.data['name'],
                email=request.data['email'],
                password=request.data['password'],
                uuid=uuid.uuid4()
            )
        else:
            response = 'Error: incorrect fields count'
        return Response(response)
