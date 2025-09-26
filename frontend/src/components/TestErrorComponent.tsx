import { useState } from 'react'

// Test component to demonstrate ErrorBoundary functionality
const TestErrorComponent = () => {
  const [shouldThrow, setShouldThrow] = useState(false)

  if (shouldThrow) {
    throw new Error('This is a test error to demonstrate ErrorBoundary functionality')
  }

  return (
    <div className="p-4 border border-gray-200 rounded-lg">
      <h3 className="text-lg font-medium text-gray-900 mb-2">Error Boundary Test</h3>
      <p className="text-sm text-gray-600 mb-4">
        Click the button below to trigger an error and see the ErrorBoundary in action.
      </p>
      <button
        onClick={() => setShouldThrow(true)}
        className="px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500"
      >
        Trigger Error
      </button>
    </div>
  )
}

export default TestErrorComponent