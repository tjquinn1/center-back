from django.shortcuts import render
from .models import Client, Project, Task, Time
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ClientSerializer, ProjectSerializer, TaskSerializer, TimeSerializer, TimePostSerializer
# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save(account_owner=self.request.user)

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TimeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    filter_fields = ('created',)

class TimePostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Time.objects.all()
    serializer_class = TimePostSerializer
