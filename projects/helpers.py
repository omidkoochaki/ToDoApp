from django.db import models


class TaskStatusChoices(models.TextChoices):
    TODO = 'TODO'
    DOING = 'DOING'
    DONE = 'DONE'
