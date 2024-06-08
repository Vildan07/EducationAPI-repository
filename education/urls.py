from django.urls import path, include
from rest_framework import routers
from .views import TeacherViewSet, StudentViewSet, ClassViewSet

router = routers.SimpleRouter()
router.register('teacher', TeacherViewSet)
router.register('student', StudentViewSet)
router.register('class', ClassViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]