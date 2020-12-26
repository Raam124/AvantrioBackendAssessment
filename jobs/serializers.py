from rest_framework import serializers
from jobs.models import Job,WorkHistory


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ( 'id','name', 'qualifications', 'experience', 'reporting_to','created_by','add_interviwer','add_candidate')
        model = Job

class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'history_user', 'position', 'workplace', 'start','end')
        model = WorkHistory