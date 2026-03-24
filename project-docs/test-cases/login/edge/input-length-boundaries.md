# Input Length Boundaries in Login Fields

**Test Case ID**: TC-LOGIN-007  
**Priority**: Medium  
**Category**: Edge

## Overview
Validates that the system properly handles very long inputs in username and password fields. No maximum length restrictions are mentioned in the specification, so the system should accept very long inputs (~500 characters) but will fail authentication if credentials don't match.

## Preconditions
- Login page is accessible
- No maximum length restrictions are enforced
- Valid credentials are: Admin / admin123
- Very long inputs are accepted by the system

---

## Test Scenarios

### Scenario 1: Very Long Username (500 Characters)

**Test Data**:
- Username: 500-character string (e.g., "a" repeated 500 times)
- Password: admin123

**Test Steps**:
1. Navigate to the login page
2. Enter a 500-character string in the username field
3. Enter "admin123" in the password field
4. Click the Login button

**Expected Results**:
- Input is accepted without truncation or length validation error
- Login fails with "Invalid credentials" error message
- System handles the long input gracefully without crashing
- Page remains responsive

---

### Scenario 2: Very Long Password (500 Characters)

**Test Data**:
- Username: Admin
- Password: 500-character string (e.g., "b" repeated 500 times)

**Test Steps**:
1. Navigate to the login page
2. Enter "Admin" in the username field
3. Enter a 500-character string in the password field
4. Click the Login button

**Expected Results**:
- Input is accepted without truncation or length validation error
- Login fails with "Invalid credentials" error message
- System handles the long input gracefully without crashing
- Page remains responsive

---

### Scenario 3: Very Long Inputs in Both Fields (1000 Characters Total)

**Test Data**:
- Username: 500-character string (e.g., "x" repeated 500 times)
- Password: 500-character string (e.g., "y" repeated 500 times)

**Test Steps**:
1. Navigate to the login page
2. Enter a 500-character string in the username field
3. Enter a 500-character string in the password field
4. Click the Login button

**Expected Results**:
- Both inputs are accepted without truncation or length validation errors
- Login fails with "Invalid credentials" error message
- System handles the combined long inputs gracefully
- No performance degradation or timeout issues
- Page remains responsive

---

### Scenario 4: Extremely Long Username (1000 Characters)

**Test Data**:
- Username: 1000-character string
- Password: admin123

**Test Steps**:
1. Navigate to the login page
2. Enter a 1000-character string in the username field
3. Enter "admin123" in the password field
4. Click the Login button

**Expected Results**:
- Input is accepted (or shows appropriate length limit message if any)
- System handles the extremely long input without crashing
- Login fails with "Invalid credentials" error or length validation error
- No security vulnerabilities exposed (buffer overflow, injection attacks)

---

### Scenario 5: Single Character Inputs

**Test Data**:
- Username: "A" (single character)
- Password: "b" (single character)

**Test Steps**:
1. Navigate to the login page
2. Enter "A" in the username field
3. Enter "b" in the password field
4. Click the Login button

**Expected Results**:
- Inputs are accepted (no minimum length validation)
- Login fails with "Invalid credentials" error message
- System handles single-character inputs properly

---

## Notes
- No maximum length restrictions mentioned allows testing extreme boundaries
- System should handle long inputs gracefully without performance issues or crashes
- These tests help identify potential buffer overflow or memory issues
- Related test cases: TC-LOGIN-002 (Invalid Credentials)
- Consider implementing reasonable maximum length limits for security and UX
- Test data can be generated programmatically using string repetition
