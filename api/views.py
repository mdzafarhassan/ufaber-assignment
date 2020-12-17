from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from project.models import Project, Task
from api.serializers import ProjectSerializer, TaskSerializer
from django.contrib.auth.models import auth, User

# NEED TO ADD AUTHENTICATIONS


@api_view(('GET',))
def project_all(request):
    project_obj = Project.objects.all()
    serializer = ProjectSerializer(project_obj, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def project_detail(request, **kwargs):
    project_id = kwargs.get('project_id', None)

    try:
        project_obj = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProjectSerializer(project_obj)

    return Response(serializer.data)


@api_view(('PUT',))
def project_update(request, **kwargs):
    project_id = kwargs.get('project_id', None)

    try:
        project_obj = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = ProjectSerializer(project_obj, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["sucsess"] = "Project Info Updated."
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
def project_delete(request, **kwargs):
    project_id = kwargs.get('project_id', None)

    try:
        project_obj = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        deletion = project_obj.delete()
        data = {}
        if deletion:
            data["sucsess"] = "Project Deleted Successfully."
        else:
            data["fail"] = "Error while delete."
        return Response(data=data)


@api_view(('POST',))
def project_create(request):
    # account = User.objects.get(pk=1)
    print("Called")

    project_obj = Project()

    if request.method == "POST":
        serializer = ProjectSerializer(project_obj, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
def task_all(request, **kwargs):
    project_id = kwargs.get('project_id')
    if project_id:
        task_obj = Task.objects.filter(project_id=project_id)
    else:
        task_obj = Task.objects.all()
    serializer = TaskSerializer(task_obj, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def task_detail(request, **kwargs):
    project_id = kwargs.get('project_id', None)
    task_id = kwargs.get('task_id', None)

    try:
        task_obj = Task.objects.get(id=task_id, project=project_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task_obj)

    return Response(serializer.data)


@api_view(('PUT',))
def task_update(request, **kwargs):
    project_id = kwargs.get('project_id', None)
    task_id = kwargs.get('task_id', None)

    try:
        task_obj = Task.objects.get(id=task_id, project=project_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = TaskSerializer(task_obj, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["sucsess"] = "Task Info Updated."
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
def task_delete(request, **kwargs):
    project_id = kwargs.get('project_id', None)
    task_id = kwargs.get('task_id', None)

    try:
        task_obj = Task.objects.get(id=task_id, project=project_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        deletion = task_obj.delete()
        data = {}
        if deletion:
            data["sucsess"] = "Task Deleted Successfully."
        else:
            data["fail"] = "Error while delete."
        return Response(data=data)


@api_view(('POST',))
def task_create(request, **kwargs):
    project_id = kwargs.get('project_id', None)
    task_obj = Task(project_id=project_id)

    if request.method == "POST":
        serializer = TaskSerializer(task_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
