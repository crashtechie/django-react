import { useState, useEffect } from 'react'
import { LoadingSpinner } from '../components/ui'

const CustomerDetail = () => {
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    // Simulate API call
    const timer = setTimeout(() => setIsLoading(false), 1000)
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
      <div className="bg-white shadow rounded-lg">
        <div className="px-6 py-4">
          <h1 className="text-xl font-semibold text-gray-900">Customer Details</h1>
          <p className="text-gray-500 mt-2">Customer details will be implemented here...</p>
        </div>
      </div>
    </div>
  )
}

export default CustomerDetail