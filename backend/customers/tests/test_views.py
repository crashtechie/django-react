from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from customers.models import Customer
from decimal import Decimal
import json


class CustomerViewSetTest(APITestCase):
    """Test cases for CustomerViewSet API endpoints."""
    
    def setUp(self):
        """Set up test data."""
        self.client = APIClient()
        
        # Create test customers
        self.customer1 = Customer.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            phone='555-1234',
            address='123 Main St',
            city='Anytown',
            state='NY',
            zip_code='12345',
            subscription_tier='basic',
            monthly_spend=Decimal('50.00')
        )
        
        self.customer2 = Customer.objects.create(
            first_name='Jane',
            last_name='Smith',
            email='jane.smith@example.com',
            phone='555-5678',
            address='456 Oak Ave',
            city='Another City',
            state='CA',
            zip_code='67890',
            subscription_tier='premium',
            monthly_spend=Decimal('150.00'),
            is_active=False
        )
        
        self.valid_customer_data = {
            'first_name': 'Bob',
            'last_name': 'Johnson',
            'email': 'bob.johnson@example.com',
            'phone': '555-9999',
            'address': '789 Pine St',
            'city': 'Test City',
            'state': 'TX',
            'zip_code': '54321',
            'subscription_tier': 'enterprise',
            'monthly_spend': '200.00'
        }
    
    def test_list_customers(self):
        """Test retrieving list of customers."""
        url = reverse('customer-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        
        # Check that customers are ordered by last name
        first_customer = response.data['results'][0]
        self.assertEqual(first_customer['last_name'], 'Doe')
    
    def test_list_customers_pagination(self):
        """Test customer list pagination."""
        # Create more customers to test pagination
        for i in range(15):
            Customer.objects.create(
                first_name=f'Test{i}',
                last_name=f'User{i}',
                email=f'test{i}@example.com'
            )
        
        url = reverse('customer-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertIn('count', response.data)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
    
    def test_retrieve_customer(self):
        """Test retrieving a single customer."""
        url = reverse('customer-detail', args=[self.customer1.pk])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'john.doe@example.com')
        self.assertEqual(response.data['first_name'], 'John')
        self.assertEqual(response.data['last_name'], 'Doe')
    
    def test_create_customer(self):
        """Test creating a new customer."""
        url = reverse('customer-list')
        response = self.client.post(url, self.valid_customer_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 3)
        
        # Verify the created customer
        created_customer = Customer.objects.get(email='bob.johnson@example.com')
        self.assertEqual(created_customer.first_name, 'Bob')
        self.assertEqual(created_customer.subscription_tier, 'enterprise')
    
    def test_create_customer_invalid_data(self):
        """Test creating customer with invalid data."""
        invalid_data = self.valid_customer_data.copy()
        invalid_data['email'] = 'invalid-email'  # Invalid email format
        
        url = reverse('customer-list')
        response = self.client.post(url, invalid_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
    
    def test_create_customer_duplicate_email(self):
        """Test creating customer with duplicate email."""
        duplicate_data = self.valid_customer_data.copy()
        duplicate_data['email'] = self.customer1.email
        
        url = reverse('customer-list')
        response = self.client.post(url, duplicate_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
    
    def test_update_customer(self):
        """Test updating an existing customer."""
        url = reverse('customer-detail', args=[self.customer1.pk])
        update_data = {
            'first_name': 'Johnny',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '555-1234',
            'subscription_tier': 'premium'
        }
        
        response = self.client.put(url, update_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify the update
        self.customer1.refresh_from_db()
        self.assertEqual(self.customer1.first_name, 'Johnny')
        self.assertEqual(self.customer1.subscription_tier, 'premium')
    
    def test_partial_update_customer(self):
        """Test partially updating a customer."""
        url = reverse('customer-detail', args=[self.customer1.pk])
        update_data = {'phone': '555-9999'}
        
        response = self.client.patch(url, update_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify the partial update
        self.customer1.refresh_from_db()
        self.assertEqual(self.customer1.phone, '555-9999')
        self.assertEqual(self.customer1.first_name, 'John')  # Unchanged
    
    def test_delete_customer(self):
        """Test deleting a customer."""
        url = reverse('customer-detail', args=[self.customer1.pk])
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 1)
        
        # Verify customer is deleted
        with self.assertRaises(Customer.DoesNotExist):
            Customer.objects.get(pk=self.customer1.pk)
    
    def test_search_customers(self):
        """Test searching customers by name, email, or phone."""
        url = reverse('customer-list')
        
        # Search by first name
        response = self.client.get(url, {'search': 'John'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['first_name'], 'John')
        
        # Search by email
        response = self.client.get(url, {'search': 'jane.smith'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['email'], 'jane.smith@example.com')
        
        # Search by phone
        response = self.client.get(url, {'search': '555-1234'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_filter_customers_by_active_status(self):
        """Test filtering customers by active status."""
        url = reverse('customer-list')
        
        # Filter for active customers
        response = self.client.get(url, {'is_active': 'true'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['email'], 'john.doe@example.com')
        
        # Filter for inactive customers
        response = self.client.get(url, {'is_active': 'false'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['email'], 'jane.smith@example.com')
    
    def test_ordering_customers(self):
        """Test ordering customers by different fields."""
        url = reverse('customer-list')
        
        # Order by email
        response = self.client.get(url, {'ordering': 'email'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        emails = [customer['email'] for customer in response.data['results']]
        self.assertEqual(emails, sorted(emails))
        
        # Order by created_at descending
        response = self.client.get(url, {'ordering': '-created_at'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should return customers in reverse chronological order
    
    def test_get_active_customers_action(self):
        """Test the custom get_active_customers action."""
        url = reverse('customer-get-active-customers')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertTrue(response.data[0]['is_active'])
    
    def test_get_customer_stats_action(self):
        """Test the custom get_customer_stats action."""
        url = reverse('customer-get-customer-stats')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('total_customers', response.data)
        self.assertIn('active_customers', response.data)
        self.assertIn('inactive_customers', response.data)
        self.assertIn('avg_monthly_spend', response.data)
        
        self.assertEqual(response.data['total_customers'], 2)
        self.assertEqual(response.data['active_customers'], 1)
        self.assertEqual(response.data['inactive_customers'], 1)
    
    def test_nonexistent_customer_retrieve(self):
        """Test retrieving a non-existent customer."""
        url = reverse('customer-detail', args=[9999])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_customer_list_serializer_fields(self):
        """Test that list view uses the correct serializer with limited fields."""
        url = reverse('customer-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        first_customer = response.data['results'][0]
        
        # CustomerListSerializer should have limited fields
        expected_fields = {'id', 'full_name', 'email', 'phone', 'subscription_tier', 'is_active'}
        actual_fields = set(first_customer.keys())
        
        self.assertTrue(expected_fields.issubset(actual_fields))
    
    def test_customer_detail_serializer_fields(self):
        """Test that detail view uses the full CustomerSerializer."""
        url = reverse('customer-detail', args=[self.customer1.pk])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # CustomerSerializer should have all fields
        expected_fields = {
            'id', 'first_name', 'last_name', 'email', 'phone',
            'address', 'city', 'state', 'zip_code', 'subscription_tier',
            'monthly_spend', 'is_active', 'created_at', 'updated_at',
            'full_name', 'full_address'
        }
        actual_fields = set(response.data.keys())
        
        self.assertEqual(actual_fields, expected_fields)