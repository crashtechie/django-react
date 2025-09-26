import { useCallback } from 'react'

interface ErrorHandlerOptions {
  logToConsole?: boolean
  showToast?: boolean
}

export const useErrorHandler = (options: ErrorHandlerOptions = {}) => {
  const { logToConsole = true, showToast = false } = options

  const handleError = useCallback((error: Error, context?: string) => {
    if (logToConsole) {
      console.error(`Error${context ? ` in ${context}` : ''}:`, error)
    }

    if (showToast) {
      // In a real app, you'd use your toast library here
      // For now, we'll just log it
      console.warn('Toast notification:', error.message)
    }

    // In production, send to monitoring service
    if (process.env.NODE_ENV === 'production') {
      // Example: Sentry.captureException(error)
    }
  }, [logToConsole, showToast])

  return { handleError }
}

export default useErrorHandler