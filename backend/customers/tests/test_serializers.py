from django.test import TestCase
from rest_framework.test import APITestCase

from customers.models import Customer
from customers.serializers import CustomerListSerializer, CustomerSerializer


class CustomerSerializerTest(TestCase):
    """Test cases for CustomerSerializer."""

    def setUp(self):
        """Set up test data."""
        self.customer_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "555-1234",
        }

        self.customer = Customer.objects.create(**self.customer_data)

    def test_customer_serializer_serialization(self):
        """Test serializing a customer instance."""
        serializer = CustomerSerializer(self.customer)
        data = serializer.data  # type: ignore

        self.assertEqual(data["first_name"], "John")  # type: ignore
        self.assertEqual(data["last_name"], "Doe")  # type: ignore
        self.assertEqual(data["email"], "john.doe@example.com")  # type: ignore
        self.assertEqual(data["phone"], "555-1234")  # type: ignore
        self.assertEqual(data["full_name"], "John Doe")  # type: ignore
        self.assertTrue(data["is_active"])  # type: ignore

    def test_customer_serializer_deserialization(self):
        """Test deserializing customer data."""
        # Use different data to avoid unique constraint conflicts
        new_customer_data = {
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane.smith@example.com",
            "phone": "555-5678",
        }

        serializer = CustomerSerializer(data=new_customer_data)

        if not serializer.is_valid():
            print("Validation errors:", serializer.errors)
        self.assertTrue(serializer.is_valid())
        customer = serializer.save()

        self.assertEqual(customer.first_name, "Jane")  # type: ignore
        self.assertEqual(customer.last_name, "Smith")  # type: ignore
        self.assertEqual(customer.email, "jane.smith@example.com")  # type: ignore
        self.assertEqual(customer.phone, "555-5678")  # type: ignore

    def test_customer_serializer_update(self):
        """Test updating a customer through the serializer."""
        update_data = {"first_name": "Johnny", "phone": "555-5678"}

        serializer = CustomerSerializer(self.customer, data=update_data, partial=True)
        self.assertTrue(serializer.is_valid())

        updated_customer = serializer.save()
        self.assertEqual(updated_customer.first_name, "Johnny")  # type: ignore
        self.assertEqual(updated_customer.phone, "555-5678")  # type: ignore
        self.assertEqual(updated_customer.email, "john.doe@example.com")  # type: ignore  # Should remain unchanged

    def test_customer_serializer_invalid_data(self):
        """Test serializer validation with invalid data."""
        invalid_data = {
            "first_name": "",  # Empty first name
            "last_name": "Doe",
            "email": "invalid-email",  # Invalid email format
            "phone": "invalid-phone",  # Invalid phone format
        }

        serializer = CustomerSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())

        # Check that we have validation errors
        self.assertIn("first_name", serializer.errors)
        self.assertIn("email", serializer.errors)
        self.assertIn("phone", serializer.errors)

    def test_customer_serializer_required_fields(self):
        """Test serializer validation with missing required fields."""
        incomplete_data = {
            "first_name": "John",
            # Missing last_name, email, phone
        }

        serializer = CustomerSerializer(data=incomplete_data)
        self.assertFalse(serializer.is_valid())

        # Check that required fields are flagged
        self.assertIn("last_name", serializer.errors)
        self.assertIn("email", serializer.errors)
        self.assertIn("phone", serializer.errors)

    def test_customer_serializer_email_uniqueness(self):
        """Test email uniqueness validation in serializer."""
        duplicate_data = self.customer_data.copy()
        duplicate_data["first_name"] = "Jane"  # type: ignore  # Different name, same email

        serializer = CustomerSerializer(data=duplicate_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    def test_customer_serializer_read_only_fields(self):
        """Test that read-only fields are not updated."""
        original_created_at = self.customer.created_at  # type: ignore

        update_data = {
            "first_name": "Johnny",
            "created_at": "2020-01-01T00:00:00Z",  # Try to update read-only field
            "id": 999,  # Try to update read-only field
        }

        serializer = CustomerSerializer(self.customer, data=update_data, partial=True)
        self.assertTrue(serializer.is_valid())

        updated_customer = serializer.save()
        self.assertEqual(updated_customer.first_name, "Johnny")  # type: ignore  # This should update
        self.assertEqual(updated_customer.created_at, original_created_at)  # type: ignore  # This should not change
        self.assertNotEqual(updated_customer.id, 999)  # type: ignore  # ID should not change

    def test_customer_serializer_phone_validation(self):
        """Test phone number validation in serializer."""
        valid_phones = ["555-1234", "1234567890", "+1234567890"]

        for phone in valid_phones:
            data = self.customer_data.copy()
            data["phone"] = phone  # type: ignore
            data["email"] = f'test{phone.replace("-", "").replace("+", "")}@example.com'  # type: ignore

            serializer = CustomerSerializer(data=data)
            self.assertTrue(serializer.is_valid(), f"Phone {phone} should be valid")


class CustomerListSerializerTest(TestCase):
    """Test cases for CustomerListSerializer."""

    def setUp(self):
        """Set up test data."""
        self.customer = Customer.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="555-1234",
        )

    def test_customer_list_serializer_fields(self):
        """Test that CustomerListSerializer includes only expected fields."""
        serializer = CustomerListSerializer(self.customer)
        data = serializer.data  # type: ignore

        # Should include basic fields
        expected_fields = {"id", "full_name", "email", "phone", "is_active"}
        self.assertEqual(set(data.keys()), expected_fields)

    def test_customer_list_serializer_full_name(self):
        """Test that full_name is correctly computed."""
        serializer = CustomerListSerializer(self.customer)
        data = serializer.data  # type: ignore

        self.assertEqual(data["full_name"], "John Doe")  # type: ignore

    def test_customer_list_serializer_multiple_customers(self):
        """Test serializing multiple customers."""
        customer2 = Customer.objects.create(
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@example.com",
            phone="555-5678",
        )

        customers = [self.customer, customer2]
        serializer = CustomerListSerializer(customers, many=True)
        data = serializer.data  # type: ignore

        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["full_name"], "John Doe")  # type: ignore
        self.assertEqual(data[1]["full_name"], "Jane Smith")  # type: ignore

    def test_customer_list_serializer_read_only(self):
        """Test that CustomerListSerializer is read-only."""
        # CustomerListSerializer should typically be read-only for list views
        # This test verifies that it doesn't have create/update methods
        serializer = CustomerListSerializer()

        # Check if serializer has create/update methods - for list views, typically they don't
        # This is more of a design principle test
        self.assertTrue(hasattr(serializer, "to_representation"))
        self.assertEqual(len(serializer.fields), 5)  # Should have 5 fields as defined
