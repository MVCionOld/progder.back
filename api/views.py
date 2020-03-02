from rest_framework import viewsets, serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

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


class RecruiterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer


class EngagementViewSet(viewsets.ModelViewSet):
    queryset = Engagement.objects.all() #filter(candidate__user=serializers.CurrentUserDefault())
    serializer_class = EngagementSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
