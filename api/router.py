from rest_framework import routers

from .viewset import (
    CandidateViewSet,
    RecruiterViewSet
)

router = routers.DefaultRouter()
router.register(r'candidates', CandidateViewSet)
router.register(r'recruiters', RecruiterViewSet)
