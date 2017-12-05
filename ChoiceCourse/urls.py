from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from course.views import CourseViewSet, EnrollmentViewSet, EnrollStudentViewSet

router = DefaultRouter()

router.register(prefix="course", viewset=CourseViewSet, base_name="course")
router.register(prefix="enrollment", viewset=EnrollmentViewSet, base_name="enrollment")
router.register(prefix="enrollstudent", viewset=EnrollStudentViewSet, base_name="enrollstudent")

urlpatterns = [
    url(r'^', include(router.urls)),

    url('admin/', admin.site.urls),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # 文档自动生成
    url(r'^docs/', include_docs_urls(title='学生选课系统')),
]
