from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework.documentation import include_docs_urls

from projects.urls import project_urls, task_urls

from users.urls import urls as user_urls

urlpatterns = [
    path(r'', include_docs_urls(title='TODO APP API')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/projects/', include((project_urls, 'projects'))),
    path(r'api/projects/<int:project_id>/tasks/', include((task_urls, 'tasks'))),
    path('api/users/', include((user_urls, 'users'))),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
