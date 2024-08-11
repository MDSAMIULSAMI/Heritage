from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, PropertyImageViewSet, BidViewSet, TestimonialViewSet, TeamMemberViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'property-images', PropertyImageViewSet)
router.register(r'bids', BidViewSet)
router.register(r'testimonials', TestimonialViewSet)
router.register(r'team', TeamMemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
