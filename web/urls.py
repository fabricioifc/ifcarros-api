from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
#from api.views import UserViewSet, CarViewSet, GroupViewSet, SolicitationViewSet, PassengerViewSet

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'cars', CarViewSet)
# router.register(r'groups', GroupViewSet)
# router.register(r'solicitations', SolicitationViewSet)
# router.register(r'passengers', PassengerViewSet)
app_name = 'web'

urlpatterns = [
    url(r'^login/$', LoginView.as_view(redirect_authenticated_user=True), {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^$', TemplateView.as_view(template_name='web/home/home.html'), name='home'),
    url(r'^profile/$', views.edit_profile, name='profile'),
]
