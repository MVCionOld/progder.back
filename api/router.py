from rest_framework import routers

from .viewset import (
    CandidateViewSet,
    RecruiterViewSet,
    EngagementViewSet
)

router = routers.DefaultRouter()
router.register(r'candidates', CandidateViewSet)
router.register(r'recruiters', RecruiterViewSet)
router.register(r'engagements', EngagementViewSet)
