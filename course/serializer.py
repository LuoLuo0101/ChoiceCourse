# coding:utf-8
__author__ = 'Luo'

from rest_framework.serializers import ModelSerializer

from course.models import Course, Teacher


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    teacher = TeacherSerializer(many=False)

    class Meta:
        model = Course
        fields = "__all__"
