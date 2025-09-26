import { useState, useEffect, useRef } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { CustomerFormData } from '../types'
import { customerApi } from '../services/api'
import { safeConsole } from '../utils/logSanitization'
import toast from 'react-hot-toast'

// Sanitize HTML content to prevent XSS attacks
const sanitizeHtml = (input: string): string => {
  return input
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#x27;')
    .replace(/\//g, '&#x2F;')
}

interface FormErrors {
  first_name?: string
  last_name?: string
  email?: string
  phone?: string
  general?: string
}

const CustomerForm = () => {
  const navigate = useNavigate()
  const { id } = useParams<{ id: string }>()
  const isEditing = Boolean(id)

  const [formData, setFormData] = useState<CustomerFormData>({
    first_name: '',
    last_name: '',
    email: '',
    phone: ''
  })

  const [errors, setErrors] = useState<FormErrors>({})
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [isLoading, setIsLoading] = useState(false)

  // Refs for managing aria-invalid attributes
  const firstNameRef = useRef<HTMLInputElement>(null)
  const lastNameRef = useRef<HTMLInputElement>(null)
  const emailRef = useRef<HTMLInputElement>(null)
  const phoneRef = useRef<HTMLInputElement>(null)

  // Update aria-invalid attributes when errors change
  useEffect(() => {
    if (firstNameRef.current) {
      firstNameRef.current.setAttribute('aria-invalid', errors.first_name ? 'true' : 'false')
    }
    if (lastNameRef.current) {
      lastNameRef.current.setAttribute('aria-invalid', errors.last_name ? 'true' : 'false')
    }
    if (emailRef.current) {
      emailRef.current.setAttribute('aria-invalid', errors.email ? 'true' : 'false')
    }
    if (phoneRef.current) {
      phoneRef.current.setAttribute('aria-invalid', errors.phone ? 'true' : 'false')
    }
  }, [errors])

  // Load customer data for editing
  useEffect(() => {
    if (isEditing && id) {
      setIsLoading(true)
      // Load customer data from API
      customerApi.getCustomer(parseInt(id))
        .then(customer => {
          setFormData({
            first_name: customer.first_name,
            last_name: customer.last_name,
            email: customer.email,
            phone: customer.phone || ''
          })
        })
        .catch(error => {
          safeConsole.error('Failed to load customer:', error)
          toast.error('Failed to load customer data')
          navigate('/customers')
        })
        .finally(() => {
          setIsLoading(false)
        })
    }
  }, [isEditing, id, navigate])

  // Validation functions
  const validateEmail = (email: string): boolean => {
    // Enhanced email validation with additional security checks
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    const dangerousPatterns = /<script|<iframe|<object|<embed|javascript:|data:/i
    
    return emailRegex.test(email) && 
           !dangerousPatterns.test(email) &&
           email.length <= 254 // RFC5321 limit
  }

  const validatePhone = (phone: string): boolean => {
    // Enhanced phone validation
    const phoneRegex = /^[\d\s\-()\\+]+$/
    const dangerousPatterns = /<script|<iframe|<object|<embed|javascript:|data:/i
    
    return phoneRegex.test(phone) && 
           phone.replace(/\D/g, '').length >= 10 && 
           phone.length <= 15 && // Reasonable phone number limit
           !dangerousPatterns.test(phone)
  }

  const validateName = (name: string): boolean => {
    // Name validation with XSS prevention
    const nameRegex = /^[a-zA-Z\s\-'\.]+$/
    const dangerousPatterns = /<script|<iframe|<object|<embed|javascript:|data:|on\w+=/i
    
    return name.trim().length >= 2 && 
           name.length <= 50 && // Reasonable name limit
           nameRegex.test(name) &&
           !dangerousPatterns.test(name)
  }

  const validateForm = (): boolean => {
    const newErrors: FormErrors = {}

    // First name validation
    if (!formData.first_name.trim()) {
      newErrors.first_name = 'First name is required'
    } else if (formData.first_name.trim().length < 2) {
      newErrors.first_name = 'First name must be at least 2 characters'
    } else if (!validateName(formData.first_name)) {
      newErrors.first_name = 'First name contains invalid characters or format'
    }

    // Last name validation
    if (!formData.last_name.trim()) {
      newErrors.last_name = 'Last name is required'
    } else if (formData.last_name.trim().length < 2) {
      newErrors.last_name = 'Last name must be at least 2 characters'
    } else if (!validateName(formData.last_name)) {
      newErrors.last_name = 'Last name contains invalid characters or format'
    }

    // Email validation
    if (!formData.email.trim()) {
      newErrors.email = 'Email is required'
    } else if (!validateEmail(formData.email)) {
      newErrors.email = 'Please enter a valid email address'
    }

    // Phone validation
    if (!formData.phone.trim()) {
      newErrors.phone = 'Phone number is required'
    } else if (!validatePhone(formData.phone)) {
      newErrors.phone = 'Please enter a valid phone number'
    }

    setErrors(newErrors)
    return Object.keys(newErrors).length === 0
  }

  const handleInputChange = (field: keyof CustomerFormData, value: string) => {
    setFormData(prev => ({
      ...prev,
      [field]: value
    }))

    // Clear field error when user starts typing
    if (errors[field]) {
      setErrors(prev => ({
        ...prev,
        [field]: undefined
      }))
    }
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    
    if (!validateForm()) {
      return
    }

    setIsSubmitting(true)
    setErrors(prev => ({ ...prev, general: undefined }))

    try {
      if (isEditing && id) {
        // Update existing customer
        await customerApi.updateCustomer(parseInt(id), formData)
        toast.success('Customer updated successfully')
      } else {
        // Create new customer
        await customerApi.createCustomer(formData)
        toast.success('Customer created successfully')
      }
      
      // Navigate back to customer list on success
      navigate('/customers', { replace: true })
    } catch (error: unknown) {
      safeConsole.error('Failed to save customer:', error)
      const rawErrorMessage = (error as { response?: { data?: { detail?: string } } })?.response?.data?.detail || 
        (isEditing ? 'Failed to update customer' : 'Failed to create customer')
      const errorMessage = sanitizeHtml(rawErrorMessage)
      setErrors({ general: errorMessage })
      toast.error(errorMessage)
    } finally {
      setIsSubmitting(false)
    }
  }

  const handleCancel = () => {
    navigate('/customers')
  }

  if (isLoading) {
    return (
      <div className="space-y-6">
        <div className="bg-white shadow rounded-lg">
          <div className="px-6 py-4">
            <div className="animate-pulse">
              <div className="h-6 bg-gray-200 rounded w-1/4 mb-4"></div>
              <div className="space-y-4">
                <div className="h-4 bg-gray-200 rounded w-3/4"></div>
                <div className="h-4 bg-gray-200 rounded w-1/2"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div className="bg-white shadow rounded-lg">
        <div className="px-6 py-4">
          <h1 className="text-xl font-semibold text-gray-900">
            {isEditing ? 'Edit Customer' : 'Add New Customer'}
          </h1>
          <p className="text-gray-500 mt-2">
            {isEditing ? 'Update customer information' : 'Fill out the form below to add a new customer'}
          </p>
        </div>
        
        <form onSubmit={handleSubmit} className="px-6 pb-6">
          {errors.general && (
            <div 
              className="mb-4 p-4 bg-red-50 border border-red-200 rounded-md"
              role="alert"
              aria-live="polite"
            >
              <p className="text-red-800 text-sm">{errors.general}</p>
            </div>
          )}
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* First Name */}
            <div>
              <label 
                htmlFor="first_name" 
                className="block text-sm font-medium text-gray-700 mb-1"
              >
                First Name *
              </label>
              <input
                ref={firstNameRef}
                type="text"
                id="first_name"
                name="first_name"
                value={formData.first_name}
                onChange={(e) => handleInputChange('first_name', e.target.value)}
                className={`block w-full px-3 py-2 border rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm ${
                  errors.first_name 
                    ? 'border-red-300 focus:ring-red-500 focus:border-red-500' 
                    : 'border-gray-300'
                }`}
                placeholder="Enter first name"
                aria-describedby={errors.first_name ? 'first_name-error' : undefined}
              />
              {errors.first_name && (
                <p 
                  id="first_name-error" 
                  className="mt-1 text-sm text-red-600"
                  role="alert"
                >
                  {errors.first_name}
                </p>
              )}
            </div>

            {/* Last Name */}
            <div>
              <label 
                htmlFor="last_name" 
                className="block text-sm font-medium text-gray-700 mb-1"
              >
                Last Name *
              </label>
              <input
                ref={lastNameRef}
                type="text"
                id="last_name"
                name="last_name"
                value={formData.last_name}
                onChange={(e) => handleInputChange('last_name', e.target.value)}
                className={`block w-full px-3 py-2 border rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm ${
                  errors.last_name 
                    ? 'border-red-300 focus:ring-red-500 focus:border-red-500' 
                    : 'border-gray-300'
                }`}
                placeholder="Enter last name"
                aria-describedby={errors.last_name ? 'last_name-error' : undefined}
              />
              {errors.last_name && (
                <p 
                  id="last_name-error" 
                  className="mt-1 text-sm text-red-600"
                  role="alert"
                >
                  {errors.last_name}
                </p>
              )}
            </div>

            {/* Email */}
            <div>
              <label 
                htmlFor="email" 
                className="block text-sm font-medium text-gray-700 mb-1"
              >
                Email Address *
              </label>
              <input
                ref={emailRef}
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={(e) => handleInputChange('email', e.target.value)}
                className={`block w-full px-3 py-2 border rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm ${
                  errors.email 
                    ? 'border-red-300 focus:ring-red-500 focus:border-red-500' 
                    : 'border-gray-300'
                }`}
                placeholder="Enter email address"
                aria-describedby={errors.email ? 'email-error' : undefined}
              />
              {errors.email && (
                <p 
                  id="email-error" 
                  className="mt-1 text-sm text-red-600"
                  role="alert"
                >
                  {errors.email}
                </p>
              )}
            </div>

            {/* Phone */}
            <div>
              <label 
                htmlFor="phone" 
                className="block text-sm font-medium text-gray-700 mb-1"
              >
                Phone Number *
              </label>
              <input
                ref={phoneRef}
                type="tel"
                id="phone"
                name="phone"
                value={formData.phone}
                onChange={(e) => handleInputChange('phone', e.target.value)}
                className={`block w-full px-3 py-2 border rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm ${
                  errors.phone 
                    ? 'border-red-300 focus:ring-red-500 focus:border-red-500' 
                    : 'border-gray-300'
                }`}
                placeholder="Enter phone number"
                aria-describedby={errors.phone ? 'phone-error' : undefined}
              />
              {errors.phone && (
                <p 
                  id="phone-error" 
                  className="mt-1 text-sm text-red-600"
                  role="alert"
                >
                  {errors.phone}
                </p>
              )}
            </div>
          </div>

          {/* Form Actions */}
          <div className="flex justify-end space-x-3 mt-6">
            <button
              type="button"
              onClick={handleCancel}
              className="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
              disabled={isSubmitting}
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={isSubmitting}
              className="px-4 py-2 text-sm font-medium text-white bg-blue-600 border border-transparent rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isSubmitting 
                ? (isEditing ? 'Updating...' : 'Creating...') 
                : (isEditing ? 'Update Customer' : 'Create Customer')
              }
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default CustomerForm