/**
 * Log Sanitization Utilities
 * Provides functions to sanitize data before logging to prevent log injection attacks
 */

/**
 * Sanitizes a string for safe logging by removing/escaping dangerous characters
 * Removes newlines, control characters, and other potentially dangerous sequences
 */
export const sanitizeForLogging = (input: unknown): string => {
  if (input === null || input === undefined) {
    return 'null'
  }
  
  let str: string
  
  // Handle different input types safely
  if (typeof input === 'string') {
    str = input
  } else if (typeof input === 'object') {
    // For objects, use JSON.stringify but catch circular references
    try {
      str = JSON.stringify(input)
    } catch (error) {
      str = '[Object object]'
    }
  } else {
    str = String(input)
  }
  
  // Remove/escape dangerous characters:
  // - Control characters (0x00-0x1F, 0x7F-0x9F)
  // - Newlines and carriage returns
  // - ANSI escape sequences
  // - Other potentially dangerous sequences
  return str
    .replace(/[\x00-\x1F\x7F-\x9F]/g, '') // Remove control characters
    .replace(/\r?\n/g, ' ') // Replace newlines with spaces
    .replace(/\r/g, ' ') // Replace carriage returns with spaces
    .replace(/\x1b\[[0-9;]*m/g, '') // Remove ANSI escape sequences
    .replace(/\t/g, ' ') // Replace tabs with spaces
    .replace(/\s+/g, ' ') // Collapse multiple spaces
    .trim() // Remove leading/trailing whitespace
    .substring(0, 1000) // Limit length to prevent log flooding
}

/**
 * Sanitizes error objects for safe logging
 */
export const sanitizeErrorForLogging = (error: unknown): string => {
  if (!error) {
    return 'Unknown error'
  }
  
  if (error instanceof Error) {
    // Extract only safe properties from Error objects
    const safeError = {
      name: error.name,
      message: sanitizeForLogging(error.message),
      // Don't include stack trace as it may contain sensitive paths
      // stack: error.stack ? sanitizeForLogging(error.stack) : undefined
    }
    return sanitizeForLogging(safeError)
  }
  
  return sanitizeForLogging(error)
}

/**
 * Creates a structured log entry with safe field separation
 */
export const createStructuredLog = (level: string, message: string, context?: Record<string, unknown>): string => {
  const timestamp = new Date().toISOString()
  const sanitizedMessage = sanitizeForLogging(message)
  
  const logEntry = {
    timestamp,
    level: sanitizeForLogging(level),
    message: sanitizedMessage,
    ...(context && { context: Object.fromEntries(
      Object.entries(context).map(([key, value]) => [
        sanitizeForLogging(key),
        sanitizeForLogging(value)
      ])
    )})
  }
  
  return JSON.stringify(logEntry)
}

/**
 * Safe console logging functions that automatically sanitize input
 */
export const safeConsole = {
  log: (...args: unknown[]) => {
    if (process.env.NODE_ENV === 'production') {
      // In production, use structured logging
      console.log(createStructuredLog('info', args.map(sanitizeForLogging).join(' ')))
    } else {
      // In development, sanitize individual arguments
      console.log(...args.map(sanitizeForLogging))
    }
  },
  
  error: (...args: unknown[]) => {
    if (process.env.NODE_ENV === 'production') {
      console.error(createStructuredLog('error', args.map(sanitizeErrorForLogging).join(' ')))
    } else {
      console.error(...args.map(sanitizeErrorForLogging))
    }
  },
  
  warn: (...args: unknown[]) => {
    if (process.env.NODE_ENV === 'production') {
      console.warn(createStructuredLog('warn', args.map(sanitizeForLogging).join(' ')))
    } else {
      console.warn(...args.map(sanitizeForLogging))
    }
  },
  
  info: (...args: unknown[]) => {
    if (process.env.NODE_ENV === 'production') {
      console.info(createStructuredLog('info', args.map(sanitizeForLogging).join(' ')))
    } else {
      console.info(...args.map(sanitizeForLogging))
    }
  }
}