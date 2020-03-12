from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    Candidate,
    Recruiter,
    Engagement
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CandidateSerializerFull(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Candidate
        fields = '__all__'


class CandidateSerializerBasic(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Candidate
        fields = ['user']


class RecruiterSerializerBasic(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Recruiter
        fields = ['user']


class RecruiterSerializerFull(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Recruiter
        fields = ['user', 'company_name']


class EngagementSerializer(serializers.ModelSerializer):
    candidate = CandidateSerializerBasic()
    recruiter = RecruiterSerializerBasic()

    class Meta:
        model = Engagement
        fields = ['state', 'candidate', 'recruiter']
