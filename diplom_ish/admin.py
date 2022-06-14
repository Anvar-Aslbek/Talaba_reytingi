from django.contrib import admin
from .models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','faculty_id','kurs_number_id', 'holat')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'holat')
    list_filter = ('kurs_number_id','faculty_id')

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'decan_name')
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'decan_name')

class BahoAdmin(admin.ModelAdmin):
    list_display = ('id', 'talaba_id', 'fan_id', 'baho')
    list_display_links = ('id', 'talaba_id',)
    search_fields = ('talaba_id', )
    ordering = ('talaba_id','fan_id')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'kafedra_id')
    list_display_links = ('id', 'first_name',)
    search_fields = ('last_name', 'first_name')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher_id')
    list_display_links = ('id', 'name', 'teacher_id')
    search_fields = ('name', 'first_name')

class KafedraAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Student, StudentAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Kafedra, KafedraAdmin)
admin.site.register(Baho, BahoAdmin)

admin.site.register([Course_number])


admin.site.site_title = "Yangiliklarni boshqarish"
admin.site.site_header = "Yangiliklarni boshqarish"