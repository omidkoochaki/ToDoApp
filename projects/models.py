from django.db import models

from core.models import BaseModel
from projects.helpers import TaskStatusChoices
from users.models import User


class Project(BaseModel):
    title = models.CharField(max_length=254, blank=False, null=False)
    manager = models.ForeignKey(User, related_name='projects', on_delete=models.PROTECT)
    budget = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    developers = models.ManyToManyField(User, related_name='developer_in_projects')

    class Meta:
        unique_together = ('manager', 'title',)


class Task(BaseModel):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=254, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    developers = models.ManyToManyField(User, related_name='tasks')
    deadline = models.DateTimeField(null=True, blank=True)
    acceptance_criteria = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=5,
                              choices=TaskStatusChoices.choices,
                              default=TaskStatusChoices.TODO)

    class Meta:
        unique_together = ('project', 'title',)
