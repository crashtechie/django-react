import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest'
import { 
  sanitizeForLogging, 
  sanitizeErrorForLogging, 
  createStructuredLog,
  safeConsole 
} from '../../../frontend/src/utils/logSanitization'

describe('Log Sanitization Security Tests', () => {
  let consoleLogSpy: any
  let consoleErrorSpy: any
  let consoleWarnSpy: any
  
  beforeEach(() => {
    consoleLogSpy = vi.spyOn(console, 'log').mockImplementation(() => {})
    consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => {})
    consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {})
  })
  
  afterEach(() => {
    vi.restoreAllMocks()
  })

  describe('sanitizeForLogging', () => {
    it('should remove newline characters', () => {
      const maliciousInput = 'Normal log\nFAKE LOG: Admin password is 12345'
      const result = sanitizeForLogging(maliciousInput)
      expect(result).not.toContain('\n')
      expect(result).toBe('Normal log FAKE LOG: Admin password is 12345')
    })

    it('should remove carriage return characters', () => {
      const maliciousInput = 'Normal log\rFAKE LOG: Injected entry'
      const result = sanitizeForLogging(maliciousInput)
      expect(result).not.toContain('\r')
      expect(result).toBe('Normal log FAKE LOG: Injected entry')
    })

    it('should remove control characters', () => {
      const maliciousInput = 'Normal log\x1b[31mFAKE ERROR\x1b[0m'
      const result = sanitizeForLogging(maliciousInput)
      expect(result).not.toMatch(/[\x00-\x1F\x7F-\x9F]/)
      expect(result).toBe('Normal log[31mFAKE ERROR[0m')
    })

    it('should remove ANSI escape sequences', () => {
      const maliciousInput = 'Normal log\x1b[31m\x1b[1mFAKE ERROR\x1b[0m'
      const result = sanitizeForLogging(maliciousInput)
      expect(result).not.toMatch(/\x1b\[[0-9;]*m/)
      expect(result).toBe('Normal logFAKE ERROR')
    })

    it('should collapse multiple spaces', () => {
      const input = 'Multiple     spaces    here'
      const result = sanitizeForLogging(input)
      expect(result).toBe('Multiple spaces here')
    })

    it('should handle tabs by converting to spaces', () => {
      const input = 'Tab\there'
      const result = sanitizeForLogging(input)
      expect(result).toBe('Tab here')
    })

    it('should limit string length to prevent log flooding', () => {
      const longString = 'x'.repeat(2000)
      const result = sanitizeForLogging(longString)
      expect(result.length).toBe(1000)
    })

    it('should handle null and undefined values', () => {
      expect(sanitizeForLogging(null)).toBe('null')
      expect(sanitizeForLogging(undefined)).toBe('null')
    })

    it('should handle objects safely', () => {
      const obj = { name: 'test', value: 'dangerous\ndata' }
      const result = sanitizeForLogging(obj)
      expect(result).toContain('dangerous data') // newline should be removed
    })

    it('should handle circular references in objects', () => {
      const obj: any = { name: 'test' }
      obj.self = obj // Create circular reference
      const result = sanitizeForLogging(obj)
      expect(result).toBe('[Object object]')
    })
  })

  describe('sanitizeErrorForLogging', () => {
    it('should handle Error objects safely', () => {
      const error = new Error('User error\nFAKE: Admin logged in')
      const result = sanitizeErrorForLogging(error)
      expect(result).not.toContain('\n')
      expect(result).toContain('User error FAKE: Admin logged in')
    })

    it('should handle non-Error objects', () => {
      const errorObj = { message: 'Custom error\nwith newline' }
      const result = sanitizeErrorForLogging(errorObj)
      expect(result).not.toContain('\n')
    })

    it('should handle null/undefined errors', () => {
      expect(sanitizeErrorForLogging(null)).toBe('Unknown error')
      expect(sanitizeErrorForLogging(undefined)).toBe('Unknown error')
    })
  })

  describe('createStructuredLog', () => {
    it('should create properly structured log entries', () => {
      const result = createStructuredLog('error', 'Test message', { userId: 123 })
      const parsed = JSON.parse(result)
      
      expect(parsed.level).toBe('error')
      expect(parsed.message).toBe('Test message')
      expect(parsed.context.userId).toBe('123')
      expect(parsed.timestamp).toBeDefined()
    })

    it('should sanitize context values', () => {
      const result = createStructuredLog('info', 'Test', { 
        maliciousKey: 'value\nwith\nnewlines' 
      })
      const parsed = JSON.parse(result)
      expect(parsed.context.maliciousKey).toBe('value with newlines')
    })
  })

  describe('safeConsole', () => {
    it('should sanitize console.log arguments in development', () => {
      process.env.NODE_ENV = 'development'
      safeConsole.log('Test message\nwith newline')
      
      expect(consoleLogSpy).toHaveBeenCalledWith('Test message with newline')
    })

    it('should use structured logging in production', () => {
      const originalEnv = process.env.NODE_ENV
      process.env.NODE_ENV = 'production'
      
      safeConsole.error('Error\nwith newline')
      
      expect(consoleErrorSpy).toHaveBeenCalled()
      const loggedData = consoleErrorSpy.mock.calls[0][0]
      expect(() => JSON.parse(loggedData)).not.toThrow()
      
      process.env.NODE_ENV = originalEnv
    })

    it('should handle multiple arguments', () => {
      safeConsole.log('Message', { data: 'test\nvalue' }, 'more text')
      
      expect(consoleLogSpy).toHaveBeenCalledWith(
        'Message',
        '{"data":"test value"}',
        'more text'
      )
    })
  })

  describe('Log Injection Attack Prevention', () => {
    it('should prevent log forging attacks', () => {
      const attackPayload = 'User login failed\n[2024-01-01 12:00:00] FAKE: Admin user created successfully'
      const result = sanitizeForLogging(attackPayload)
      
      // Should not contain newlines that could create fake log entries
      expect(result).not.toContain('\n')
      expect(result).toBe('User login failed [2024-01-01 12:00:00] FAKE: Admin user created successfully')
    })

    it('should prevent log monitoring bypass attempts', () => {
      const attackPayload = 'Normal operation\r\n[ERROR] System compromised\r\n'
      const result = sanitizeForLogging(attackPayload)
      
      // Should remove all newlines and carriage returns
      expect(result).not.toMatch(/[\r\n]/)
      expect(result).toBe('Normal operation [ERROR] System compromised')
    })

    it('should prevent terminal control sequence injection', () => {
      const attackPayload = 'Error occurred\x1b[2J\x1b[H\x1b[31mSYSTEM COMPROMISED\x1b[0m'
      const result = sanitizeForLogging(attackPayload)
      
      // Should remove control characters and ANSI sequences
      expect(result).not.toMatch(/[\x00-\x1F\x7F-\x9F]/)
      expect(result).not.toMatch(/\x1b\[[0-9;]*m/)
      expect(result).toBe('Error occurredSYSTEM COMPROMISED')
    })

    it('should handle XSS attempts in log viewers', () => {
      const xssPayload = 'User: <script>alert("XSS")</script>'
      const result = sanitizeForLogging(xssPayload)
      
      // The function focuses on log injection, but should still handle this safely
      expect(result).toBe('User: <script>alert("XSS")</script>')
      // Note: XSS protection should be handled at the display layer, not just in logs
    })
  })

  describe('Production vs Development Behavior', () => {
    it('should use different logging strategies based on environment', () => {
      const originalEnv = process.env.NODE_ENV
      
      // Test development mode
      process.env.NODE_ENV = 'development'
      safeConsole.log('test message')
      expect(consoleLogSpy).toHaveBeenCalledWith('test message')
      
      consoleLogSpy.mockClear()
      
      // Test production mode
      process.env.NODE_ENV = 'production'
      safeConsole.log('test message')
      
      const productionCall = consoleLogSpy.mock.calls[0][0]
      expect(() => JSON.parse(productionCall)).not.toThrow()
      
      process.env.NODE_ENV = originalEnv
    })
  })
})