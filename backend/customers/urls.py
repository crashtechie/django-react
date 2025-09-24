from django.urls import include, path  # type: ignore
from rest_framework.routers import DefaultRouter  # type: ignore

from .views import CustomerViewSet

router = DefaultRouter()
router.register(r"customers", CustomerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
