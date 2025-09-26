import { describe, it, expect, beforeEach } from '@jest/globals'
import { getMocks, resetAllMocks, setEditMode, setCreateMode } from '@/test/helpers'

describe('Mock System', () => {
  beforeEach(() => {
    resetAllMocks()
  })

  it('should have all required mocks available', () => {
    const mocks = getMocks()
    
    // Check router mocks
    expect(mocks.navigate).toBeDefined()
    expect(mocks.useParams).toBeDefined()
    
    // Check API mocks
    expect(mocks.customerApi.getCustomer).toBeDefined()
    expect(mocks.customerApi.createCustomer).toBeDefined()
    expect(mocks.customerApi.updateCustomer).toBeDefined()
    expect(mocks.customerApi.getCustomers).toBeDefined()
    expect(mocks.customerApi.deleteCustomer).toBeDefined()
    expect(mocks.customerApi.getCustomerStats).toBeDefined()
    expect(mocks.customerApi.activateCustomer).toBeDefined()
    expect(mocks.customerApi.deactivateCustomer).toBeDefined()
    
    // Check toast mocks
    expect(mocks.toast.success).toBeDefined()
    expect(mocks.toast.error).toBeDefined()
    expect(mocks.toast.loading).toBeDefined()
    expect(mocks.toast.dismiss).toBeDefined()
  })

  it('should reset mocks properly', () => {
    const mocks = getMocks()
    
    // Call some mocks
    mocks.navigate('/test')
    mocks.customerApi.getCustomer(1)
    mocks.toast.success('test')
    
    // Verify they were called
    expect(mocks.navigate).toHaveBeenCalledWith('/test')
    expect(mocks.customerApi.getCustomer).toHaveBeenCalledWith(1)
    expect(mocks.toast.success).toHaveBeenCalledWith('test')
    
    // Reset and verify they're cleared
    resetAllMocks()
    expect(mocks.navigate).not.toHaveBeenCalled()
    expect(mocks.customerApi.getCustomer).not.toHaveBeenCalled()
    expect(mocks.toast.success).not.toHaveBeenCalled()
  })

  it('should handle edit mode setup', () => {
    const mocks = getMocks()
    
    setEditMode('123')
    expect(mocks.useParams()).toEqual({ id: '123' })
    
    setEditMode('1') // default to '1'
    expect(mocks.useParams()).toEqual({ id: '1' })
  })

  it('should handle create mode setup', () => {
    const mocks = getMocks()
    
    setCreateMode()
    expect(mocks.useParams()).toEqual({ id: undefined })
  })

  it('should have consistent default API responses', () => {
    const mocks = getMocks()
    
    // Test default getCustomer response
    expect(mocks.customerApi.getCustomer()).resolves.toEqual({
      id: 1,
      first_name: 'John',
      last_name: 'Doe',
      email: 'john.doe@example.com',
      phone: '(555) 123-4567',
      is_active: true,
      created_at: '2024-01-01T00:00:00Z',
      updated_at: '2024-01-01T00:00:00Z',
      full_name: 'John Doe'
    })
    
    // Test default createCustomer response
    expect(mocks.customerApi.createCustomer({})).resolves.toEqual({ id: 1 })
  })
})