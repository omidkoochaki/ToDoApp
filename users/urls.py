from django.urls import path
from rest_framework import routers

from users.views import RegisterView, UserDetailViewSet

# TokenObtainPairViewSet, TokenRefreshViewSet, TokenVerifyViewSet

router = routers.DefaultRouter()
router.register(prefix='signup', viewset=RegisterView, basename='user-signup')
router.register(prefix='details', viewset=UserDetailViewSet, basename='user')

# urls = [
#     # path('/login/', TokenObtainPairViewSet.as_view(), name='token_obtain_pair'),
#     # path('/token/refresh/', TokenRefreshViewSet.as_view(), name='token_refresh'),
#     # path('/token/verify/', TokenVerifyViewSet.as_view(), name='token_verify'),
# ]

urls = router.urls
# urls = token_urls
