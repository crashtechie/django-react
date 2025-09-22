import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import Layout from '../components/Layout'
import '@testing-library/jest-dom'

const renderWithRouter = (children: React.ReactNode) => {
  return render(
    <BrowserRouter>
      <Layout>{children}</Layout>
    </BrowserRouter>
  )
}

describe('Layout', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('renders without crashing', () => {
    renderWithRouter(<div>Test Content</div>)
    expect(screen.getByText('Customer Management System')).toBeInTheDocument()
  })

  it('renders navigation header', () => {
    renderWithRouter(<div>Test Content</div>)
    
    expect(screen.getByText('Customer Management System')).toBeInTheDocument()
    expect(screen.getByText('Dashboard')).toBeInTheDocument()
    expect(screen.getByText('Customers')).toBeInTheDocument()
    expect(screen.getByText('Add Customer')).toBeInTheDocument()
  })

  it('renders children content', () => {
    const testContent = <div data-testid="test-content">Test Content</div>
    renderWithRouter(testContent)
    
    expect(screen.getByTestId('test-content')).toBeInTheDocument()
    expect(screen.getByText('Test Content')).toBeInTheDocument()
  })

  it('has correct navigation links', () => {
    renderWithRouter(<div>Test Content</div>)
    
    const dashboardLink = screen.getByRole('link', { name: 'Dashboard' })
    const customersLink = screen.getByRole('link', { name: 'Customers' })
    const addCustomerLink = screen.getByRole('link', { name: 'Add Customer' })
    
    expect(dashboardLink).toHaveAttribute('href', '/')
    expect(customersLink).toHaveAttribute('href', '/customers')
    expect(addCustomerLink).toHaveAttribute('href', '/customers/new')
  })

  it('applies correct CSS classes for styling', () => {
    renderWithRouter(<div>Test Content</div>)
    
    const header = screen.getByRole('banner')
    const nav = screen.getByRole('navigation')
    const main = screen.getByRole('main')
    
    expect(header).toHaveClass('bg-blue-600', 'text-white', 'shadow-md')
    expect(nav).toBeInTheDocument()
    expect(main).toHaveClass('container', 'mx-auto', 'px-4', 'py-8')
  })

  it('renders responsive navigation', () => {
    renderWithRouter(<div>Test Content</div>)
    
    // Check for responsive classes
    const nav = screen.getByRole('navigation')
    expect(nav).toHaveClass('flex', 'space-x-4')
  })
})