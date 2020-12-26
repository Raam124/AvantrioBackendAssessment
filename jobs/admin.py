from django.contrib import admin
from jobs.models import Job, QuestionSet, Assessment,AssesmentMarks,WorkHistory


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'qualifications', 'experience','reporting_to','created_by')
    list_filter = ('qualifications', 'reporting_to', 'created_by')
    search_fields = ('name', 'qualifications','reporting_to')


@admin.register(QuestionSet)
class QuestionSetAdmin(admin.ModelAdmin):
    list_display = ('regarded_job', 'title', 'category')
    list_filter = ('category', 'asking_ways')



@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('regarded_job', 'title', 'typeof_assessment')
    list_filter = ('typeof_assessment', 'assessors')


@admin.register(AssesmentMarks)
class AssesmentMarksAdmin(admin.ModelAdmin):
    list_display = ('regarded_assessment', 'marks')



@admin.register(WorkHistory)
class WorkHistoryAdmin(admin.ModelAdmin):
    list_display = ('history_user', 'position','workplace')
    list_filter = ('history_user', 'position','workplace','start','end')
   


