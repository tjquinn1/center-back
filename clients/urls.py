from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from center.urls import common_router as router

router.register(r'client', views.ClientViewSet) 
router.register(r'project', views.ProjectViewSet)
router.register(r'task', views.TaskViewSet) 
router.register(r'time', views.TimeViewSet) 


    