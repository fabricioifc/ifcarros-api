from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet, CarViewSet, GroupViewSet, SolicitationViewSet, PassengerViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cars', CarViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'solicitations', SolicitationViewSet)
router.register(r'passengers', PassengerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
