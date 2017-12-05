from rest_framework import viewsets, mixins

from course.models import Course
from course.serializer import CourseSerializer


class CourseViewSet(mixins.ListModelMixin,
    viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer