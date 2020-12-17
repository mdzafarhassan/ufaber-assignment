from rest_framework import serializers
from project.models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'duration',
                  'avatar', 'created_date', 'is_active']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'project', 'name', 'description', 'start_date',
                  'end_date', 'created_date', 'is_active']
