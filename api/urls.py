from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as rest_framework_views

from api import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'users', views.UserViewSet)
# router.register(r'token-auth', rest_framework_views.obtain_auth_token, base_name='get_auth_token')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token')
]
