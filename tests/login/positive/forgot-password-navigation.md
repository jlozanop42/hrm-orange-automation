# Forgot Password Link Navigation

**Test Case ID**: TC-LOGIN-002  
**Priority**: Medium  
**Category**: Positive

## Overview
Validates that the "Forgot your password?" link on the login page correctly navigates the user to the password reset request page.

## Preconditions
- User is on the login page
- "Forgot your password?" link is visible and accessible
- Password reset functionality is enabled on the system

---

## Test Scenarios

### Scenario 1: Navigate to Password Reset Page

**Test Data**:
- N/A (No input required)

**Test Steps**:
1. Navigate to the OrangeHRM login page
2. Locate the "Forgot your password?" link
3. Click on the "Forgot your password?" link

**Expected Results**:
- User is redirected to the password reset request page
- URL matches the pattern: `.*/auth/requestPasswordResetCode`
- Expected full URL: `https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode`
- Password reset page displays correctly with appropriate form fields
- No error messages are displayed
- Back navigation to login page should be available

---

## Notes
- This validates navigation flow, not the password reset functionality itself
- Password reset form validation will be covered in separate test cases
- Related test cases: TC-LOGIN-001 (Successful Login)
- User should be able to return to login page from password reset page
