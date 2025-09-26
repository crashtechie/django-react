import { render, screen } from '@testing-library/react'
import LoadingSpinner from '../components/ui/LoadingSpinner'

describe('LoadingSpinner', () => {
  it('renders with default props', () => {
    render(<LoadingSpinner />)
    
    const spinner = screen.getByRole('status')
    expect(spinner).toBeInTheDocument()
    expect(spinner).toHaveAttribute('aria-label', 'Loading')
  })

  it('applies correct size classes', () => {
    const { rerender } = render(<LoadingSpinner size="small" />)
    expect(screen.getByRole('status')).toHaveClass('w-4 h-4')

    rerender(<LoadingSpinner size="medium" />)
    expect(screen.getByRole('status')).toHaveClass('w-6 h-6')

    rerender(<LoadingSpinner size="large" />)
    expect(screen.getByRole('status')).toHaveClass('w-8 h-8')
  })

  it('applies correct color classes', () => {
    const { rerender } = render(<LoadingSpinner color="primary" />)
    expect(screen.getByRole('status')).toHaveClass('text-blue-600')

    rerender(<LoadingSpinner color="white" />)
    expect(screen.getByRole('status')).toHaveClass('text-white')

    rerender(<LoadingSpinner color="gray" />)
    expect(screen.getByRole('status')).toHaveClass('text-gray-600')
  })

  it('applies custom className', () => {
    render(<LoadingSpinner className="custom-class" />)
    expect(screen.getByRole('status')).toHaveClass('custom-class')
  })

  it('has proper accessibility attributes', () => {
    render(<LoadingSpinner />)
    const spinner = screen.getByRole('status')
    
    expect(spinner).toHaveAttribute('role', 'status')
    expect(spinner).toHaveAttribute('aria-label', 'Loading')
  })

  it('contains SVG with correct structure', () => {
    render(<LoadingSpinner />)
    const svg = screen.getByRole('status').querySelector('svg')
    
    expect(svg).toBeInTheDocument()
    expect(svg).toHaveClass('w-full h-full')
    expect(svg).toHaveAttribute('fill', 'none')
    expect(svg).toHaveAttribute('viewBox', '0 0 24 24')
  })
})