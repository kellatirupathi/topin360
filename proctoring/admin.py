from django.contrib import admin
from .models import Assessment, Student, Video


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('student_id', )


class AssessmentAdmin(admin.ModelAdmin):
    readonly_fields = ('assessment_id', )


# Register your models here.
admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Video, VideoAdmin)
