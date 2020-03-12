from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAdminUser

from .models import (
    Candidate,
    Recruiter,
    Engagement
)
from .serializers import (
    CandidateSerializerFull,
    RecruiterSerializerFull,
    EngagementSerializer
)


class CandidateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializerFull
    # authentication_classes = (BasicAuthentication, SessionAuthentication)


class RecruiterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializerFull
    # authentication_classes = (BasicAuthentication, SessionAuthentication)
    # permission_classes = (IsAdminUser,)


class EngagementViewSet(viewsets.ModelViewSet):
    queryset = Engagement.objects.all()
    serializer_class = EngagementSerializer
    authentication_classes = (BasicAuthentication, )
    # permission_classes = IsAdminUser
