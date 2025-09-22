from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from customers.models import Customer
from decimal import Decimal


class CustomerModelTest(TestCase):
    """Test cases for the Customer model."""
    
    def setUp(self):
        """Set up test data."""
        self.valid_customer_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '555-1234',
            'address': '123 Main St',
            'city': 'Anytown',
            'state': 'NY',
            'zip_code': '12345',
            'subscription_tier': 'basic',
            'monthly_spend': Decimal('99.99')
        }
    
    def test_customer_creation_success(self):
        """Test successful customer creation."""
        customer = Customer.objects.create(**self.valid_customer_data)
        
        self.assertEqual(customer.first_name, 'John')
        self.assertEqual(customer.last_name, 'Doe')
        self.assertEqual(customer.email, 'john.doe@example.com')
        self.assertEqual(customer.phone, '555-1234')
        self.assertEqual(customer.full_address, '123 Main St, Anytown, NY 12345')
        self.assertTrue(customer.is_active)
        self.assertIsNotNone(customer.created_at)
        self.assertIsNotNone(customer.updated_at)
    
    def test_customer_string_representation(self):
        """Test the string representation of a customer."""
        customer = Customer.objects.create(**self.valid_customer_data)
        expected_str = f"{customer.first_name} {customer.last_name} ({customer.email})"
        self.assertEqual(str(customer), expected_str)
    
    def test_full_name_property(self):
        """Test the full_name property."""
        customer = Customer.objects.create(**self.valid_customer_data)
        self.assertEqual(customer.full_name, 'John Doe')
    
    def test_full_address_property(self):
        """Test the full_address property."""
        customer = Customer.objects.create(**self.valid_customer_data)
        expected_address = '123 Main St, Anytown, NY 12345'
        self.assertEqual(customer.full_address, expected_address)
    
    def test_email_uniqueness(self):
        """Test that email addresses must be unique."""
        Customer.objects.create(**self.valid_customer_data)
        
        # Try to create another customer with the same email
        duplicate_data = self.valid_customer_data.copy()
        duplicate_data['first_name'] = 'Jane'
        
        with self.assertRaises(IntegrityError):
            Customer.objects.create(**duplicate_data)
    
    def test_invalid_email_format(self):
        """Test validation of email format."""
        invalid_data = self.valid_customer_data.copy()
        invalid_data['email'] = 'invalid-email'
        
        customer = Customer(**invalid_data)
        with self.assertRaises(ValidationError):
            customer.full_clean()
    
    def test_invalid_phone_format(self):
        """Test validation of phone format."""
        invalid_phone_data = [
            'abc-defg',  # Non-numeric
            '12-34',     # Too short
            '123456789012345678',  # Too long
            '123-45-6789',  # Wrong format
        ]
        
        for invalid_phone in invalid_phone_data:
            invalid_data = self.valid_customer_data.copy()
            invalid_data['phone'] = invalid_phone
            
            customer = Customer(**invalid_data)
            with self.assertRaises(ValidationError):
                customer.full_clean()
    
    def test_valid_phone_formats(self):
        """Test various valid phone formats."""
        valid_phones = [
            '555-1234',
            '1234567890',
            '+11234567890',
            '12345678901234567890'  # Max length
        ]
        
        for i, valid_phone in enumerate(valid_phones):
            valid_data = self.valid_customer_data.copy()
            valid_data['phone'] = valid_phone
            valid_data['email'] = f'test{i}@example.com'  # Unique email
            
            customer = Customer(**valid_data)
            try:
                customer.full_clean()
                customer.save()
            except ValidationError:
                self.fail(f"Valid phone format {valid_phone} should not raise ValidationError")
    
    def test_subscription_tier_choices(self):
        """Test subscription tier validation."""
        valid_tiers = ['basic', 'premium', 'enterprise']
        
        for tier in valid_tiers:
            valid_data = self.valid_customer_data.copy()
            valid_data['subscription_tier'] = tier
            valid_data['email'] = f'{tier}@example.com'
            
            customer = Customer.objects.create(**valid_data)
            self.assertEqual(customer.subscription_tier, tier)
    
    def test_invalid_subscription_tier(self):
        """Test invalid subscription tier."""
        invalid_data = self.valid_customer_data.copy()
        invalid_data['subscription_tier'] = 'invalid_tier'
        
        customer = Customer(**invalid_data)
        with self.assertRaises(ValidationError):
            customer.full_clean()
    
    def test_monthly_spend_validation(self):
        """Test monthly spend field validation."""
        # Test negative value
        invalid_data = self.valid_customer_data.copy()
        invalid_data['monthly_spend'] = Decimal('-10.00')
        
        customer = Customer(**invalid_data)
        with self.assertRaises(ValidationError):
            customer.full_clean()
    
    def test_required_fields(self):
        """Test that required fields are validated."""
        required_fields = ['first_name', 'last_name', 'email']
        
        for field in required_fields:
            invalid_data = self.valid_customer_data.copy()
            del invalid_data[field]
            
            customer = Customer(**invalid_data)
            with self.assertRaises(ValidationError):
                customer.full_clean()
    
    def test_default_values(self):
        """Test default values for optional fields."""
        minimal_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com'
        }
        
        customer = Customer.objects.create(**minimal_data)
        
        self.assertTrue(customer.is_active)
        self.assertEqual(customer.subscription_tier, 'basic')
        self.assertEqual(customer.monthly_spend, Decimal('0.00'))
    
    def test_model_ordering(self):
        """Test the model's default ordering."""
        # Create customers with different names
        Customer.objects.create(
            first_name='John', last_name='Zebra', email='john@example.com'
        )
        Customer.objects.create(
            first_name='Alice', last_name='Apple', email='alice@example.com'
        )
        Customer.objects.create(
            first_name='Bob', last_name='Baker', email='bob@example.com'
        )
        
        customers = list(Customer.objects.all())
        
        # Should be ordered by last_name, then first_name
        expected_order = ['Apple', 'Baker', 'Zebra']
        actual_order = [customer.last_name for customer in customers]
        
        self.assertEqual(actual_order, expected_order)