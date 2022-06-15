from functools import partial
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from yaml import serialize

from .models import Student
from .serializers import StudentSerializer
# Create your views here.

class StudentApi(APIView):

    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(pk=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)


    def post(self,request,format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data is created'})


    def put(self,request,pk,format=None):
        id = pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data is updated'})        


    def delete(self,request,pk,format=None):
        id = pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data is deleted'})  
       
                    