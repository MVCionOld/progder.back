from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAdminUser

from .models import (
    Candidate,
    Recruiter,
    Engagement
)
from .serializers import (
    CandidateSerializer,
    RecruiterSerializer,
    EngagementSerializer
)


class CandidateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    authentication_classes = (BasicAuthentication, SessionAuthentication)


class RecruiterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
    permission_classes = (IsAdminUser,)


class EngagementViewSet(viewsets.ModelViewSet):
    queryset = Engagement.objects.all()
    serializer_class = EngagementSerializer
    permission_classes = (IsAdminUser,)
