from rest_framework import serializers

from projects.models import Project, Task
from users.models import User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'budget', 'developers']

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        validated_data.update({
            'manager': user
        })
        return super().create(validated_data)


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]


class ProjectDetailSerializer(serializers.ModelSerializer):
    manager = ProjectMemberSerializer(read_only=True)
    developers = ProjectMemberSerializer(many=True)

    class Meta:
        model = Project
        fields = ["id", "title", "budget", "description", "manager", "tasks", "developers"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "status", "description", "developers", "deadline", "acceptance_criteria"]

    def validate(self, attrs):
        request = self.context.get("request")
        project = request.data.get("project")
        attrs.update({
            "project": request.data.get("project")
        })
        project_developers = list(project.developers.all())
        user = request.user
        developers = attrs.get('developers')
        if user != project.manager:

            if user in project_developers and developers == [user]:
                pass
            else:
                raise serializers.ValidationError("ask manager to add you to the project as a developer and then you "
                                                  "can just assign task to yourself")
        else:
            available_developers = set(project_developers + developers)
            project.developers.set(available_developers)

        return super().validate(attrs)
