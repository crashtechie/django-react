import { Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import { ErrorBoundary } from './components/ui'
import CustomerList from './pages/CustomerList'
import CustomerDetail from './pages/CustomerDetail'
import CustomerForm from './pages/CustomerForm'
import Dashboard from './pages/Dashboard'
import NotFound from './pages/NotFound'
import { safeConsole } from './utils/logSanitization'

function App() {
  const handleError = (error: Error, errorInfo: React.ErrorInfo) => {
    // Log to console in development with safe sanitization
    safeConsole.error('Application Error:', error, errorInfo)
    
    // In production, you would send this to your monitoring service
    // Example: Sentry, LogRocket, etc.
  }

  return (
    <ErrorBoundary onError={handleError}>
      <Layout>
        <ErrorBoundary>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route 
              path="/customers" 
              element={
                <ErrorBoundary>
                  <CustomerList />
                </ErrorBoundary>
              } 
            />
            <Route 
              path="/customers/new" 
              element={
                <ErrorBoundary>
                  <CustomerForm />
                </ErrorBoundary>
              } 
            />
            <Route 
              path="/customers/:id" 
              element={
                <ErrorBoundary>
                  <CustomerDetail />
                </ErrorBoundary>
              } 
            />
            <Route 
              path="/customers/:id/edit" 
              element={
                <ErrorBoundary>
                  <CustomerForm />
                </ErrorBoundary>
              } 
            />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </ErrorBoundary>
      </Layout>
    </ErrorBoundary>
  )
}

export default App