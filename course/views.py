from rest_framework import viewsets, mixins

from course.models import Course, Enrollment
from course.serializer import CourseSerializer, EnrollmentSerializer, EnrollmentDetailsSerializer


class CourseViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EnrollmentViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = Enrollment.objects.all()

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve" or self.action == "destroy":
            return EnrollmentDetailsSerializer
        else:
            return EnrollmentSerializer
