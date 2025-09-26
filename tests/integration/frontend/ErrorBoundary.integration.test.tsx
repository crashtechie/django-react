import { render, screen, fireEvent } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import App from '../../../frontend/src/App'

// Mock a component that can throw errors
jest.mock('../../../frontend/src/pages/Dashboard', () => {
  return function MockDashboard() {
    const shouldThrow = new URLSearchParams(window.location.search).get('throwError')
    if (shouldThrow === 'true') {
      throw new Error('Dashboard error for testing')
    }
    return <div>Dashboard loaded successfully</div>
  }
})

describe('ErrorBoundary Integration', () => {
  // Suppress console.error for these tests
  const originalError = console.error
  beforeAll(() => {
    console.error = jest.fn()
  })
  afterAll(() => {
    console.error = originalError
  })

  it('renders app normally when no errors occur', () => {
    render(
      <BrowserRouter>
        <App />
      </BrowserRouter>
    )
    
    expect(screen.getByText('Dashboard loaded successfully')).toBeInTheDocument()
    expect(screen.getByText('Customer Management')).toBeInTheDocument()
  })

  it('catches and displays error when component throws', () => {
    // Mock window.location.search to trigger error
    Object.defineProperty(window, 'location', {
      value: { search: '?throwError=true' },
      writable: true
    })
    
    render(
      <BrowserRouter>
        <App />
      </BrowserRouter>
    )
    
    expect(screen.getByText('Something went wrong')).toBeInTheDocument()
    expect(screen.getByText('We encountered an unexpected error. Please try again.')).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Try again' })).toBeInTheDocument()
  })

  it('recovers from error when retry is clicked', () => {
    // Start with error
    Object.defineProperty(window, 'location', {
      value: { search: '?throwError=true' },
      writable: true
    })
    
    const { rerender } = render(
      <BrowserRouter>
        <App />
      </BrowserRouter>
    )
    
    expect(screen.getByText('Something went wrong')).toBeInTheDocument()
    
    // Click retry and remove error condition
    Object.defineProperty(window, 'location', {
      value: { search: '' },
      writable: true
    })
    
    fireEvent.click(screen.getByRole('button', { name: 'Try again' }))
    
    rerender(
      <BrowserRouter>
        <App />
      </BrowserRouter>
    )
    
    expect(screen.getByText('Dashboard loaded successfully')).toBeInTheDocument()
  })

  it('calls error handler when error occurs', () => {
    const consoleSpy = jest.spyOn(console, 'error').mockImplementation()
    
    Object.defineProperty(window, 'location', {
      value: { search: '?throwError=true' },
      writable: true
    })
    
    render(
      <BrowserRouter>
        <App />
      </BrowserRouter>
    )
    
    expect(consoleSpy).toHaveBeenCalledWith(
      'Application Error:',
      expect.any(Error),
      expect.any(Object)
    )
    
    consoleSpy.mockRestore()
  })
})