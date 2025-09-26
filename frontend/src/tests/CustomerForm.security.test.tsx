import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { BrowserRouter } from 'react-router-dom'
import CustomerForm from '../pages/CustomerForm'
import { customerApi } from '../services/api'
import { toast } from 'react-hot-toast'

// Mock dependencies
jest.mock('../services/api')
jest.mock('react-hot-toast')

const mockedCustomerApi = customerApi as jest.Mocked<typeof customerApi>
const mockedToast = toast as jest.Mocked<typeof toast>

const renderCustomerForm = () => {
  return render(
    <BrowserRouter>
      <CustomerForm />
    </BrowserRouter>
  )
}

describe('CustomerForm XSS Security Tests', () => {
  beforeEach(() => {
    jest.clearAllMocks()
    mockedToast.error = jest.fn()
  })

  describe('Input Validation Security', () => {
    it('should reject XSS attempts in first name', async () => {
      renderCustomerForm()
      
      const user = userEvent.setup()
      const xssPayload = '<script>alert("XSS")</script>'
      
      await user.type(screen.getByLabelText(/first name/i), xssPayload)
      await user.type(screen.getByLabelText(/last name/i), 'Doe')
      await user.type(screen.getByLabelText(/email address/i), 'test@example.com')
      await user.type(screen.getByLabelText(/phone number/i), '1234567890')
      
      await user.click(screen.getByRole('button', { name: /create customer/i }))

      await waitFor(() => {
        expect(screen.getByText('First name contains invalid characters or format')).toBeInTheDocument()
      })
    })

    it('should reject XSS attempts in last name', async () => {
      renderCustomerForm()
      
      const user = userEvent.setup()
      const xssPayload = '<img src="x" onerror="alert(1)">'
      
      await user.type(screen.getByLabelText(/first name/i), 'John')
      await user.type(screen.getByLabelText(/last name/i), xssPayload)
      await user.type(screen.getByLabelText(/email address/i), 'test@example.com')
      await user.type(screen.getByLabelText(/phone number/i), '1234567890')
      
      await user.click(screen.getByRole('button', { name: /create customer/i }))

      await waitFor(() => {
        expect(screen.getByText('Last name contains invalid characters or format')).toBeInTheDocument()
      })
    })

    it('should reject malicious javascript URLs in email', async () => {
      renderCustomerForm()
      
      const user = userEvent.setup()
      const maliciousEmail = 'test@javascript:alert(1).com'
      
      await user.type(screen.getByLabelText(/first name/i), 'John')
      await user.type(screen.getByLabelText(/last name/i), 'Doe')
      await user.type(screen.getByLabelText(/email address/i), maliciousEmail)
      await user.type(screen.getByLabelText(/phone number/i), '1234567890')
      
      await user.click(screen.getByRole('button', { name: /create customer/i }))

      await waitFor(() => {
        expect(screen.getByText('Please enter a valid email address')).toBeInTheDocument()
      })
    })

    it('should reject script tags in phone numbers', async () => {
      renderCustomerForm()
      
      const user = userEvent.setup()
      const maliciousPhone = '555<script>alert(1)</script>1234'
      
      await user.type(screen.getByLabelText(/first name/i), 'John')
      await user.type(screen.getByLabelText(/last name/i), 'Doe')
      await user.type(screen.getByLabelText(/email address/i), 'test@example.com')
      await user.type(screen.getByLabelText(/phone number/i), maliciousPhone)
      
      await user.click(screen.getByRole('button', { name: /create customer/i }))

      await waitFor(() => {
        expect(screen.getByText('Please enter a valid phone number')).toBeInTheDocument()
      })
    })

    it('should accept safe input values', async () => {
      mockedCustomerApi.createCustomer.mockResolvedValue({ id: 1 })
      
      renderCustomerForm()
      
      const user = userEvent.setup()
      
      await user.type(screen.getByLabelText(/first name/i), "John O'Connor")
      await user.type(screen.getByLabelText(/last name/i), 'Smith-Jones')
      await user.type(screen.getByLabelText(/email address/i), 'john.smith@example.com')
      await user.type(screen.getByLabelText(/phone number/i), '(555) 123-4567')
      
      await user.click(screen.getByRole('button', { name: /create customer/i }))

      await waitFor(() => {
        expect(mockedCustomerApi.createCustomer).toHaveBeenCalled()
      })
    })
  })

  describe('Error Message Sanitization', () => {
    it('should sanitize XSS attempts in API error messages', async () => {
      // Mock API to return an error with XSS payload
      const xssPayload = '<script>alert("XSS")</script>'
      const maliciousError = {
        response: {
          data: {
            detail: xssPayload
          }
        }
      }

      mockedCustomerApi.createCustomer.mockRejectedValue(maliciousError)

      renderCustomerForm()
      
      // Fill out form with valid data
      const user = userEvent.setup()
      await user.type(screen.getByLabelText(/first name/i), 'John')
      await user.type(screen.getByLabelText(/last name/i), 'Doe')
      await user.type(screen.getByLabelText(/email address/i), 'john@example.com')
      await user.type(screen.getByLabelText(/phone number/i), '1234567890')
      
      // Submit form to trigger error
      await user.click(screen.getByRole('button', { name: /create customer/i }))

      await waitFor(() => {
        // The error message should be sanitized (HTML entities instead of raw script tags)
        expect(screen.getByRole('alert')).toHaveTextContent('&lt;script&gt;alert("XSS")&lt;/script&gt;')
        // The raw script tag should NOT be present
        expect(screen.queryByText(xssPayload)).not.toBeInTheDocument()
      })
    })

    it('should sanitize complex XSS payloads in error messages', async () => {
      // Mock API to return complex XSS payload
      const complexXssPayload = '<img src="x" onerror="alert(\'XSS\')" /><svg onload="alert(1)">'
      const maliciousError = {
        response: {
          data: {
            detail: complexXssPayload
          }
        }
      }

      mockedCustomerApi.createCustomer.mockRejectedValue(maliciousError)

      renderCustomerForm()
      
      // Fill out form with valid data
      const user = userEvent.setup()
      await user.type(screen.getByLabelText(/first name/i), 'Jane')
      await user.type(screen.getByLabelText(/last name/i), 'Smith')
      await user.type(screen.getByLabelText(/email address/i), 'jane@example.com')
      await user.type(screen.getByLabelText(/phone number/i), '0987654321')
      
      // Submit form to trigger error
      await user.click(screen.getByRole('button', { name: /create customer/i }))

      await waitFor(() => {
        const alertElement = screen.getByRole('alert')
        const alertText = alertElement.textContent || ''
        
        // Should contain sanitized version with HTML entities
        expect(alertText).toContain('&lt;img')
        expect(alertText).toContain('&gt;')
        expect(alertText).toContain('&quot;')
        expect(alertText).toContain('&#x27;')
        
        // Should NOT contain executable script tags
        expect(alertElement.innerHTML).not.toContain('<img')
        expect(alertElement.innerHTML).not.toContain('<svg')
        expect(alertElement.innerHTML).not.toContain('onerror=')
        expect(alertElement.innerHTML).not.toContain('onload=')
      })
    })

    it('should handle safe error messages without over-sanitization', async () => {
      // Test that normal error messages work correctly
      const safeError = {
        response: {
          data: {
            detail: 'This customer email already exists'
          }
        }
      }

      mockedCustomerApi.createCustomer.mockRejectedValue(safeError)

      renderCustomerForm()
      
      // Fill out form with valid data
      const user = userEvent.setup()
      await user.type(screen.getByLabelText(/first name/i), 'Bob')
      await user.type(screen.getByLabelText(/last name/i), 'Wilson')
      await user.type(screen.getByLabelText(/email address/i), 'bob@example.com')
      await user.type(screen.getByLabelText(/phone number/i), '5551234567')
      
      // Submit form to trigger error
      await user.click(screen.getByRole('button', { name: /create customer/i }))

      await waitFor(() => {
        // Safe error message should be displayed normally
        expect(screen.getByRole('alert')).toHaveTextContent('This customer email already exists')
      })
    })
  })

  describe('Fallback Error Messages', () => {
    it('should sanitize fallback error messages', async () => {
      // Mock API to return error without detail field - should use fallback
      const maliciousError = {
        response: {
          data: {}
        }
      }

      mockedCustomerApi.createCustomer.mockRejectedValue(maliciousError)

      renderCustomerForm()
      
      // Fill out form and submit
      const user = userEvent.setup()
      await user.type(screen.getByLabelText(/first name/i), 'Test')
      await user.type(screen.getByLabelText(/last name/i), 'User')
      await user.type(screen.getByLabelText(/email address/i), 'test@example.com')
      await user.type(screen.getByLabelText(/phone number/i), '1111111111')
      
      await user.click(screen.getByRole('button', { name: /create customer/i }))

      await waitFor(() => {
        // Should show safe fallback message
        expect(screen.getByRole('alert')).toHaveTextContent('Failed to create customer')
      })
    })
  })
})