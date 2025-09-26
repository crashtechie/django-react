import { render, screen, fireEvent } from '@testing-library/react'
import ErrorFallback from '../../../../../frontend/src/components/ui/ErrorFallback'

describe('ErrorFallback', () => {
  it('renders with default props', () => {
    render(<ErrorFallback />)
    
    expect(screen.getByText('Something went wrong')).toBeInTheDocument()
    expect(screen.getByText('We encountered an unexpected error. Please try again.')).toBeInTheDocument()
    expect(screen.getByRole('alert')).toBeInTheDocument()
  })

  it('renders with custom title and message', () => {
    render(
      <ErrorFallback 
        title="Custom Error Title"
        message="Custom error message"
      />
    )
    
    expect(screen.getByText('Custom Error Title')).toBeInTheDocument()
    expect(screen.getByText('Custom error message')).toBeInTheDocument()
  })

  it('renders retry button when resetError is provided', () => {
    const resetError = jest.fn()
    
    render(<ErrorFallback resetError={resetError} />)
    
    const retryButton = screen.getByRole('button', { name: 'Try again' })
    expect(retryButton).toBeInTheDocument()
    
    fireEvent.click(retryButton)
    expect(resetError).toHaveBeenCalledTimes(1)
  })

  it('does not render retry button when resetError is not provided', () => {
    render(<ErrorFallback />)
    
    expect(screen.queryByRole('button', { name: 'Try again' })).not.toBeInTheDocument()
  })

  it('shows error details in development mode', () => {
    const originalEnv = process.env.NODE_ENV
    process.env.NODE_ENV = 'development'
    
    const error = new Error('Test error message')
    error.stack = 'Error stack trace'
    
    render(<ErrorFallback error={error} />)
    
    expect(screen.getByText('Error Details (Development)')).toBeInTheDocument()
    expect(screen.getByText('Test error message')).toBeInTheDocument()
    
    process.env.NODE_ENV = originalEnv
  })

  it('hides error details in production mode', () => {
    const originalEnv = process.env.NODE_ENV
    process.env.NODE_ENV = 'production'
    
    const error = new Error('Test error message')
    
    render(<ErrorFallback error={error} />)
    
    expect(screen.queryByText('Error Details (Development)')).not.toBeInTheDocument()
    expect(screen.queryByText('Test error message')).not.toBeInTheDocument()
    
    process.env.NODE_ENV = originalEnv
  })

  it('has proper accessibility attributes', () => {
    render(<ErrorFallback />)
    
    const alertElement = screen.getByRole('alert')
    expect(alertElement).toBeInTheDocument()
    
    const icon = screen.getByRole('img', { hidden: true })
    expect(icon).toHaveAttribute('aria-hidden', 'true')
  })

  it('expands error details when clicked in development', () => {
    const originalEnv = process.env.NODE_ENV
    process.env.NODE_ENV = 'development'
    
    const error = new Error('Test error message')
    error.stack = 'Error stack trace'
    
    render(<ErrorFallback error={error} />)
    
    const summary = screen.getByText('Error Details (Development)')
    fireEvent.click(summary)
    
    expect(screen.getByText(/Error stack trace/)).toBeInTheDocument()
    
    process.env.NODE_ENV = originalEnv
  })
})