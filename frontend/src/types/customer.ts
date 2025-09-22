export interface Customer {
  id: number
  first_name: string
  last_name: string
  full_name: string
  email: string
  phone: string
  is_active: boolean
  created_at: string
  updated_at: string
}

export interface CustomerFormData {
  first_name: string
  last_name: string
  email: string
  phone: string
}

export interface CustomerStats {
  total_customers: number
  active_customers: number
  inactive_customers: number
}

export interface PaginatedResponse<T> {
  count: number
  next: string | null
  previous: string | null
  results: T[]
}

export interface ApiError {
  message: string
  field_errors?: Record<string, string[]>
}