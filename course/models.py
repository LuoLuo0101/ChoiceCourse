from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20, verbose_name="学生名")
    gender = models.CharField(
        max_length=20,
        choices=(("male", "男"), ("female", "女")),
        verbose_name="性别"
    )


class Teacher(models.Model):
    name = models.CharField(max_length=20, verbose_name="老师名")


class Course(models.Model):
    name = models.CharField(max_length=20, verbose_name="课程名")
    room = models.CharField(max_length=20, verbose_name="教室名")
    teacher = models.ForeignKey(to=Teacher, verbose_name="老师", related_name="courses", on_delete=None)


class Enrollment(models.Model):
    student = models.ForeignKey(to=Student, on_delete=None, related_name="stu_enroll")
    course = models.ForeignKey(to=Course, on_delete=None, related_name="course_enroll")
