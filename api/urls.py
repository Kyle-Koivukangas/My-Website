from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

from api import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'token-auth', auth_views.obtain_auth_token, 'authenticate')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
]
