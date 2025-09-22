"""
URL configuration for customer_management project.
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def health_check(request):
    """Health check endpoint for Docker health checks."""
    return JsonResponse({"status": "healthy", "service": "customer-backend"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('customers.urls')),
    path('health/', health_check, name='health_check'),
]