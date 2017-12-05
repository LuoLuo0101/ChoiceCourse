from django.contrib import admin

from course.models import Student, Teacher, Course, Enrollment

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Enrollment)
