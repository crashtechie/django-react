from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.response import Response
from customers.models import Customer
from decimal import Decimal
from typing import Any, Dict, List

# Type ignore for DRF response.data access - this is a known limitation of DRF type stubs  # type: ignore
# The response.data attribute exists at runtime but isn't properly typed
# pyright: reportAttributeAccessIssue=false


class CustomerViewSetTest(APITestCase):
    """Test cases for CustomerViewSet."""

    def setUp(self):
        """Set up test data."""
        
        # Create test customers
        self.customer1 = Customer.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            phone='555-1234'
        )
        
        self.customer2 = Customer.objects.create(
            first_name='Jane',
            last_name='Smith',
            email='jane.smith@example.com',
            phone='555-5678'
        )
        
        self.customer3 = Customer.objects.create(
            first_name='Bob',
            last_name='Johnson',
            email='bob.johnson@example.com',
            phone='555-9999',
            is_active=False
        )
        
        self.list_url = reverse('customer-list')
        self.detail_url = lambda pk: reverse('customer-detail', kwargs={'pk': pk})
        self.stats_url = reverse('customer-stats')

    def test_list_customers(self):
        """Test retrieving list of customers."""
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)  # type: ignore

    def test_list_customers_pagination(self):
        """Test customer list pagination."""
        # Create more customers to test pagination
        for i in range(25):
            Customer.objects.create(
                first_name=f'Test{i}',
                last_name=f'User{i}',
                email=f'test{i}@example.com',
                phone=f'555-{i:04d}'
            )
        
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 20)  # type: ignore  # Default page size
        self.assertIsNotNone(response.data.get('next'))  # type: ignore

    def test_retrieve_customer(self):
        """Test retrieving a single customer."""
        response = self.client.get(self.detail_url(self.customer1.pk))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'John')  # type: ignore
        self.assertEqual(response.data['email'], 'john.doe@example.com')  # type: ignore

    def test_create_customer(self):
        """Test creating a new customer."""
        new_customer_data = {
            'first_name': 'Alice',
            'last_name': 'Wonder',
            'email': 'alice.wonder@example.com',
            'phone': '555-7777'
        }
        
        response = self.client.post(self.list_url, new_customer_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 4)
        
        # Verify the created customer data
        created_customer = Customer.objects.get(email='alice.wonder@example.com')
        self.assertEqual(created_customer.first_name, 'Alice')
        self.assertEqual(created_customer.last_name, 'Wonder')

    def test_create_customer_invalid_data(self):
        """Test creating customer with invalid data."""
        invalid_data = {
            'first_name': '',  # Required field
            'email': 'invalid-email'  # Invalid format
        }
        
        response = self.client.post(self.list_url, invalid_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('first_name', response.data)  # type: ignore
        self.assertIn('email', response.data)  # type: ignore
        self.assertIn('phone', response.data)  # type: ignore

    def test_create_customer_duplicate_email(self):
        """Test creating customer with duplicate email."""
        duplicate_data = {
            'first_name': 'Duplicate',
            'last_name': 'User',
            'email': 'john.doe@example.com',  # Already exists
            'phone': '555-0000'
        }
        
        response = self.client.post(self.list_url, duplicate_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)  # type: ignore

    def test_update_customer(self):
        """Test updating an existing customer."""
        update_data = {
            'first_name': 'Johnny',
            'last_name': 'Doe',
            'email': 'johnny.doe@example.com',
            'phone': '555-1111'
        }
        
        response = self.client.put(self.detail_url(self.customer1.pk), update_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify the update
        updated_customer = Customer.objects.get(pk=self.customer1.pk)
        self.assertEqual(updated_customer.first_name, 'Johnny')
        self.assertEqual(updated_customer.email, 'johnny.doe@example.com')

    def test_partial_update_customer(self):
        """Test partially updating a customer."""
        partial_data = {
            'phone': '555-9999'
        }
        
        response = self.client.patch(self.detail_url(self.customer1.pk), partial_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify the partial update
        updated_customer = Customer.objects.get(pk=self.customer1.pk)
        self.assertEqual(updated_customer.phone, '555-9999')
        # Original values should remain unchanged
        self.assertEqual(updated_customer.first_name, 'John')
        self.assertEqual(updated_customer.email, 'john.doe@example.com')

    def test_delete_customer(self):
        """Test deleting a customer."""
        response = self.client.delete(self.detail_url(self.customer1.pk))
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 2)

    def test_nonexistent_customer_retrieve(self):
        """Test retrieving a non-existent customer."""
        response = self.client.get(self.detail_url(9999))
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_filter_customers_by_active_status(self):
        """Test filtering customers by active status."""
        # Filter for active customers
        response = self.client.get(self.list_url, {'is_active': 'true'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)  # type: ignore
        
        for customer in response.data['results']:  # type: ignore
            self.assertTrue(customer['is_active'])

        # Filter for inactive customers
        response = self.client.get(self.list_url, {'is_active': 'false'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)  # type: ignore
        self.assertFalse(response.data['results'][0]['is_active'])  # type: ignore

    def test_search_customers(self):
        """Test searching customers by name, email, or phone."""
        # Search by first name
        response = self.client.get(self.list_url, {'search': 'John'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Note: Search also matches 'Johnson' so expecting 2 results
        self.assertEqual(len(response.data['results']), 2)  # type: ignore
        
        # More specific search
        response = self.client.get(self.list_url, {'search': 'john.doe'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)  # type: ignore
        self.assertEqual(response.data['results'][0]['email'], 'john.doe@example.com')  # type: ignore

    def test_ordering_customers(self):
        """Test ordering customers by different fields."""
        # Order by first name
        response = self.client.get(self.list_url, {'ordering': 'first_name'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        names = [customer['full_name'] for customer in response.data['results']]  # type: ignore
        self.assertIn('Bob Johnson', names[0])  # First alphabetically

        # Order by first name descending
        response = self.client.get(self.list_url, {'ordering': '-first_name'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        names = [customer['full_name'] for customer in response.data['results']]  # type: ignore
        self.assertIn('John Doe', names[0])  # Last alphabetically becomes first

    def test_customer_list_serializer_fields(self):
        """Test that list view uses the correct serializer with limited fields."""
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check that response includes expected fields
        customer_data = response.data['results'][0]  # type: ignore
        expected_fields = {'id', 'full_name', 'email', 'phone', 'is_active'}
        self.assertEqual(set(customer_data.keys()), expected_fields)
    
    def test_customer_detail_serializer_fields(self):
        """Test that detail view uses the full CustomerSerializer."""
        response = self.client.get(self.detail_url(self.customer1.pk))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check that response includes all fields
        expected_fields = {
            'id', 'first_name', 'last_name', 'full_name', 
            'email', 'phone', 'is_active', 'created_at', 'updated_at'
        }
        self.assertEqual(set(response.data.keys()), expected_fields)  # type: ignore

    def test_get_customer_stats_action(self):
        """Test the custom stats action."""
        response = self.client.get(self.stats_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total_customers'], 3)  # type: ignore
        self.assertEqual(response.data['active_customers'], 2)  # type: ignore
        self.assertEqual(response.data['inactive_customers'], 1)  # type: ignore

    def test_deactivate_customer_action(self):
        """Test the deactivate action."""
        deactivate_url = reverse('customer-deactivate', kwargs={'pk': self.customer1.pk})
        response = self.client.post(deactivate_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify customer was deactivated
        updated_customer = Customer.objects.get(pk=self.customer1.pk)
        self.assertFalse(updated_customer.is_active)

    def test_activate_customer_action(self):
        """Test the activate action."""
        activate_url = reverse('customer-activate', kwargs={'pk': self.customer3.pk})
        response = self.client.post(activate_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify customer was activated
        updated_customer = Customer.objects.get(pk=self.customer3.pk)
        self.assertTrue(updated_customer.is_active)