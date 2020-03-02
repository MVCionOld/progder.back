from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault


from .models import (
    Candidate,
    Recruiter,
    Engagement
)


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = '__all__'


class EngagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engagement
        fields = '__all__'

    # def save(self):

