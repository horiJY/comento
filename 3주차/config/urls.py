from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from todoapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'todos', views.TodoViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
