// Test helpers for Jest
interface TestMocks {
  navigate: jest.Mock;
  useParams: jest.Mock;
  customerApi: Record<string, jest.Mock>;
  toast: Record<string, jest.Mock>;
}

export const getMocks = (): TestMocks => (global as unknown as { __TEST_MOCKS__: TestMocks }).__TEST_MOCKS__;

export const resetAllMocks = () => {
  const mocks = getMocks();
  
  // Reset router mocks
  mocks.navigate.mockClear();
  mocks.useParams.mockReturnValue({ id: undefined });
  
  // Reset API mocks
  Object.values(mocks.customerApi).forEach((mockFn: jest.Mock) => {
    if (typeof mockFn.mockClear === 'function') {
      mockFn.mockClear();
    }
  });
  
  // Reset toast mocks
  Object.values(mocks.toast).forEach((mockFn: jest.Mock) => {
    if (typeof mockFn.mockClear === 'function') {
      mockFn.mockClear();
    }
  });
};

export const setEditMode = (id: string) => {
  const mocks = getMocks();
  mocks.useParams.mockReturnValue({ id });
};

export const setCreateMode = () => {
  const mocks = getMocks();
  mocks.useParams.mockReturnValue({ id: undefined });
};