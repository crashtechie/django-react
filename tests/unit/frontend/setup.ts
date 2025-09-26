import '@testing-library/jest-dom';

// Extend Jest matchers with jest-dom
declare global {
  namespace jest {
    interface Matchers<R> {
      toBeInTheDocument(): R;
      toHaveTextContent(text: string | RegExp): R;
      toHaveAttribute(attr: string, value?: string): R;
      toHaveClass(...classNames: string[]): R;
      toHaveFocus(): R;
      toHaveValue(value: string | number): R;
      toBeDisabled(): R;
      toBeEnabled(): R;
      toBeVisible(): R;
      toBeEmptyDOMElement(): R;
      toBeInvalid(): R;
      toBeRequired(): R;
      toBeValid(): R;
      toContainElement(element: HTMLElement | null): R;
      toContainHTML(htmlText: string): R;
      toHaveAccessibleDescription(expectedAccessibleDescription?: string | RegExp): R;
      toHaveAccessibleName(expectedAccessibleName?: string | RegExp): R;
      toHaveDisplayValue(value: string | RegExp | (string | RegExp)[]): R;
      toHaveFormValues(expectedValues: Record<string, any>): R;
      toHaveStyle(css: string | Record<string, any>): R;
      toBeChecked(): R;
      toBePartiallyChecked(): R;
      toHaveErrorMessage(expectedErrorMessage?: string | RegExp): R;
    }
  }
}

// Create persistent mock functions that can be accessed across tests
const mockNavigate = jest.fn();
const mockUseParams = jest.fn(() => ({ id: undefined }));

// Mock react-router-dom with persistent mocks
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: () => mockNavigate,
  useParams: mockUseParams,
}));

// Create persistent API mocks
const mockCustomerApi = {
  getCustomer: jest.fn().mockResolvedValue({
    id: 1,
    first_name: 'John',
    last_name: 'Doe',
    email: 'john.doe@example.com',
    phone: '(555) 123-4567',
    is_active: true,
    created_at: '2024-01-01T00:00:00Z',
    updated_at: '2024-01-01T00:00:00Z',
    full_name: 'John Doe'
  }),
  createCustomer: jest.fn().mockResolvedValue({ id: 1 }),
  updateCustomer: jest.fn().mockResolvedValue({ id: 1 }),
  getCustomers: jest.fn().mockResolvedValue({ results: [], count: 0 }),
  deleteCustomer: jest.fn().mockResolvedValue(undefined),
  getCustomerStats: jest.fn().mockResolvedValue({ total: 0, active: 0 }),
  activateCustomer: jest.fn().mockResolvedValue({ id: 1 }),
  deactivateCustomer: jest.fn().mockResolvedValue({ id: 1 })
};

// Mock API services
jest.mock('@/services/api', () => ({
  customerApi: mockCustomerApi,
  default: {
    get: jest.fn(),
    post: jest.fn(),
    put: jest.fn(),
    delete: jest.fn()
  }
}));

// Mock react-hot-toast
const mockToast = {
  success: jest.fn(),
  error: jest.fn(),
  loading: jest.fn(),
  dismiss: jest.fn()
};

jest.mock('react-hot-toast', () => mockToast);

// Export mocks for test access
(global as unknown as { __TEST_MOCKS__: unknown }).__TEST_MOCKS__ = {
  navigate: mockNavigate,
  useParams: mockUseParams,
  customerApi: mockCustomerApi,
  toast: mockToast
};