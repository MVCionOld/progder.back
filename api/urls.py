from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    candidate_engagement,
    candidate_engagement_list,
    recruiter_engagement_list,
    recruiter_engagement_list_new,
    CandidateAuthView,
    RecruiterAuthView
)

urlpatterns = [
    path(r'engagement/candidate/<int:id>', candidate_engagement),
    path(r'engagement/candidate', candidate_engagement_list),
    path(r'engagement/recruiter', recruiter_engagement_list),
    path(r'engagement/recruiter/new', recruiter_engagement_list_new),
    path(r'register/candidate', CandidateAuthView.as_view()),
    path(r'register/recruiter', RecruiterAuthView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
