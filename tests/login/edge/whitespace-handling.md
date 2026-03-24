# Whitespace Handling in Login Fields

**Test Case ID**: TC-LOGIN-005  
**Priority**: High  
**Category**: Edge

## Overview
Validates that the system properly handles leading and trailing whitespace in username and password fields. The system does NOT trim spaces, meaning credentials with extra whitespace will fail authentication even if the core text matches valid credentials.

## Preconditions
- Login page is accessible
- Valid credentials are: Admin / admin123 (exact match required)
- System does not trim leading/trailing spaces

---

## Test Scenarios

### Scenario 1: Leading Space in Username

**Test Data**:
- Username: " Admin" (one leading space)
- Password: admin123

**Test Steps**:
1. Navigate to the login page
2. Enter " Admin" in the username field (with leading space)
3. Enter "admin123" in the password field
4. Click the Login button

**Expected Results**:
- Login fails with "Invalid credentials" error message
- User remains on login page
- Error message is displayed clearly

---

### Scenario 2: Trailing Space in Username

**Test Data**:
- Username: "Admin " (one trailing space)
- Password: admin123

**Test Steps**:
1. Navigate to the login page
2. Enter "Admin " in the username field (with trailing space)
3. Enter "admin123" in the password field
4. Click the Login button

**Expected Results**:
- Login fails with "Invalid credentials" error message
- User remains on login page
- Error message is displayed clearly

---

### Scenario 3: Leading Space in Password

**Test Data**:
- Username: Admin
- Password: " admin123" (one leading space)

**Test Steps**:
1. Navigate to the login page
2. Enter "Admin" in the username field
3. Enter " admin123" in the password field (with leading space)
4. Click the Login button

**Expected Results**:
- Login fails with "Invalid credentials" error message
- User remains on login page
- Error message is displayed clearly

---

### Scenario 4: Trailing Space in Password

**Test Data**:
- Username: Admin
- Password: "admin123 " (one trailing space)

**Test Steps**:
1. Navigate to the login page
2. Enter "Admin" in the username field
3. Enter "admin123 " in the password field (with trailing space)
4. Click the Login button

**Expected Results**:
- Login fails with "Invalid credentials" error message
- User remains on login page
- Error message is displayed clearly

---

### Scenario 5: Multiple Leading/Trailing Spaces

**Test Data**:
- Username: "  Admin  " (two leading, two trailing spaces)
- Password: "  admin123  " (two leading, two trailing spaces)

**Test Steps**:
1. Navigate to the login page
2. Enter "  Admin  " in the username field
3. Enter "  admin123  " in the password field
4. Click the Login button

**Expected Results**:
- Login fails with "Invalid credentials" error message
- User remains on login page
- Error message is displayed clearly

---

## Notes
- This behavior confirms the system does NOT implement automatic space trimming
- Users must enter credentials exactly as stored in the system
- Related test cases: TC-LOGIN-001 (Successful Login), TC-LOGIN-002 (Invalid Credentials)
- Consider adding user guidance to warn about space sensitivity
