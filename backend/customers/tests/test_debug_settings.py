"""
Debug test to verify Django settings in CI environment
"""
from django.conf import settings
from django.test import TestCase


class DebugSettingsTest(TestCase):
    """Debug test to verify settings are loaded correctly."""

    def test_django_settings_module(self):
        """Verify which settings module is being used."""
        print(f"DJANGO_SETTINGS_MODULE: {settings.SETTINGS_MODULE}")
        self.assertEqual(settings.SETTINGS_MODULE, "customer_management.test_settings")

    def test_rest_framework_settings(self):
        """Verify REST framework permissions."""
        rest_framework_settings = getattr(settings, 'REST_FRAMEWORK', {})
        print(f"REST_FRAMEWORK settings: {rest_framework_settings}")
        
        permission_classes = rest_framework_settings.get('DEFAULT_PERMISSION_CLASSES', [])
        print(f"Default permission classes: {permission_classes}")
        
        auth_classes = rest_framework_settings.get('DEFAULT_AUTHENTICATION_CLASSES', [])
        print(f"Default authentication classes: {auth_classes}")
        
        self.assertIn("rest_framework.permissions.AllowAny", permission_classes)
        self.assertEqual(auth_classes, [])

    def test_csrf_middleware(self):
        """Verify CSRF middleware is disabled."""
        middleware = getattr(settings, 'MIDDLEWARE', [])
        print(f"Middleware: {middleware}")
        self.assertNotIn("django.middleware.csrf.CsrfViewMiddleware", middleware)