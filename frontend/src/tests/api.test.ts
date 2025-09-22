import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { customerApi } from '../services/api'
import axios from 'axios'
import { Customer, CustomerFormData } from '../types'

// Mock axios
vi.mock('axios', () => ({
  default: {
    create: vi.fn(() => ({
      get: vi.fn(),
      post: vi.fn(),
      put: vi.fn(),
      delete: vi.fn(),
      interceptors: {
        request: { use: vi.fn() },
        response: { use: vi.fn() }
      }
    }))
  }
}))

const mockAxiosInstance = {
  get: vi.fn(),
  post: vi.fn(),
  put: vi.fn(),
  delete: vi.fn(),
  interceptors: {
    request: { use: vi.fn() },
    response: { use: vi.fn() }
  }
}

// Mock the axios.create method
vi.mocked(axios.create).mockReturnValue(mockAxiosInstance as any)

describe('customerApi', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  afterEach(() => {
    vi.resetAllMocks()
  })

  const mockCustomer: Customer = {
    id: 1,
    first_name: 'John',
    last_name: 'Doe',
    email: 'john.doe@example.com',
    phone: '555-1234',
    is_active: true,
    created_at: '2024-01-01T00:00:00Z',
    updated_at: '2024-01-01T00:00:00Z',
    full_name: 'John Doe'
  }

  const mockCustomerFormData: CustomerFormData = {
    first_name: 'John',
    last_name: 'Doe',
    email: 'john.doe@example.com',
    phone: '555-1234'
  }

  describe('getCustomers', () => {
    it('fetches customers successfully', async () => {
      const mockResponse = {
        data: {
          results: [mockCustomer],
          count: 1,
          next: null,
          previous: null
        }
      }
      mockAxiosInstance.get.mockResolvedValueOnce(mockResponse)

      const result = await customerApi.getCustomers()

      expect(mockAxiosInstance.get).toHaveBeenCalledWith('/customers/', { params: {} })
      expect(result).toEqual(mockResponse.data)
    })

    it('passes search parameters correctly', async () => {
      const mockResponse = { data: { results: [] } }
      mockAxiosInstance.get.mockResolvedValueOnce(mockResponse)

      await customerApi.getCustomers({ page: 2, search: 'John', is_active: true })

      expect(mockAxiosInstance.get).toHaveBeenCalledWith('/customers/', {
        params: { page: 2, search: 'John', is_active: true }
      })
    })

    it('handles API errors', async () => {
      const mockError = new Error('Network Error')
      mockAxiosInstance.get.mockRejectedValueOnce(mockError)

      await expect(customerApi.getCustomers()).rejects.toThrow('Network Error')
    })
  })

  describe('getCustomer', () => {
    it('fetches a single customer successfully', async () => {
      const mockResponse = { data: mockCustomer }
      mockAxiosInstance.get.mockResolvedValueOnce(mockResponse)

      const result = await customerApi.getCustomer(1)

      expect(mockAxiosInstance.get).toHaveBeenCalledWith('/customers/1/')
      expect(result).toEqual(mockCustomer)
    })

    it('handles customer not found', async () => {
      const mockError = { response: { status: 404 } }
      mockAxiosInstance.get.mockRejectedValueOnce(mockError)

      await expect(customerApi.getCustomer(999)).rejects.toEqual(mockError)
    })
  })

  describe('createCustomer', () => {
    it('creates a customer successfully', async () => {
      const mockResponse = { data: mockCustomer }
      mockAxiosInstance.post.mockResolvedValueOnce(mockResponse)

      const result = await customerApi.createCustomer(mockCustomerFormData)

      expect(mockAxiosInstance.post).toHaveBeenCalledWith('/customers/', mockCustomerFormData)
      expect(result).toEqual(mockCustomer)
    })

    it('handles validation errors', async () => {
      const mockError = {
        response: {
          status: 400,
          data: { email: ['This field must be unique.'] }
        }
      }
      mockAxiosInstance.post.mockRejectedValueOnce(mockError)

      await expect(customerApi.createCustomer(mockCustomerFormData)).rejects.toEqual(mockError)
    })
  })

  describe('updateCustomer', () => {
    it('updates a customer successfully', async () => {
      const updatedCustomer = { ...mockCustomer, first_name: 'Johnny' }
      const mockResponse = { data: updatedCustomer }
      mockAxiosInstance.put.mockResolvedValueOnce(mockResponse)

      const updateData = { ...mockCustomerFormData, first_name: 'Johnny' }
      const result = await customerApi.updateCustomer(1, updateData)

      expect(mockAxiosInstance.put).toHaveBeenCalledWith('/customers/1/', updateData)
      expect(result).toEqual(updatedCustomer)
    })

    it('handles update errors', async () => {
      const mockError = { response: { status: 400 } }
      mockAxiosInstance.put.mockRejectedValueOnce(mockError)

      await expect(customerApi.updateCustomer(1, mockCustomerFormData)).rejects.toEqual(mockError)
    })
  })

  describe('deleteCustomer', () => {
    it('deletes a customer successfully', async () => {
      mockAxiosInstance.delete.mockResolvedValueOnce({ data: null })

      await customerApi.deleteCustomer(1)

      expect(mockAxiosInstance.delete).toHaveBeenCalledWith('/customers/1/')
    })

    it('handles delete errors', async () => {
      const mockError = { response: { status: 404 } }
      mockAxiosInstance.delete.mockRejectedValueOnce(mockError)

      await expect(customerApi.deleteCustomer(999)).rejects.toEqual(mockError)
    })
  })

  describe('getCustomerStats', () => {
    it('fetches customer statistics successfully', async () => {
      const mockStats = {
        total_customers: 100,
        active_customers: 85,
        inactive_customers: 15,
        avg_monthly_spend: '125.50'
      }
      const mockResponse = { data: mockStats }
      mockAxiosInstance.get.mockResolvedValueOnce(mockResponse)

      const result = await customerApi.getCustomerStats()

      expect(mockAxiosInstance.get).toHaveBeenCalledWith('/customers/stats/')
      expect(result).toEqual(mockStats)
    })
  })

  describe('activateCustomer', () => {
    it('activates a customer successfully', async () => {
      const mockResponse = { data: { customer: mockCustomer } }
      mockAxiosInstance.post.mockResolvedValueOnce(mockResponse)

      const result = await customerApi.activateCustomer(1)

      expect(mockAxiosInstance.post).toHaveBeenCalledWith('/customers/1/activate/')
      expect(result).toEqual(mockCustomer)
    })
  })

  describe('deactivateCustomer', () => {
    it('deactivates a customer successfully', async () => {
      const mockResponse = { data: { customer: mockCustomer } }
      mockAxiosInstance.post.mockResolvedValueOnce(mockResponse)

      const result = await customerApi.deactivateCustomer(1)

      expect(mockAxiosInstance.post).toHaveBeenCalledWith('/customers/1/deactivate/')
      expect(result).toEqual(mockCustomer)
    })
  })
})