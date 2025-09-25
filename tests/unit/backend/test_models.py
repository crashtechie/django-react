from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from customers.models import Customer


class CustomerModelTest(TestCase):
    """Test cases for the Customer model."""

    def setUp(self):
        """Set up test data."""
        self.valid_customer_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "555-1234",
        }

    def test_customer_creation_success(self):
        """Test successful customer creation."""
        customer = Customer.objects.create(**self.valid_customer_data)

        self.assertEqual(customer.first_name, "John")
        self.assertEqual(customer.last_name, "Doe")
        self.assertEqual(customer.email, "john.doe@example.com")
        self.assertEqual(customer.phone, "555-1234")
        self.assertEqual(customer.full_name, "John Doe")
        self.assertTrue(customer.is_active)

    def test_customer_string_representation(self):
        """Test the string representation of a customer."""
        customer = Customer.objects.create(**self.valid_customer_data)
        expected_str = f"{customer.first_name} {customer.last_name} ({customer.email})"
        self.assertEqual(str(customer), expected_str)

    def test_full_name_property(self):
        """Test the full_name property."""
        customer = Customer.objects.create(**self.valid_customer_data)
        expected_full_name = "John Doe"
        self.assertEqual(customer.full_name, expected_full_name)

    def test_email_uniqueness(self):
        """Test that email addresses must be unique."""
        Customer.objects.create(**self.valid_customer_data)

        # Try to create another customer with the same email
        duplicate_data = self.valid_customer_data.copy()
        duplicate_data["first_name"] = "Jane"

        with self.assertRaises(IntegrityError):
            Customer.objects.create(**duplicate_data)

    def test_invalid_email_format(self):
        """Test validation of email format."""
        invalid_data = self.valid_customer_data.copy()
        invalid_data["email"] = "invalid-email"

        customer = Customer(**invalid_data)
        with self.assertRaises(ValidationError):
            customer.full_clean()

    def test_invalid_phone_format(self):
        """Test validation of phone format."""
        invalid_data = self.valid_customer_data.copy()
        invalid_data["phone"] = "invalid-phone"

        customer = Customer(**invalid_data)
        with self.assertRaises(ValidationError):
            customer.full_clean()

    def test_valid_phone_formats(self):
        """Test various valid phone formats."""
        valid_phone_numbers = ["555-1234", "1234567890", "+1234567890"]

        for i, phone in enumerate(valid_phone_numbers):
            valid_data = self.valid_customer_data.copy()
            valid_data["phone"] = phone
            valid_data["email"] = (
                f"test{i}@example.com"  # Use index to avoid duplicates
            )

            customer = Customer(**valid_data)
            try:
                customer.full_clean()
                customer.save()
                self.assertTrue(True)  # If we reach here, validation passed
            except ValidationError:
                self.fail(f"Valid phone number {phone} failed validation")

    def test_required_fields(self):
        """Test that required fields are validated."""
        # Test missing first_name
        invalid_data = self.valid_customer_data.copy()
        del invalid_data["first_name"]

        customer = Customer(**invalid_data)
        with self.assertRaises(ValidationError):
            customer.full_clean()

        # Test missing last_name
        invalid_data = self.valid_customer_data.copy()
        del invalid_data["last_name"]

        customer = Customer(**invalid_data)
        with self.assertRaises(ValidationError):
            customer.full_clean()

        # Test missing email
        invalid_data = self.valid_customer_data.copy()
        del invalid_data["email"]

        customer = Customer(**invalid_data)
        with self.assertRaises(ValidationError):
            customer.full_clean()

    def test_default_values(self):
        """Test default values for optional fields."""
        customer = Customer.objects.create(**self.valid_customer_data)
        self.assertTrue(customer.is_active)  # Default should be True
        self.assertIsNotNone(customer.created_at)
        self.assertIsNotNone(customer.updated_at)

    def test_name_capitalization(self):
        """Test that names are properly capitalized."""
        data = self.valid_customer_data.copy()
        data["first_name"] = "john"
        data["last_name"] = "doe"

        customer = Customer.objects.create(**data)
        self.assertEqual(customer.first_name, "John")
        self.assertEqual(customer.last_name, "Doe")

    def test_email_normalization(self):
        """Test that email is normalized to lowercase."""
        data = self.valid_customer_data.copy()
        data["email"] = "JOHN.DOE@EXAMPLE.COM"

        customer = Customer.objects.create(**data)
        self.assertEqual(customer.email, "john.doe@example.com")
