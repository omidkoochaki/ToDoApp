# Generated by Django 4.1.2 on 2022-10-12 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='developers',
            field=models.ManyToManyField(related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='projects.project'),
        ),
        migrations.AddField(
            model_name='project',
            name='developers',
            field=models.ManyToManyField(related_name='developer_in_projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
    ]
