# coding:utf-8
__author__ = 'Luo'

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from course.models import Course, Teacher, Student, Enrollment


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    teacher = TeacherSerializer(many=False)

    class Meta:
        model = Course
        fields = "__all__"


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class EnrollmentDetailsSerializer(ModelSerializer):
    student = StudentSerializer(many=False)

    course = CourseSerializer(many=False)

    class Meta:
        model = Enrollment
        fields = "__all__"


class EnrollmentSerializer(ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=Student.objects.all()
    )

    course = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=Course.objects.all()
    )

    class Meta:
        model = Enrollment
        fields = "__all__"
