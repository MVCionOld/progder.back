from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register('candidates', CandidateViewSet)
router.register('recruiters', RecruiterViewSet)
router.register('engagements', EngagementViewSet)