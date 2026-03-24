# Required Field Validation

**Test Case ID**: TC-LOGIN-004  
**Priority**: High  
**Category**: Negative

## Overview
Validates that the system enforces required field validation for username and password fields, displaying appropriate error messages when fields are left empty during login attempts.

## Preconditions
- User is on the HR Orange login page
- Browser is open and page is fully loaded
- No fields are pre-filled

---

## Test Scenarios

### Scenario 1: Empty Username Field

**Test Data**:
- Username: (empty - leave blank)
- Password: admin123

**Test Steps**:
1. Navigate to the login page
2. Leave the username field empty
3. Enter "admin123" in the password field
4. Click the Login button

**Expected Results**:
- Login attempt is rejected
- Page does NOT refresh
- "Required" error message appears in red text below the username field
- Password field retains the entered value "admin123"
- User remains on the login page
- No error banner appears

---

### Scenario 2: Empty Password Field

**Test Data**:
- Username: Admin
- Password: (empty - leave blank)

**Test Steps**:
1. Navigate to the login page
2. Enter "Admin" in the username field
3. Leave the password field empty
4. Click the Login button

**Expected Results**:
- Login attempt is rejected
- Page does NOT refresh
- "Required" error message appears in red text below the password field
- Username field retains the entered value "Admin"
- User remains on the login page
- No error banner appears

---

### Scenario 3: Both Username and Password Fields Empty

**Test Data**:
- Username: (empty - leave blank)
- Password: (empty - leave blank)

**Test Steps**:
1. Navigate to the login page
2. Leave both username and password fields empty
3. Click the Login button

**Expected Results**:
- Login attempt is rejected
- Page does NOT refresh
- "Required" error message appears in red text below the username field
- "Required" error message appears in red text below the password field
- Both fields remain empty
- User remains on the login page
- No error banner appears

---

## Notes
- Required field validation occurs client-side before form submission
- Unlike invalid credentials errors, required field validation does not refresh the page
- Non-empty fields retain their values when validation fails
- "Required" errors are field-specific and displayed directly below the corresponding input field
- No error banner is shown for required field validation (only for invalid credentials)
- Related test cases: TC-LOGIN-001 (Successful Login), TC-LOGIN-003 (Invalid Credentials)
