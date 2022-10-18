from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import ToDoListSerializer
from .models import ToDoList
# Create your views here.
def index(request):
    return HttpResponse("hello to do app")

class todoAPIview(APIView):
    def post(self,request):
        data=request.data 
        serializer=ToDoListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)
