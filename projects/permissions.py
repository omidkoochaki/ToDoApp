from rest_framework.permissions import BasePermission


class TaskPermission(BasePermission):
    def has_permission(self, request, view):

        project = request.data.get('project')
        project_developers = project.developers.all()

        return (project.manager == request.user) or (request.user in project_developers)


class ProjectPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user.is_manager
        else:
            return True

