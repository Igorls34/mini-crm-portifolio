from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import LeadViewSet, ActivityLogViewSet

router = DefaultRouter()
router.register(r'leads', LeadViewSet)
router.register(r'activity-logs', ActivityLogViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]