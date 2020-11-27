from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
from tasks.models import Task
from django.core import serializers
from tasks.serializer import TaskSerializer


# Create your views here.
@api_view(["GET"])
def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


@api_view(["GET"])
def get_tasks(request):
    tasks = Task.objects.all()
    # HTTP response needs to return a json
    tasks_response = serializers.serialize("json", tasks)
    return HttpResponse(tasks_response, content_type="application/json")


@api_view(["POST"])
def post_task(request):
    data = JSONParser().parse(request)
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_tasks(request):
    tasks = Task.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)