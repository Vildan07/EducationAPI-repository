from django.contrib import admin
from .models import Teacher, Class, Student

# Register your models here.


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'salary',  'get_class_name')

    def get_class_name(self, obj):
        classes_name = obj.class_name.all()
        return ', '.join([str(c) for c in classes_name])

    get_class_name.short_description = 'Classes'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'class_name')


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name',)
