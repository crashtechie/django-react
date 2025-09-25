import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import CustomerForm from '../pages/CustomerForm'
import { resetAllMocks } from '../test/helpers'

describe('CustomerForm - Jest Tests', () => {
  beforeEach(() => {
    resetAllMocks()
  })

  it('renders the form correctly', () => {
    render(
      <MemoryRouter>
        <CustomerForm />
      </MemoryRouter>
    )
    
    expect(screen.getByText('Add New Customer')).toBeInTheDocument()
  })
})