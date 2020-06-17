from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date
# Create your views here.

def home(request):
    return render(request, 'api/home.html')

@api_view(['GET'])
def view_task(request):
    entered_date = request.GET[str('date')]
    if entered_date == str(date.today()):
        context = {'task':'your task'}
        return Response(context, status=status.HTTP_200_OK )
    else:
        context = {'Error':'Date not matched'}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ping(request):
    return Response(status=status.HTTP_200_OK)


