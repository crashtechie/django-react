import { useState, useEffect } from 'react'
import { LoadingSpinner } from '../components/ui'

const CustomerList = () => {
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    // Simulate API call
    const timer = setTimeout(() => setIsLoading(false), 1500)
    return () => clearTimeout(timer)
  }, [])

  if (isLoading) {
    return (
      <div className="flex justify-center items-center min-h-64">
        <LoadingSpinner size="large" />
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div className="sm:flex sm:items-center">
        <div className="sm:flex-auto">
          <h1 className="text-xl font-semibold text-gray-900">Customers</h1>
          <p className="mt-2 text-sm text-gray-700">
            A list of all customers in your account including their name, email, and phone number.
          </p>
        </div>
        <div className="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
          <a
            href="/customers/new"
            className="btn btn-primary"
          >
            Add Customer
          </a>
        </div>
      </div>

      <div className="bg-white shadow rounded-lg">
        <div className="px-6 py-4">
          <p className="text-gray-500">Customer list will be implemented here...</p>
        </div>
      </div>
    </div>
  )
}

export default CustomerList