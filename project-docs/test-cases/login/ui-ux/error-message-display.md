# Error Message Display Validation

**Test Case ID**: TC-LOGIN-010  
**Priority**: High  
**Category**: UI/UX

## Overview
Validates that error messages are displayed correctly on the login page, including visibility, positioning, styling, and text content for both "Invalid credentials" banner and "Required" field errors.

## Preconditions
- Navigate to the login page
- Login page is fully loaded
- No user is currently logged in

---

## Test Scenarios

### Scenario 1: Error Banner Visibility - Initially Hidden

**Test Data**:
- N/A

**Test Steps**:
1. Navigate to the login page
2. Observe the page before any interaction
3. Check for the presence of the error banner (Invalid credentials message)

**Expected Results**:
- Error banner is not visible on initial page load
- No error messages are displayed above the username field
- Page displays clean login form without errors

---

### Scenario 2: Error Banner Appears After Invalid Login

**Test Data**:
- Username: invalid_user
- Password: invalid_pass

**Test Steps**:
1. Navigate to the login page
2. Enter invalid username
3. Enter invalid password
4. Click the Login button
5. Wait for page response
6. Verify error banner visibility

**Expected Results**:
- Page refreshes after login attempt
- Error banner becomes visible above the username field
- Error banner displays "Invalid credentials" message
- Error banner styling is consistent (red/alert style)

---

### Scenario 3: Required Error for Empty Username Field

**Test Data**:
- Username: (empty)
- Password: ValidPassword123

**Test Steps**:
1. Navigate to the login page
2. Leave username field empty
3. Enter valid password
4. Click the Login button
5. Verify error message appears below username field

**Expected Results**:
- "Required" error text appears below username field
- Error text is displayed in red color
- Error appears without page refresh
- Password field retains entered value

---

### Scenario 4: Required Error for Empty Password Field

**Test Data**:
- Username: ValidUsername
- Password: (empty)

**Test Steps**:
1. Navigate to the login page
2. Enter valid username
3. Leave password field empty
4. Click the Login button
5. Verify error message appears below password field

**Expected Results**:
- "Required" error text appears below password field
- Error text is displayed in red color
- Error appears without page refresh
- Username field retains entered value

---

### Scenario 5: Required Errors for Both Empty Fields

**Test Data**:
- Username: (empty)
- Password: (empty)

**Test Steps**:
1. Navigate to the login page
2. Leave both fields empty
3. Click the Login button
4. Verify error messages appear below both fields

**Expected Results**:
- "Required" error text appears below username field
- "Required" error text appears below password field
- Both error texts are displayed in red color
- Errors appear without page refresh
- Both fields remain empty

---

### Scenario 6: Error Text Positioning and Styling

**Test Data**:
- Username: (empty)
- Password: (empty)

**Test Steps**:
1. Navigate to the login page
2. Leave both fields empty
3. Click the Login button
4. Inspect the positioning and styling of error messages

**Expected Results**:
- "Required" error text is positioned directly below the respective input field
- Error text color is red
- Error text font size is smaller than regular text
- Error messages are left-aligned with the input fields
- Error banner (when visible) is positioned above the username field

---

## Notes
- Error banner appears only after invalid credentials submission (with page refresh)
- "Required" errors appear for empty fields without page refresh
- Error banner and "Required" errors are different types of validation feedback
- Automation should verify both the visibility state and the exact error text content
- CSS selectors for error elements should be stable and unique
