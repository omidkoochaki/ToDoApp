from django.db.models import Q
from rest_framework import permissions

from rest_framework.viewsets import ModelViewSet

from projects.models import Project, Task
from projects.permissions import TaskPermission, ProjectPermission
from projects.serializers import ProjectSerializer, ProjectDetailSerializer, TaskSerializer


class ProjectsViewSet(ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
        ProjectPermission,
    ]

    def get_queryset(self):
        query = Q(manager=self.request.user) | Q(developers=self.request.user)
        return Project.objects.select_related().filter(query)

    def get_serializer_class(self):
        if self.action == 'create':
            return ProjectSerializer
        else:
            return ProjectDetailSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer

    permission_classes = [
        permissions.IsAuthenticated,
        TaskPermission,
    ]

    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)
        request.data.update({
            'project': Project.objects.get(id=kwargs.get('project_id'))
        })
        return request

    def get_queryset(self):

        project_id = self.kwargs.get('project_id')

        return Task.objects.filter(project__id=project_id)
