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
        fields = ('id', 'username')


class UserAuthSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)


class CandidateSerializerBasic(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Candidate
        fields = ('user',)


class CandidateAuthSerializer(serializers.ModelSerializer):
    user = UserAuthSerializer()

    def create(self, validated_data):
        candidate = Candidate.objects.create(
            user=self.get_fields()['user'].create(validated_data['user']),
            personal_info=validated_data['personal_info'],
            skills_info=validated_data['skills_info'],
            wishes_info=validated_data['wishes_info'],
            extra_info=validated_data['extra_info'],
            personal_info_extended=validated_data['personal_info_extended'],
            skills_info_extended=validated_data['skills_info_extended'],
            wishes_info_extended=validated_data['wishes_info_extended'],
            extra_info_extended=validated_data['extra_info_extended']
        )
        candidate.save()
        return candidate

    class Meta:
        model = Candidate
        fields = (
            'user',
            'personal_info',
            'skills_info',
            'wishes_info',
            'extra_info',
            'personal_info_extended',
            'skills_info_extended',
            'wishes_info_extended',
            'extra_info_extended'
        )


class CandidateSerializerFull(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Candidate
        fields = '__all__'


class RecruiterSerializerBasic(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Recruiter
        fields = ('user',)


class RecruiterAuthSerializer(serializers.ModelSerializer):
    user = UserAuthSerializer()

    def create(self, validated_data):
        recruiter = Recruiter.objects.create(
            user=self.get_fields()['user'].create(validated_data['user']),
            company_name=validated_data['company_name']
        )
        recruiter.save()
        return recruiter

    class Meta:
        model = Recruiter
        fields = ('user', 'company_name')


class RecruiterSerializerFull(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Recruiter
        fields = ('user', 'company_name')


class EngagementSerializer(serializers.ModelSerializer):
    candidate = CandidateSerializerBasic()
    recruiter = RecruiterSerializerBasic()

    class Meta:
        model = Engagement
        fields = ('state', 'candidate', 'recruiter')
