interface ErrorFallbackProps {
  error?: Error
  resetError?: () => void
  title?: string
  message?: string
}

const ErrorFallback = ({ 
  error, 
  resetError, 
  title = "Something went wrong",
  message = "We encountered an unexpected error. Please try again."
}: ErrorFallbackProps) => {
  return (
    <div className="min-h-64 flex items-center justify-center p-6" role="alert">
      <div className="text-center max-w-md">
        <div className="mx-auto flex items-center justify-center h-12 w-12 rounded-full bg-red-100">
          <svg 
            className="h-6 w-6 text-red-600" 
            fill="none" 
            viewBox="0 0 24 24" 
            stroke="currentColor"
            aria-hidden="true"
          >
            <path 
              strokeLinecap="round" 
              strokeLinejoin="round" 
              strokeWidth={2} 
              d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16c-.77.833.192 2.5 1.732 2.5z" 
            />
          </svg>
        </div>
        
        <h3 className="mt-2 text-sm font-medium text-gray-900">
          {title}
        </h3>
        
        <p className="mt-1 text-sm text-gray-500">
          {message}
        </p>
        
        {error && process.env.NODE_ENV === 'development' && (
          <details className="mt-4 text-left">
            <summary className="text-xs text-gray-400 cursor-pointer hover:text-gray-600">
              Error Details (Development)
            </summary>
            <pre className="mt-2 text-xs text-red-600 bg-red-50 p-2 rounded overflow-auto">
              {error.message}
              {error.stack && `\n\n${error.stack}`}
            </pre>
          </details>
        )}
        
        {resetError && (
          <div className="mt-6">
            <button
              type="button"
              onClick={resetError}
              className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            >
              Try again
            </button>
          </div>
        )}
      </div>
    </div>
  )
}

export default ErrorFallback