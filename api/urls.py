from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    candidate_engagement,
    candidate_engagement_list,
    recruiter_engagement_list,
    CandidateAuthView,
    RecruiterAuthView
)

urlpatterns = [
    path(r'list/candidate/<int:pk>', candidate_engagement),
    path(r'list/candidate', candidate_engagement_list),
    path(r'list/recruiter', recruiter_engagement_list),
    path(r'register/candidate', CandidateAuthView.as_view()),
    path(r'register/recruiter', RecruiterAuthView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
