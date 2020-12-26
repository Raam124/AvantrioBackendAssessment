from rest_framework import serializers
from django.contrib.auth.models import User

from jobs.models import Job,WorkHistory

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)


    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            email =validated_data['email'],
            first_name =validated_data['first_name'],
            last_name =validated_data['last_name'],

        )
        user.save()

        return user

    class Meta:
        model = User
        fields = ( "id", "username",'email','password', 'confirm_password',"first_name",'last_name')


class UserAccountUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True, initial="current username")
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.email = validated_data.get('email',instance.email)
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)

        
        return instance
        instance.save()



class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'qualifications', 'experience', 'reporting_to','created_by','add_interviwer','add_candidate')
        model = Job