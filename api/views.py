from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import (
    Candidate,
    Recruiter,
    Engagement
)
from .serializers import (
    CandidateAuthSerializer,
    RecruiterAuthSerializer,
    EngagementSerializer,
    CandidateComplexSerializer,
)


class CandidateAuthView(CreateAPIView):
    model = Candidate
    permission_classes = (permissions.AllowAny,)
    serializer_class = CandidateAuthSerializer


class RecruiterAuthView(CreateAPIView):
    model = Recruiter
    permission_classes = (permissions.AllowAny,)
    serializer_class = RecruiterAuthSerializer


@api_view(['GET', 'POST'])
def recruiter_engagement_list(request):
    current_user = request.user
    if request.method == 'GET':
        try:
            engagements = Recruiter.objects \
                .get(user=current_user) \
                .get_accepted_engagements()
        except Engagement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        engagement_serializer = EngagementSerializer(engagements, many=True)
        return Response(engagement_serializer.data)
    elif request.method == 'POST':
        try:
            recruiter = Recruiter.objects.get(user=current_user)
            candidate = Candidate.objects.get(user_id=request.data['candidate'])
            state = request.data['state']
            engagement = Engagement(
                state=state,
                candidate=candidate,
                recruiter=recruiter
            )
            engagement.save()
            return Response(
                data=engagement.last_change_date,
                status=status.HTTP_201_CREATED
            )
        except (Recruiter.DoesNotExist, Candidate.DoesNotExist, ):
            return Response(
                exception=True,
                status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['GET'])
def recruiter_engagement_list_new(request):
    current_user = request.user
    try:
        engagements = Recruiter.objects \
            .get(user=current_user) \
            .interview_candidates()
    except Engagement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    candidate_serializer = CandidateComplexSerializer(engagements, many=True)
    return Response(candidate_serializer.data)


@api_view(['GET'])
def candidate_engagement_list(request):
    current_user = request.user
    try:
        engagements = Candidate.objects \
            .get(user=current_user) \
            .get_engagements()
    except Candidate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    engagement_serializer = EngagementSerializer(engagements, many=True)
    return Response(data=engagement_serializer.data)


@api_view(['PUT'])
def candidate_engagement(request, id):
    try:
        engagement = Engagement.objects.get(id=id)
    except Engagement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    engagement.state = request.data["state"]
    engagement.save(update_fields=["state"])
    return Response(data="ok", status=status.HTTP_202_ACCEPTED)
