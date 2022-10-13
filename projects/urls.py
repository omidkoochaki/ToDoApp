from rest_framework import routers

from projects.views import TaskViewSet, ProjectsViewSet

router = routers.DefaultRouter()
router.register(prefix='', viewset=ProjectsViewSet, basename='projects')
project_urls = router.urls

tasks_router = routers.DefaultRouter()
tasks_router.register(prefix='', viewset=TaskViewSet, basename='tasks')
task_urls = tasks_router.urls


