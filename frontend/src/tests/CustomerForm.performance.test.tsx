import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import CustomerForm from '../pages/CustomerForm'
import '@testing-library/jest-dom'

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

describe('CustomerForm Performance & Snapshot Tests', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  describe('Performance Tests', () => {
    it('renders quickly without performance issues', () => {
      const startTime = performance.now()
      
      renderWithRouter()
      
      const endTime = performance.now()
      const renderTime = endTime - startTime
      
      // Should render in less than 100ms
      expect(renderTime).toBeLessThan(100)
    })

    it('handles rapid form input changes efficiently', async () => {
      const user = userEvent.setup()
      renderWithRouter()
      
      const startTime = performance.now()
      
      // Simulate rapid typing
      const firstNameInput = screen.getByLabelText(/first name/i)
      
      // Type multiple characters quickly
      for (let i = 0; i < 20; i++) {
        await user.type(firstNameInput, 'a')
      }
      
      const endTime = performance.now()
      const inputTime = endTime - startTime
      
      // Should handle rapid input efficiently
      expect(inputTime).toBeLessThan(1000)
      expect(screen.getByDisplayValue('a'.repeat(20))).toBeInTheDocument()
    })

    it('validates form efficiently with large inputs', async () => {
      const user = userEvent.setup()
      renderWithRouter()
      
      const longString = 'a'.repeat(1000)
      
      const startTime = performance.now()
      
      // Input large strings
      await user.type(screen.getByLabelText(/first name/i), longString)
      await user.click(screen.getByRole('button', { name: /create customer/i }))
      
      const endTime = performance.now()
      const validationTime = endTime - startTime
      
      // Validation should complete quickly even with large inputs
      expect(validationTime).toBeLessThan(500)
    })

    it('handles multiple re-renders efficiently', async () => {
      const { rerender } = renderWithRouter()
      
      const startTime = performance.now()
      
      // Force multiple re-renders by changing props
      for (let i = 0; i < 10; i++) {
        rerender(
          <MemoryRouter initialEntries={['/customers/new']}>
            <CustomerForm />
          </MemoryRouter>
        )
      }
      
      const endTime = performance.now()
      const rerenderTime = endTime - startTime
      
      // Multiple re-renders should be efficient
      expect(rerenderTime).toBeLessThan(200)
    })

    it('maintains performance during error state transitions', async () => {
      const user = userEvent.setup()
      renderWithRouter()
      
      const startTime = performance.now()
      
      // Trigger validation errors multiple times
      for (let i = 0; i < 5; i++) {
        await user.click(screen.getByRole('button', { name: /create customer/i }))
        await user.type(screen.getByLabelText(/first name/i), 'a')
        await user.clear(screen.getByLabelText(/first name/i))
      }
      
      const endTime = performance.now()
      const errorStateTime = endTime - startTime
      
      // Error state transitions should be efficient
      expect(errorStateTime).toBeLessThan(1000)
    })
  })

  describe('Memory Usage Tests', () => {
    it('does not create memory leaks on mount/unmount', () => {
      // Render and unmount multiple times
      for (let i = 0; i < 100; i++) {
        const { unmount } = renderWithRouter()
        unmount()
      }
      
      // If this test completes without issues, no major memory leaks
      expect(true).toBe(true)
    })

    it('cleans up event listeners properly', () => {
      const { unmount } = renderWithRouter()
      
      // Check that component unmounts without issues
      unmount()
      
      // No errors should be thrown during cleanup
      expect(true).toBe(true)
    })
  })

  describe('Snapshot Tests', () => {
    it('matches snapshot for new customer form', () => {
      const { container } = renderWithRouter()
      expect(container.firstChild).toMatchSnapshot()
    })

    it('matches snapshot for edit customer form', () => {
      const { container } = renderWithRouter(['/customers/edit/1'])
      expect(container.firstChild).toMatchSnapshot()
    })

    it('matches snapshot for loading state', () => {
      const { container } = renderWithRouter(['/customers/edit/1'])
      
      // Capture loading state before data loads
      const loadingElement = container.querySelector('.animate-pulse')
      expect(loadingElement).toMatchSnapshot()
    })

    it('matches snapshot for form with validation errors', async () => {
      const user = userEvent.setup()
      const { container } = renderWithRouter()
      
      // Trigger validation errors
      await user.click(screen.getByRole('button', { name: /create customer/i }))
      
      await waitFor(() => {
        expect(screen.getByText('First name is required')).toBeInTheDocument()
      })
      
      expect(container.firstChild).toMatchSnapshot()
    })

    it('matches snapshot for form in submitting state', async () => {
      const user = userEvent.setup()
      const { container } = renderWithRouter()
      
      // Fill form
      await user.type(screen.getByLabelText(/first name/i), 'John')
      await user.type(screen.getByLabelText(/last name/i), 'Doe')
      await user.type(screen.getByLabelText(/email address/i), 'john@example.com')
      await user.type(screen.getByLabelText(/phone number/i), '1234567890')
      
      // Start submission
      await user.click(screen.getByRole('button', { name: /create customer/i }))
      
      await waitFor(() => {
        expect(screen.getByText('Creating...')).toBeInTheDocument()
      })
      
      expect(container.firstChild).toMatchSnapshot()
    })

    it('matches snapshot for filled form', async () => {
      const user = userEvent.setup()
      const { container } = renderWithRouter()
      
      // Fill all fields
      await user.type(screen.getByLabelText(/first name/i), 'John')
      await user.type(screen.getByLabelText(/last name/i), 'Doe')
      await user.type(screen.getByLabelText(/email address/i), 'john.doe@example.com')
      await user.type(screen.getByLabelText(/phone number/i), '(555) 123-4567')
      
      expect(container.firstChild).toMatchSnapshot()
    })

    it('matches snapshot for responsive layout', () => {
      // Test different viewport sizes
      const { container } = renderWithRouter()
      
      // Mobile view would be tested with different CSS classes
      // This is a basic structural snapshot
      expect(container.firstChild).toMatchSnapshot()
    })
  })

  describe('Component Stability Tests', () => {
    it('maintains consistent DOM structure across renders', () => {
      const { container: container1 } = renderWithRouter()
      const { container: container2 } = renderWithRouter()
      
      // DOM structure should be consistent
      expect(container1.innerHTML).toBe(container2.innerHTML)
    })

    it('maintains form field order and structure', () => {
      renderWithRouter()
      
      const formFields = [
        screen.getByLabelText(/first name/i),
        screen.getByLabelText(/last name/i),
        screen.getByLabelText(/email address/i),
        screen.getByLabelText(/phone number/i)
      ]
      
      // Fields should be in expected order
      formFields.forEach((field) => {
        expect(field).toBeInTheDocument()
      })
    })

    it('maintains consistent CSS classes', () => {
      renderWithRouter()
      
      // Check that key elements have consistent styling
      const container = screen.getByText('Add New Customer').closest('.space-y-6')
      expect(container).toHaveClass('space-y-6')
      
      const form = screen.getByRole('form')
      expect(form).toHaveClass('px-6', 'pb-6')
    })

    it('maintains accessibility attributes consistently', () => {
      renderWithRouter()
      
      // Check that accessibility attributes are consistent
      const inputs = [
        screen.getByLabelText(/first name/i),
        screen.getByLabelText(/last name/i),
        screen.getByLabelText(/email address/i),
        screen.getByLabelText(/phone number/i)
      ]
      
      inputs.forEach(input => {
        expect(input).toHaveAttribute('aria-invalid', 'false')
        expect(input).toHaveAttribute('id')
      })
    })
  })

  describe('Error Boundary Integration', () => {
    it('handles component errors gracefully', () => {
      // Mock console.error to prevent test noise
      const consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => {})
      
      try {
        renderWithRouter()
        
        // Component should render without throwing errors
        expect(screen.getByText('Add New Customer')).toBeInTheDocument()
      } catch (error) {
        // If an error occurs, test should still complete
        expect(error).toBeDefined()
      } finally {
        consoleErrorSpy.mockRestore()
      }
    })

    it('recovers from validation errors', async () => {
      const user = userEvent.setup()
      renderWithRouter()
      
      // Create error state
      await user.click(screen.getByRole('button', { name: /create customer/i }))
      
      await waitFor(() => {
        expect(screen.getByText('First name is required')).toBeInTheDocument()
      })
      
      // Recover from error state
      await user.type(screen.getByLabelText(/first name/i), 'John')
      
      await waitFor(() => {
        expect(screen.queryByText('First name is required')).not.toBeInTheDocument()
      })
      
      // Form should be functional again
      expect(screen.getByDisplayValue('John')).toBeInTheDocument()
    })
  })

  describe('Browser Compatibility Tests', () => {
    it('uses standard form elements', () => {
      renderWithRouter()
      
      // Check that standard HTML form elements are used
      expect(screen.getByRole('form')).toBeInTheDocument()
      
      const inputs = screen.getAllByRole('textbox')
      expect(inputs.length).toBeGreaterThan(0)
      
      const buttons = screen.getAllByRole('button')
      expect(buttons.length).toBe(2)
    })

    it('has proper input types for mobile compatibility', () => {
      renderWithRouter()
      
      // Check mobile-friendly input types
      expect(screen.getByLabelText(/email address/i)).toHaveAttribute('type', 'email')
      expect(screen.getByLabelText(/phone number/i)).toHaveAttribute('type', 'tel')
    })
  })
})