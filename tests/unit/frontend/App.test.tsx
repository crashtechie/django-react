import { describe, it, expect, beforeEach } from '@jest/globals'
import { render, screen } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import App from '@/App'
import '@testing-library/jest-dom'

// Mock the pages since we're testing App routing
jest.mock('@/pages/Dashboard', () => ({
  default: () => <div data-testid="dashboard">Dashboard Page</div>
}))

jest.mock('@/pages/CustomerList', () => ({
  default: () => <div data-testid="customer-list">Customer List Page</div>
}))

jest.mock('@/pages/CustomerDetail', () => ({
  default: () => <div data-testid="customer-detail">Customer Detail Page</div>
}))

jest.mock('@/pages/CustomerForm', () => ({
  default: () => <div data-testid="customer-form">Customer Form Page</div>
}))

jest.mock('@/pages/NotFound', () => ({
  default: () => <div data-testid="not-found">Not Found Page</div>
}))

// Mock the Layout component
jest.mock('@/components/Layout', () => ({
  default: ({ children }: { children: React.ReactNode }) => (
    <div data-testid="layout">
      <nav data-testid="navigation">
        <a href="/">Dashboard</a>
        <a href="/customers">Customers</a>
      </nav>
      <main>{children}</main>
    </div>
  )
}))

const renderWithRouter = (initialRoute = '/') => {
  window.history.pushState({}, 'Test page', initialRoute)
  return render(
    <BrowserRouter>
      <App />
    </BrowserRouter>
  )
}

describe('App', () => {
  beforeEach(() => {
    jest.clearAllMocks()
  })

  it('renders without crashing', () => {
    renderWithRouter()
    expect(screen.getByTestId('layout')).toBeInTheDocument()
  })

  it('renders Dashboard component on root route', () => {
    renderWithRouter('/')
    expect(screen.getByTestId('dashboard')).toBeInTheDocument()
  })

  it('renders CustomerList component on /customers route', () => {
    renderWithRouter('/customers')
    expect(screen.getByTestId('customer-list')).toBeInTheDocument()
  })

  it('renders CustomerForm component on /customers/new route', () => {
    renderWithRouter('/customers/new')
    expect(screen.getByTestId('customer-form')).toBeInTheDocument()
  })

  it('renders CustomerDetail component on /customers/:id route', () => {
    renderWithRouter('/customers/123')
    expect(screen.getByTestId('customer-detail')).toBeInTheDocument()
  })

  it('renders CustomerForm component on /customers/:id/edit route', () => {
    renderWithRouter('/customers/123/edit')
    expect(screen.getByTestId('customer-form')).toBeInTheDocument()
  })

  it('renders NotFound component for unknown routes', () => {
    renderWithRouter('/unknown-route')
    expect(screen.getByTestId('not-found')).toBeInTheDocument()
  })

  it('includes navigation in layout', () => {
    renderWithRouter()
    expect(screen.getByTestId('navigation')).toBeInTheDocument()
    expect(screen.getByText('Dashboard')).toBeInTheDocument()
    expect(screen.getByText('Customers')).toBeInTheDocument()
  })
})