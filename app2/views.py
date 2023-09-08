from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def Home(request):
    data = {
        "name": "ruban",
        "gender": "male",
        "project_name": "PROJECT 2"
    }

    return Response(data, status=status.HTTP_200_OK)