from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
    Candidate,
    Recruiter,
    Engagement
)
from .serializers import (
    EngagementSerializer
)


@api_view(['GET', 'POST'])
def recruiter_engagement_list(request):
    current_user = request.user
    if request.method == 'GET':
        try:
            engagements = Recruiter.objects\
                .get(user=current_user)\
                .get_accepted_engagements()
        except Engagement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        engagement_serializer = EngagementSerializer(engagements, many=True)
        return Response(engagement_serializer.data)
    elif request.method == 'POST':
        engagement_serializer = EngagementSerializer(data=request.data)
        if engagement_serializer.is_valid():
            engagement_serializer.save()
            return Response(engagement_serializer.data, status=status.HTTP_201_CREATED)
        return Response(engagement_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def candidate_engagement_list(request):
    current_user = request.user
    try:
        engagements = Candidate.objects\
            .get(user=current_user)\
            .get_engagements()
    except Engagement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    engagement_serializer = EngagementSerializer(engagements, many=True)
    return Response(engagement_serializer.data)


@api_view(['PUT'])
def candidate_engagement(request, pk):
    try:
        engagement = Engagement.objects.get(pk=pk)
    except Engagement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    engagement_serializer = EngagementSerializer(engagement, data=request.data)
    if engagement_serializer.is_valid():
        engagement_serializer.save()
        return Response(engagement_serializer.data, status=status.HTTP_201_CREATED)
    return Response(engagement_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
