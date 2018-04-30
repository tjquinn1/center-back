from rest_framework import serializers
from .models import Client, Project, Task, Time

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('id','url','account_owner', 'name', 'start_date', 'end_date', 'notes')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    client = ClientSerializer(many=False, read_only=True)
    class Meta:
        model = Project
        fields = ('id','url', 'client', 'project_name', 'start_date', 'end_date')

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    project = ProjectSerializer(many=False, read_only=True)
    class Meta:
        model = Task
        fields = ('id','url', 'project', 'task_name')

class TimeSerializer(serializers.HyperlinkedModelSerializer):
    task = TaskSerializer(many=False, read_only=True)
    class Meta:
        model = Time
        fields = ('id','url', 'task', 'time', 'non_billable', 'created')