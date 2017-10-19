from django.conf.urls import url
from rest_framework import routers
from django.contrib import admin
from django.conf.urls import include
from betslip_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'betslip', views.BetSlipViewSet, base_name='betslip')
router.register(r'match', views.MatchViewSet, base_name='match')


urlpatterns = [
	url(r'^', include(router.urls)),    
]