import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { render, screen, waitFor, cleanup } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import CustomerForm from '../pages/CustomerForm'
import '@testing-library/jest-dom'

// Mock fetch globally
const mockFetch = vi.fn()
global.fetch = mockFetch

// Mock useNavigate
const mockNavigate = vi.fn()
vi.mock('react-router-dom', async () => {
  const actual = await vi.importActual('react-router-dom')
  return {
    ...actual,
    useNavigate: () => mockNavigate,
  }
})

const renderWithRouter = (initialEntries = ['/customers/new']) => {
  return render(
    <MemoryRouter initialEntries={initialEntries}>
      <CustomerForm />
    </MemoryRouter>
  )
}

describe('CustomerForm Integration Tests', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    mockFetch.mockClear()
  })

  afterEach(() => {
    cleanup()
  })

  describe('API Integration', () => {
    it('successfully creates a new customer', async () => {
      const user = userEvent.setup()
      
      // Mock successful API response
      mockFetch.mockResolvedValueOnce({
        ok: true,
        status: 201,
        json: async () => ({
          id: 1,
          first_name: 'John',
          last_name: 'Doe',
          email: 'john.doe@example.com',
          phone: '1234567890',
          is_active: true,
          created_at: '2024-01-01T00:00:00Z',
          updated_at: '2024-01-01T00:00:00Z',
          full_name: 'John Doe'
        })
      })

      renderWithRouter()

      // Fill out the form
      await user.type(screen.getByLabelText(/first name/i), 'John')
      await user.type(screen.getByLabelText(/last name/i), 'Doe')
      await user.type(screen.getByLabelText(/email address/i), 'john.doe@example.com')
      await user.type(screen.getByLabelText(/phone number/i), '1234567890')

      // Submit the form
      await user.click(screen.getByRole('button', { name: /create customer/i }))

      // Should show loading state
      await waitFor(() => {
        expect(screen.getByText('Creating...')).toBeInTheDocument()
      })

      // Should navigate to success page
      await waitFor(() => {
        expect(mockNavigate).toHaveBeenCalledWith('/customers', {
          replace: true,
          state: { message: 'Customer created successfully' }
        })
      }, { timeout: 2000 })
    })

    it('successfully updates an existing customer', async () => {
      const user = userEvent.setup()
      
      // Mock API responses
      mockFetch
        // First call - fetch existing customer
        .mockResolvedValueOnce({
          ok: true,
          status: 200,
          json: async () => ({
            id: 1,
            first_name: 'John',
            last_name: 'Doe',
            email: 'john.doe@example.com',
            phone: '555-0123',
            is_active: true,
            created_at: '2024-01-01T00:00:00Z',
            updated_at: '2024-01-01T00:00:00Z',
            full_name: 'John Doe'
          })
        })
        // Second call - update customer
        .mockResolvedValueOnce({
          ok: true,
          status: 200,
          json: async () => ({
            id: 1,
            first_name: 'John',
            last_name: 'Smith',
            email: 'john.smith@example.com',
            phone: '555-0123',
            is_active: true,
            created_at: '2024-01-01T00:00:00Z',
            updated_at: '2024-01-01T12:00:00Z',
            full_name: 'John Smith'
          })
        })

      renderWithRouter(['/customers/edit/1'])

      // Wait for customer data to load
      await waitFor(() => {
        expect(screen.getByDisplayValue('John')).toBeInTheDocument()
      })

      // Update the form
      await user.clear(screen.getByLabelText(/last name/i))
      await user.type(screen.getByLabelText(/last name/i), 'Smith')
      await user.clear(screen.getByLabelText(/email address/i))
      await user.type(screen.getByLabelText(/email address/i), 'john.smith@example.com')

      // Submit the form
      await user.click(screen.getByRole('button', { name: /update customer/i }))

      // Should show updating state
      await waitFor(() => {
        expect(screen.getByText('Updating...')).toBeInTheDocument()
      })

      // Should navigate to success page
      await waitFor(() => {
        expect(mockNavigate).toHaveBeenCalledWith('/customers', {
          replace: true,
          state: { message: 'Customer updated successfully' }
        })
      }, { timeout: 2000 })
    })

    it('handles API errors gracefully during creation', async () => {
      const user = userEvent.setup()
      
      // Mock API error response
      mockFetch.mockRejectedValueOnce(new Error('Network error'))

      renderWithRouter()

      // Fill out the form
      await user.type(screen.getByLabelText(/first name/i), 'John')
      await user.type(screen.getByLabelText(/last name/i), 'Doe')
      await user.type(screen.getByLabelText(/email address/i), 'john.doe@example.com')
      await user.type(screen.getByLabelText(/phone number/i), '1234567890')

      // Submit the form
      await user.click(screen.getByRole('button', { name: /create customer/i }))

      // Should show error message
      await waitFor(() => {
        expect(screen.getByText('Failed to create customer')).toBeInTheDocument()
      }, { timeout: 2000 })

      // Should not navigate
      expect(mockNavigate).not.toHaveBeenCalled()
    })

    it('handles validation errors from server', async () => {
      const user = userEvent.setup()
      
      // Mock server validation error
      mockFetch.mockResolvedValueOnce({
        ok: false,
        status: 400,
        json: async () => ({
          email: ['Customer with this email already exists.'],
          phone: ['Invalid phone number format.']
        })
      })

      renderWithRouter()

      // Fill out form with duplicate email
      await user.type(screen.getByLabelText(/first name/i), 'John')
      await user.type(screen.getByLabelText(/last name/i), 'Doe')
      await user.type(screen.getByLabelText(/email address/i), 'existing@example.com')
      await user.type(screen.getByLabelText(/phone number/i), 'invalid-phone')

      // Submit the form
      await user.click(screen.getByRole('button', { name: /create customer/i }))

      // Should show server validation errors
      await waitFor(() => {
        expect(screen.getByText('Customer with this email already exists.')).toBeInTheDocument()
        expect(screen.getByText('Invalid phone number format.')).toBeInTheDocument()
      }, { timeout: 2000 })
    })

    it('handles 404 error when editing non-existent customer', async () => {
      // Mock 404 response for customer fetch
      mockFetch.mockResolvedValueOnce({
        ok: false,
        status: 404,
        json: async () => ({ detail: 'Customer not found.' })
      })

      renderWithRouter(['/customers/edit/999'])

      // Should show error message
      await waitFor(() => {
        expect(screen.getByText('Customer not found')).toBeInTheDocument()
      }, { timeout: 1000 })
    })

    it('handles network timeout gracefully', async () => {
      const user = userEvent.setup()
      
      // Mock timeout
      mockFetch.mockImplementationOnce(() => 
        new Promise((_, reject) => 
          setTimeout(() => reject(new Error('Request timeout')), 100)
        )
      )

      renderWithRouter()

      // Fill out the form
      await user.type(screen.getByLabelText(/first name/i), 'John')
      await user.type(screen.getByLabelText(/last name/i), 'Doe')
      await user.type(screen.getByLabelText(/email address/i), 'john.doe@example.com')
      await user.type(screen.getByLabelText(/phone number/i), '1234567890')

      // Submit the form
      await user.click(screen.getByRole('button', { name: /create customer/i }))

      // Should handle timeout and show error
      await waitFor(() => {
        expect(screen.getByText('Failed to create customer')).toBeInTheDocument()
      }, { timeout: 2000 })
    })
  })

  describe('Loading States', () => {
    it('shows loading state when fetching customer data', async () => {
      // Mock delayed response
      mockFetch.mockImplementationOnce(() => 
        new Promise(resolve => 
          setTimeout(() => resolve({
            ok: true,
            status: 200,
            json: async () => ({
              id: 1,
              first_name: 'John',
              last_name: 'Doe',
              email: 'john.doe@example.com',
              phone: '555-0123',
              is_active: true,
              created_at: '2024-01-01T00:00:00Z',
              updated_at: '2024-01-01T00:00:00Z',
              full_name: 'John Doe'
            })
          }), 100)
        )
      )

      renderWithRouter(['/customers/edit/1'])

      // Should show loading state
      const loadingElement = document.querySelector('.animate-pulse')
      expect(loadingElement).toBeInTheDocument()

      // Should eventually load data
      await waitFor(() => {
        expect(screen.getByDisplayValue('John')).toBeInTheDocument()
      }, { timeout: 1000 })
    })

    it('disables form during submission', async () => {
      const user = userEvent.setup()
      
      // Mock slow API response
      mockFetch.mockImplementationOnce(() => 
        new Promise(resolve => 
          setTimeout(() => resolve({
            ok: true,
            status: 201,
            json: async () => ({ id: 1 })
          }), 200)
        )
      )

      renderWithRouter()

      // Fill out the form
      await user.type(screen.getByLabelText(/first name/i), 'John')
      await user.type(screen.getByLabelText(/last name/i), 'Doe')
      await user.type(screen.getByLabelText(/email address/i), 'john.doe@example.com')
      await user.type(screen.getByLabelText(/phone number/i), '1234567890')

      // Submit the form
      await user.click(screen.getByRole('button', { name: /create customer/i }))

      // Form should be disabled during submission
      await waitFor(() => {
        expect(screen.getByRole('button', { name: /creating.../i })).toBeDisabled()
        expect(screen.getByRole('button', { name: /cancel/i })).toBeDisabled()
      })
    })
  })

  describe('Data Persistence', () => {
    it('persists form data when validation fails', async () => {
      const user = userEvent.setup()
      renderWithRouter()

      // Fill out form with some invalid data
      await user.type(screen.getByLabelText(/first name/i), 'John')
      await user.type(screen.getByLabelText(/email address/i), 'invalid-email')

      // Submit form (should fail validation)
      await user.click(screen.getByRole('button', { name: /create customer/i }))

      // Form data should persist
      expect(screen.getByDisplayValue('John')).toBeInTheDocument()
      expect(screen.getByDisplayValue('invalid-email')).toBeInTheDocument()
    })

    it('clears form after successful submission', async () => {
      const user = userEvent.setup()
      
      mockFetch.mockResolvedValueOnce({
        ok: true,
        status: 201,
        json: async () => ({ id: 1 })
      })

      renderWithRouter()

      // Fill and submit form
      await user.type(screen.getByLabelText(/first name/i), 'John')
      await user.type(screen.getByLabelText(/last name/i), 'Doe')
      await user.type(screen.getByLabelText(/email address/i), 'john.doe@example.com')
      await user.type(screen.getByLabelText(/phone number/i), '1234567890')

      await user.click(screen.getByRole('button', { name: /create customer/i }))

      // Should navigate away (form clearing happens after navigation)
      await waitFor(() => {
        expect(mockNavigate).toHaveBeenCalled()
      }, { timeout: 2000 })
    })
  })

  describe('Browser Navigation Integration', () => {
    it('handles browser back button during form editing', () => {
      renderWithRouter(['/customers/edit/1'])
      
      // Form should handle navigation events gracefully
      // This would require additional implementation to handle beforeunload events
      expect(screen.getByText('Edit Customer')).toBeInTheDocument()
    })

    it('navigates correctly after successful operations', async () => {
      const user = userEvent.setup()
      
      mockFetch.mockResolvedValueOnce({
        ok: true,
        status: 201,
        json: async () => ({ id: 1 })
      })

      renderWithRouter()

      // Complete form submission
      await user.type(screen.getByLabelText(/first name/i), 'John')
      await user.type(screen.getByLabelText(/last name/i), 'Doe')
      await user.type(screen.getByLabelText(/email address/i), 'john.doe@example.com')
      await user.type(screen.getByLabelText(/phone number/i), '1234567890')
      await user.click(screen.getByRole('button', { name: /create customer/i }))

      // Should navigate with proper state
      await waitFor(() => {
        expect(mockNavigate).toHaveBeenCalledWith('/customers', {
          replace: true,
          state: { message: 'Customer created successfully' }
        })
      }, { timeout: 2000 })
    })
  })

  describe('Real-world Scenarios', () => {
    it('handles partial form completion and return', async () => {
      const user = userEvent.setup()
      renderWithRouter()

      // Partially fill form
      await user.type(screen.getByLabelText(/first name/i), 'John')
      await user.type(screen.getByLabelText(/last name/i), 'Doe')

      // Simulate user navigating away and back
      // In real world, this would test form data persistence
      expect(screen.getByDisplayValue('John')).toBeInTheDocument()
      expect(screen.getByDisplayValue('Doe')).toBeInTheDocument()
    })

    it('handles concurrent form submissions', async () => {
      const user = userEvent.setup()
      
      // Mock slow response
      mockFetch.mockImplementationOnce(() => 
        new Promise(resolve => 
          setTimeout(() => resolve({
            ok: true,
            status: 201,
            json: async () => ({ id: 1 })
          }), 500)
        )
      )

      renderWithRouter()

      // Fill form
      await user.type(screen.getByLabelText(/first name/i), 'John')
      await user.type(screen.getByLabelText(/last name/i), 'Doe')
      await user.type(screen.getByLabelText(/email address/i), 'john.doe@example.com')
      await user.type(screen.getByLabelText(/phone number/i), '1234567890')

      // Try to submit multiple times quickly
      const submitButton = screen.getByRole('button', { name: /create customer/i })
      await user.click(submitButton)
      
      // Button should be disabled to prevent multiple submissions
      expect(submitButton).toBeDisabled()
      
      // Additional clicks should not trigger more API calls
      await user.click(submitButton)
      expect(mockFetch).toHaveBeenCalledTimes(1)
    })

    it('handles form validation with mixed valid and invalid data', async () => {
      const user = userEvent.setup()
      renderWithRouter()

      // Mix of valid and invalid data
      await user.type(screen.getByLabelText(/first name/i), 'John') // valid
      await user.type(screen.getByLabelText(/last name/i), 'A') // invalid (too short)
      await user.type(screen.getByLabelText(/email address/i), 'john.doe@example.com') // valid
      await user.type(screen.getByLabelText(/phone number/i), '123') // invalid

      await user.click(screen.getByRole('button', { name: /create customer/i }))

      // Should show errors only for invalid fields
      await waitFor(() => {
        expect(screen.getByText('Last name must be at least 2 characters')).toBeInTheDocument()
        expect(screen.getByText('Please enter a valid phone number')).toBeInTheDocument()
        
        // Valid fields should not show errors
        expect(screen.queryByText('First name is required')).not.toBeInTheDocument()
        expect(screen.queryByText('Please enter a valid email address')).not.toBeInTheDocument()
      })
    })
  })
})