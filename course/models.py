from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20, verbose_name="学生名")
    gender = models.CharField(
        max_length=20,
        choices=(("male", "男"), ("female", "女")),
        verbose_name="性别"
    )

    class Meta:
        verbose_name = verbose_name_plural = "学生表"

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=20, verbose_name="老师名")

    class Meta:
        verbose_name = verbose_name_plural = "老师表"

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=20, verbose_name="课程名")
    room = models.CharField(max_length=20, verbose_name="教室名")
    teacher = models.ForeignKey(to=Teacher, verbose_name="老师", related_name="courses", on_delete=None)

    class Meta:
        verbose_name = verbose_name_plural = "课程表"

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(to=Student, on_delete=None, related_name="stu_enroll")
    course = models.ForeignKey(to=Course, on_delete=None, related_name="course_enroll")

    class Meta:
        verbose_name = verbose_name_plural = "选课表"
        unique_together = ("student", "course")

    def __str__(self):
        return "选课表"
