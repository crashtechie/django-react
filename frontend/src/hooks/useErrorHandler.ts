import { useCallback } from 'react'
import { safeConsole, sanitizeForLogging } from '../utils/logSanitization'

interface ErrorHandlerOptions {
  logToConsole?: boolean
  showToast?: boolean
}

export const useErrorHandler = (options: ErrorHandlerOptions = {}) => {
  const { logToConsole = true, showToast = false } = options

  const handleError = useCallback((error: Error, context?: string) => {
    if (logToConsole) {
      safeConsole.error(`Error${context ? ` in ${sanitizeForLogging(context)}` : ''}:`, error)
    }

    if (showToast) {
      // In a real app, you'd use your toast library here
      // For now, we'll just log it with sanitization
      safeConsole.warn('Toast notification:', sanitizeForLogging(error.message))
    }

    // In production, send to monitoring service
    if (process.env.NODE_ENV === 'production') {
      // Example: Sentry.captureException(error)
    }
  }, [logToConsole, showToast])

  return { handleError }
}

export default useErrorHandler