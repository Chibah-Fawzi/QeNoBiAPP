from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('groups', views.GroupView)
router.register('links', views.LinkView)

urlpatterns = [
    path('', include(router.urls))
]
