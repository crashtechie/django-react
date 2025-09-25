import { describe, it, expect, beforeEach } from '@jest/globals'
import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import CustomerForm from '../pages/CustomerForm'
import '@testing-library/jest-dom'

// Mock the navigate function
const mockNavigate = vi.fn()

// Mock react-router-dom hooks
vi.mock('react-router-dom', async () => {
  const actual = await vi.importActual('react-router-dom')
  return {
    ...actual,
    useNavigate: () => mockNavigate,
    useParams: () => ({ id: undefined }),
  }
})

// Mock API
vi.mock('../services/api', () => ({
  customerApi: {
    getCustomer: vi.fn().mockResolvedValue({
      id: 1,
      first_name: 'John',
      last_name: 'Doe', 
      email: 'john.doe@example.com',
      phone: '(555) 123-4567'
    }),
    createCustomer: vi.fn().mockResolvedValue({ id: 1 }),
    updateCustomer: vi.fn().mockResolvedValue({ id: 1 }),
  }
}))

// Mock toast
vi.mock('react-hot-toast', () => ({
  default: {
    success: vi.fn(),
    error: vi.fn(),
  }
}))

const renderCustomerForm = () => {
  return render(
    <MemoryRouter>
      <CustomerForm />
    </MemoryRouter>
  )
}

describe('CustomerForm - Fixed Tests', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('renders the form correctly', () => {
    renderCustomerForm()
    
    expect(screen.getByText('Add New Customer')).toBeInTheDocument()
    expect(screen.getByLabelText(/first name/i)).toBeInTheDocument()
    expect(screen.getByLabelText(/last name/i)).toBeInTheDocument()
    expect(screen.getByLabelText(/email address/i)).toBeInTheDocument()
    expect(screen.getByLabelText(/phone number/i)).toBeInTheDocument()
  })

  it('handles form input changes', async () => {
    const user = userEvent.setup()
    renderCustomerForm()
    
    const firstNameInput = screen.getByLabelText(/first name/i)
    await user.type(firstNameInput, 'John')
    
    expect(firstNameInput).toHaveValue('John')
  })

  it('shows validation errors for empty fields', async () => {
    const user = userEvent.setup()
    renderCustomerForm()
    
    const submitButton = screen.getByRole('button', { name: /create customer/i })
    await user.click(submitButton)
    
    await waitFor(() => {
      expect(screen.getByText('First name is required')).toBeInTheDocument()
      expect(screen.getByText('Last name is required')).toBeInTheDocument()
      expect(screen.getByText('Email is required')).toBeInTheDocument()
      expect(screen.getByText('Phone number is required')).toBeInTheDocument()
    })
  })

  it('submits form with valid data', async () => {
    const user = userEvent.setup()
    renderCustomerForm()
    
    // Fill out the form
    await user.type(screen.getByLabelText(/first name/i), 'John')
    await user.type(screen.getByLabelText(/last name/i), 'Doe')
    await user.type(screen.getByLabelText(/email address/i), 'john.doe@example.com')
    await user.type(screen.getByLabelText(/phone number/i), '1234567890')
    
    // Submit the form
    await user.click(screen.getByRole('button', { name: /create customer/i }))
    
    // Should show submitting state
    await waitFor(() => {
      expect(screen.getByText('Creating...')).toBeInTheDocument()
    })
  })

  it('handles cancel button click', async () => {
    const user = userEvent.setup()
    renderCustomerForm()
    
    await user.click(screen.getByRole('button', { name: /cancel/i }))
    
    expect(mockNavigate).toHaveBeenCalledWith('/customers')
  })
})