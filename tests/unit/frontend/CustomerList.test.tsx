import { describe, it, expect, beforeEach } from '@jest/globals'
import { render, screen } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import CustomerList from '@/pages/CustomerList'
import '@testing-library/jest-dom'

const renderWithRouter = () => {
  return render(
    <BrowserRouter>
      <CustomerList />
    </BrowserRouter>
  )
}

describe('CustomerList', () => {
  beforeEach(() => {
    jest.clearAllMocks()
  })

  it('renders the customer list page title', () => {
    renderWithRouter()
    expect(screen.getByText('Customers')).toBeInTheDocument()
  })

  it('renders the customer list description', () => {
    renderWithRouter()
    expect(screen.getByText('A list of all customers in your account including their name, email, and phone number.')).toBeInTheDocument()
  })

  it('displays add customer button', () => {
    renderWithRouter()
    const addButton = screen.getByText('Add Customer')
    expect(addButton).toBeInTheDocument()
    expect(addButton.closest('a')).toHaveAttribute('href', '/customers/new')
  })

  it('shows placeholder message', () => {
    renderWithRouter()
    expect(screen.getByText('Customer list will be implemented here...')).toBeInTheDocument()
  })

  it('renders with correct CSS structure', () => {
    renderWithRouter()
    
    // Check for main container
    const container = screen.getByText('Customers').closest('.space-y-6')
    expect(container).toBeInTheDocument()
    
    // Check for add customer button styling
    const addButton = screen.getByText('Add Customer')
    expect(addButton).toHaveClass('btn', 'btn-primary')
  })
})