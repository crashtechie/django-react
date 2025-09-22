import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import CustomerList from '../pages/CustomerList'
import { customerApi } from '../services/api'
import '@testing-library/jest-dom'

// Mock the API
vi.mock('../services/api')
const mockCustomerApi = vi.mocked(customerApi)

// Mock react-router-dom
const mockNavigate = vi.fn()
vi.mock('react-router-dom', async () => {
  const actual = await vi.importActual('react-router-dom')
  return {
    ...actual,
    useNavigate: () => mockNavigate,
  }
})

const mockCustomers = [
  {
    id: 1,
    first_name: 'John',
    last_name: 'Doe',
    full_name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '555-1234',
    is_active: true,
    created_at: '2024-01-01T00:00:00Z',
    updated_at: '2024-01-01T00:00:00Z'
  },
  {
    id: 2,
    first_name: 'Jane',
    last_name: 'Smith',
    full_name: 'Jane Smith',
    email: 'jane.smith@example.com',
    phone: '555-5678',
    is_active: false,
    created_at: '2024-01-02T00:00:00Z',
    updated_at: '2024-01-02T00:00:00Z'
  }
]

const mockPaginatedResponse = {
  results: mockCustomers,
  count: 2,
  next: null,
  previous: null
}

const renderWithRouter = () => {
  return render(
    <BrowserRouter>
      <CustomerList />
    </BrowserRouter>
  )
}

describe('CustomerList', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    mockCustomerApi.getCustomers.mockResolvedValue(mockPaginatedResponse)
  })

  it('renders loading state initially', () => {
    renderWithRouter()
    expect(screen.getByText('Loading customers...')).toBeInTheDocument()
  })

  it('renders customer list after loading', async () => {
    renderWithRouter()

    await waitFor(() => {
      expect(screen.getByText('Customer Management')).toBeInTheDocument()
    })

    expect(screen.getByText('John Doe')).toBeInTheDocument()
    expect(screen.getByText('john.doe@example.com')).toBeInTheDocument()
    expect(screen.getByText('Jane Smith')).toBeInTheDocument()
    expect(screen.getByText('jane.smith@example.com')).toBeInTheDocument()
  })

  it('displays search input', async () => {
    renderWithRouter()

    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search customers...')).toBeInTheDocument()
    })
  })

  it('handles search input', async () => {
    renderWithRouter()

    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search customers...')).toBeInTheDocument()
    })

    const searchInput = screen.getByPlaceholderText('Search customers...')
    fireEvent.change(searchInput, { target: { value: 'John' } })

    await waitFor(() => {
      expect(mockCustomerApi.getCustomers).toHaveBeenCalledWith(
        expect.objectContaining({ search: 'John' })
      )
    })
  })

  it('displays add customer button', async () => {
    renderWithRouter()

    await waitFor(() => {
      expect(screen.getByText('Add Customer')).toBeInTheDocument()
    })

    const addButton = screen.getByText('Add Customer')
    expect(addButton.closest('a')).toHaveAttribute('href', '/customers/new')
  })

  it('displays active/inactive status', async () => {
    renderWithRouter()

    await waitFor(() => {
      expect(screen.getByText('Active')).toBeInTheDocument()
      expect(screen.getByText('Inactive')).toBeInTheDocument()
    })
  })

  it('handles API error', async () => {
    mockCustomerApi.getCustomers.mockRejectedValueOnce(new Error('API Error'))
    renderWithRouter()

    await waitFor(() => {
      expect(screen.getByText('Error loading customers. Please try again.')).toBeInTheDocument()
    })
  })

  it('shows empty state when no customers', async () => {
    mockCustomerApi.getCustomers.mockResolvedValueOnce({
      results: [],
      count: 0,
      next: null,
      previous: null
    })

    renderWithRouter()

    await waitFor(() => {
      expect(screen.getByText('No customers found')).toBeInTheDocument()
    })
  })

  it('handles filter by active status', async () => {
    renderWithRouter()

    await waitFor(() => {
      expect(screen.getByText('All')).toBeInTheDocument()
    })

    // Find and click the Active filter
    const activeFilter = screen.getByText('Active')
    fireEvent.click(activeFilter)

    await waitFor(() => {
      expect(mockCustomerApi.getCustomers).toHaveBeenCalledWith(
        expect.objectContaining({ is_active: true })
      )
    })
  })

  it('navigates to customer detail when clicking on customer', async () => {
    renderWithRouter()

    await waitFor(() => {
      expect(screen.getByText('John Doe')).toBeInTheDocument()
    })

    const customerRow = screen.getByText('John Doe').closest('tr')
    if (customerRow) {
      fireEvent.click(customerRow)
      expect(mockNavigate).toHaveBeenCalledWith('/customers/1')
    }
  })

  it('displays pagination when there are multiple pages', async () => {
    const mockPaginatedResponseWithNext = {
      ...mockPaginatedResponse,
      next: 'http://localhost/api/customers/?page=2',
      count: 20
    }

    mockCustomerApi.getCustomers.mockResolvedValueOnce(mockPaginatedResponseWithNext)
    renderWithRouter()

    await waitFor(() => {
      expect(screen.getByText('Next')).toBeInTheDocument()
    })
  })
})