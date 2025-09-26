import { describe, it, expect, beforeEach } from '@jest/globals'
import { render, screen } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import Layout from '@/components/Layout'
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
    jest.clearAllMocks()
  })

  it('renders without crashing', () => {
    renderWithRouter(<div>Test Content</div>)
    expect(screen.getByText('Customer Management')).toBeInTheDocument()
  })

  it('renders navigation header', () => {
    renderWithRouter(<div>Test Content</div>)
    
    expect(screen.getByText('Customer Management')).toBeInTheDocument()
    expect(screen.getByText('Dashboard')).toBeInTheDocument()
    expect(screen.getByText('Customers')).toBeInTheDocument()
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
    
    expect(dashboardLink).toHaveAttribute('href', '/')
    expect(customersLink).toHaveAttribute('href', '/customers')
  })

  it('applies correct CSS classes for styling', () => {
    renderWithRouter(<div>Test Content</div>)
    
    const nav = screen.getByRole('navigation')
    const main = screen.getByRole('main')
    
    expect(nav).toHaveClass('bg-white', 'shadow-sm', 'border-b', 'border-gray-200')
    expect(main).toHaveClass('max-w-7xl', 'mx-auto', 'py-6')
  })

  it('renders responsive navigation', () => {
    renderWithRouter(<div>Test Content</div>)
    
    // Check for responsive classes on navigation container
    const navContainer = screen.getByRole('navigation').querySelector('div')
    expect(navContainer).toHaveClass('max-w-7xl', 'mx-auto')
  })
})