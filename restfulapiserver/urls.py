from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
import addresses.views as views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('addresses/', views.address_list),
    path('addresses/<int:pk>/', views.address),
    path('app_login/', views.app_login),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]