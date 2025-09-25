// Test helpers for Jest
export const getMocks = () => (global as any).__TEST_MOCKS__;

export const resetAllMocks = () => {
  const mocks = getMocks();
  
  // Reset router mocks
  mocks.navigate.mockClear();
  mocks.useParams.mockReturnValue({ id: undefined });
  
  // Reset API mocks
  Object.values(mocks.customerApi).forEach((mockFn: any) => {
    if (typeof mockFn.mockClear === 'function') {
      mockFn.mockClear();
    }
  });
  
  // Reset toast mocks
  Object.values(mocks.toast).forEach((mockFn: any) => {
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