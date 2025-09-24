import axios, { AxiosResponse, AxiosError, InternalAxiosRequestConfig } from 'axios'
import { Customer, CustomerFormData, CustomerStats, PaginatedResponse } from '../types'

const API_BASE_URL = import.meta.env.VITE_API_URL || '/api'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
})

// Request interceptor
api.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    // Only log in development
    if (import.meta.env.DEV) {
      console.log(`API Request: ${config.method?.toUpperCase()} ${config.url}`)
    }
    return config
  },
  (error: AxiosError) => {
    return Promise.reject(error)
  }
)

// Response interceptor for error handling
api.interceptors.response.use(
  (response: AxiosResponse) => {
    return response
  },
  (error: AxiosError) => {
    console.error('API Error:', error.response?.data || error.message)
    return Promise.reject(error)
  }
)

export const customerApi = {
  // Get all customers with optional filtering
  getCustomers: async (params?: {
    page?: number
    search?: string
    is_active?: boolean
    ordering?: string
  }): Promise<PaginatedResponse<Customer>> => {
    const response = await api.get('/customers/', { params })
    return response.data
  },

  // Get a single customer by ID
  getCustomer: async (id: number): Promise<Customer> => {
    const response = await api.get(`/customers/${id}/`)
    return response.data
  },

  // Create a new customer
  createCustomer: async (data: CustomerFormData): Promise<Customer> => {
    const response = await api.post('/customers/', data)
    return response.data
  },

  // Update an existing customer
  updateCustomer: async (id: number, data: CustomerFormData): Promise<Customer> => {
    const response = await api.put(`/customers/${id}/`, data)
    return response.data
  },

  // Delete a customer
  deleteCustomer: async (id: number): Promise<void> => {
    await api.delete(`/customers/${id}/`)
  },

  // Get customer statistics
  getCustomerStats: async (): Promise<CustomerStats> => {
    const response = await api.get('/customers/stats/')
    return response.data
  },

  // Activate a customer
  activateCustomer: async (id: number): Promise<Customer> => {
    const response = await api.post(`/customers/${id}/activate/`)
    return response.data.customer
  },

  // Deactivate a customer
  deactivateCustomer: async (id: number): Promise<Customer> => {
    const response = await api.post(`/customers/${id}/deactivate/`)
    return response.data.customer
  },
}

export default api