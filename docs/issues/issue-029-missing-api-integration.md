# Issue #29: Missing API Integration in Customer Pages

## Feature Description
CustomerList and CustomerDetail pages need proper API integration to fetch real customer data

## User Story
As a user, I want to see actual customer data so that I can manage real customers instead of placeholder content

## Acceptance Criteria
- [ ] Connect CustomerList to GET /api/customers/ endpoint
- [ ] Connect CustomerDetail to GET /api/customers/{id}/ endpoint
- [ ] Implement proper error handling for API failures
- [ ] Add loading states during API calls
- [ ] Handle empty states (no customers)
- [ ] Implement pagination for customer list

## Technical Requirements
- Use existing customerApi service from services/api.ts
- Implement React Query or similar for data fetching
- Add error boundaries for API failures
- TypeScript interfaces for API responses
- Proper loading and error states

## Priority
- [x] High (Must have)
- [ ] Medium (Should have)
- [ ] Low (Nice to have)

## Estimated Story Points
13