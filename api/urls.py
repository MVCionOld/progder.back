from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    candidate_engagement,
    candidate_engagement_list,
    recruiter_engagement_list
)

urlpatterns = [
    path(r'engagements/candidate/<int:pk>', candidate_engagement),
    path(r'engagements/candidate/list/', candidate_engagement_list),
    path(r'engagements/recruiter/list/', recruiter_engagement_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
