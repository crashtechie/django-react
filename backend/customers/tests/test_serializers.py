from django.test import TestCase
from rest_framework.test import APITestCase
from customers.models import Customer
from customers.serializers import CustomerSerializer, CustomerListSerializer
from decimal import Decimal


class CustomerSerializerTest(TestCase):
    """Test cases for CustomerSerializer."""
    
    def setUp(self):
        """Set up test data."""
        self.customer_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '555-1234',
            'address': '123 Main St',
            'city': 'Anytown',
            'state': 'NY',
            'zip_code': '12345',
            'subscription_tier': 'basic',
            'monthly_spend': '99.99'
        }
        
        self.customer = Customer.objects.create(**{
            **self.customer_data,
            'monthly_spend': Decimal('99.99')
        })
    
    def test_customer_serializer_serialization(self):
        """Test serializing a customer instance."""
        serializer = CustomerSerializer(self.customer)
        data = serializer.data
        
        self.assertEqual(data['first_name'], 'John')
        self.assertEqual(data['last_name'], 'Doe')
        self.assertEqual(data['email'], 'john.doe@example.com')
        self.assertEqual(data['full_name'], 'John Doe')
        self.assertEqual(data['full_address'], '123 Main St, Anytown, NY 12345')
        self.assertEqual(data['subscription_tier'], 'basic')
        self.assertEqual(float(data['monthly_spend']), 99.99)
        self.assertTrue(data['is_active'])
    
    def test_customer_serializer_deserialization(self):
        """Test deserializing customer data."""
        serializer = CustomerSerializer(data=self.customer_data)
        
        self.assertTrue(serializer.is_valid())
        customer = serializer.save()
        
        self.assertEqual(customer.first_name, 'John')
        self.assertEqual(customer.last_name, 'Doe')
        self.assertEqual(customer.email, 'john.doe@example.com')
        self.assertEqual(customer.monthly_spend, Decimal('99.99'))
    
    def test_customer_serializer_invalid_data(self):
        """Test serializer validation with invalid data."""
        invalid_data = self.customer_data.copy()
        invalid_data['email'] = 'invalid-email'
        invalid_data['subscription_tier'] = 'invalid_tier'
        
        serializer = CustomerSerializer(data=invalid_data)
        
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)
        self.assertIn('subscription_tier', serializer.errors)
    
    def test_customer_serializer_required_fields(self):
        """Test serializer validation with missing required fields."""
        incomplete_data = {
            'first_name': 'John'
            # Missing last_name and email
        }
        
        serializer = CustomerSerializer(data=incomplete_data)
        
        self.assertFalse(serializer.is_valid())
        self.assertIn('last_name', serializer.errors)
        self.assertIn('email', serializer.errors)
    
    def test_customer_serializer_update(self):
        """Test updating a customer through the serializer."""
        update_data = {
            'first_name': 'Johnny',
            'subscription_tier': 'premium',
            'monthly_spend': '150.00'
        }
        
        serializer = CustomerSerializer(self.customer, data=update_data, partial=True)
        
        self.assertTrue(serializer.is_valid())
        updated_customer = serializer.save()
        
        self.assertEqual(updated_customer.first_name, 'Johnny')
        self.assertEqual(updated_customer.subscription_tier, 'premium')
        self.assertEqual(updated_customer.monthly_spend, Decimal('150.00'))
        # Unchanged fields should remain the same
        self.assertEqual(updated_customer.last_name, 'Doe')
        self.assertEqual(updated_customer.email, 'john.doe@example.com')
    
    def test_customer_serializer_email_uniqueness(self):
        """Test email uniqueness validation in serializer."""
        # Create another customer
        Customer.objects.create(
            first_name='Jane',
            last_name='Smith',
            email='jane.smith@example.com'
        )
        
        # Try to create customer with existing email
        duplicate_data = self.customer_data.copy()
        duplicate_data['email'] = 'jane.smith@example.com'
        
        serializer = CustomerSerializer(data=duplicate_data)
        
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)
    
    def test_customer_serializer_phone_validation(self):
        """Test phone number validation in serializer."""
        invalid_phones = ['abc-defg', '12-34', '123456789012345678']
        
        for invalid_phone in invalid_phones:
            invalid_data = self.customer_data.copy()
            invalid_data['phone'] = invalid_phone
            
            serializer = CustomerSerializer(data=invalid_data)
            
            self.assertFalse(serializer.is_valid())
            self.assertIn('phone', serializer.errors)
    
    def test_customer_serializer_read_only_fields(self):
        """Test that read-only fields are not updated."""
        original_created_at = self.customer.created_at
        
        update_data = {
            'first_name': 'Johnny',
            'created_at': '2020-01-01T00:00:00Z',  # Try to update read-only field
            'id': 9999  # Try to update read-only field
        }
        
        serializer = CustomerSerializer(self.customer, data=update_data, partial=True)
        
        self.assertTrue(serializer.is_valid())
        updated_customer = serializer.save()
        
        # Read-only fields should not change
        self.assertEqual(updated_customer.created_at, original_created_at)
        self.assertEqual(updated_customer.id, self.customer.id)
        # Regular field should update
        self.assertEqual(updated_customer.first_name, 'Johnny')


class CustomerListSerializerTest(TestCase):
    """Test cases for CustomerListSerializer."""
    
    def setUp(self):
        """Set up test data."""
        self.customer = Customer.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            phone='555-1234',
            address='123 Main St',
            city='Anytown',
            state='NY',
            zip_code='12345',
            subscription_tier='basic',
            monthly_spend=Decimal('99.99')
        )
    
    def test_customer_list_serializer_fields(self):
        """Test that CustomerListSerializer includes only expected fields."""
        serializer = CustomerListSerializer(self.customer)
        data = serializer.data
        
        expected_fields = {'id', 'full_name', 'email', 'phone', 'subscription_tier', 'is_active'}
        actual_fields = set(data.keys())
        
        self.assertEqual(actual_fields, expected_fields)
    
    def test_customer_list_serializer_full_name(self):
        """Test that full_name is correctly computed."""
        serializer = CustomerListSerializer(self.customer)
        data = serializer.data
        
        self.assertEqual(data['full_name'], 'John Doe')
    
    def test_customer_list_serializer_multiple_customers(self):
        """Test serializing multiple customers."""
        Customer.objects.create(
            first_name='Jane',
            last_name='Smith',
            email='jane.smith@example.com',
            subscription_tier='premium'
        )
        
        customers = Customer.objects.all()
        serializer = CustomerListSerializer(customers, many=True)
        data = serializer.data
        
        self.assertEqual(len(data), 2)
        
        # Check first customer
        self.assertEqual(data[0]['full_name'], 'John Doe')
        self.assertEqual(data[0]['subscription_tier'], 'basic')
        
        # Check second customer
        self.assertEqual(data[1]['full_name'], 'Jane Smith')
        self.assertEqual(data[1]['subscription_tier'], 'premium')
    
    def test_customer_list_serializer_read_only(self):
        """Test that CustomerListSerializer is read-only."""
        # This serializer should only be used for reading data
        # It doesn't include all required fields for creating/updating
        data = {
            'full_name': 'Test User',
            'email': 'test@example.com'
        }
        
        serializer = CustomerListSerializer(data=data)
        
        # Should be invalid for creation since it's missing required fields
        # and is designed only for reading
        self.assertFalse(serializer.is_valid())