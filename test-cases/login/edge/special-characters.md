# Special Characters in Login Fields

**Test Case ID**: TC-LOGIN-008  
**Priority**: Medium  
**Category**: Edge

## Overview
Validates that the system properly handles special characters in username and password fields. Special characters are accepted as input and processed correctly without causing errors or security vulnerabilities.

## Preconditions
- Login page is accessible
- Special characters are accepted in input fields
- Valid credentials are: Admin / admin123
- System does not sanitize or reject special characters

---

## Test Scenarios

### Scenario 1: Special Characters in Username

**Test Data**:
- Username: "Admin@#$%"
- Password: admin123

**Test Steps**:
1. Navigate to the login page
2. Enter "Admin@#$%" in the username field
3. Enter "admin123" in the password field
4. Click the Login button

**Expected Results**:
- Special characters are accepted as input
- Login fails with "Invalid credentials" error message
- No JavaScript errors or unexpected behavior
- Input is properly encoded/escaped to prevent injection attacks

---

### Scenario 2: Special Characters in Password

**Test Data**:
- Username: Admin
- Password: "admin123!@#$%^&*()"

**Test Steps**:
1. Navigate to the login page
2. Enter "Admin" in the username field
3. Enter "admin123!@#$%^&*()" in the password field
4. Click the Login button

**Expected Results**:
- Special characters are accepted as input
- Login fails with "Invalid credentials" error message
- Password field properly masks special characters
- No JavaScript errors or unexpected behavior

---

### Scenario 3: SQL Injection Attempt in Username

**Test Data**:
- Username: "Admin' OR '1'='1"
- Password: admin123

**Test Steps**:
1. Navigate to the login page
2. Enter "Admin' OR '1'='1" in the username field
3. Enter "admin123" in the password field
4. Click the Login button

**Expected Results**:
- Input is accepted and properly escaped/sanitized
- Login fails with "Invalid credentials" error message
- SQL injection attack is prevented
- No unauthorized access granted
- No database errors exposed

---

### Scenario 4: XSS Attempt in Username

**Test Data**:
- Username: "<script>alert('XSS')</script>"
- Password: admin123

**Test Steps**:
1. Navigate to the login page
2. Enter "<script>alert('XSS')</script>" in the username field
3. Enter "admin123" in the password field
4. Click the Login button

**Expected Results**:
- Input is accepted and properly escaped
- No script execution occurs
- Login fails with "Invalid credentials" error message
- Error message displays without executing embedded script
- XSS attack is prevented

---

### Scenario 5: Unicode and Emoji Characters

**Test Data**:
- Username: "Admin🔒😀"
- Password: "admin123™€¥"

**Test Steps**:
1. Navigate to the login page
2. Enter "Admin🔒😀" in the username field
3. Enter "admin123™€¥" in the password field
4. Click the Login button

**Expected Results**:
- Unicode and emoji characters are accepted as input
- Characters are properly displayed and encoded
- Login fails with "Invalid credentials" error message
- No character encoding errors

---

### Scenario 6: Special Characters from Different Categories

**Test Data**:
- Username: "Admin<>[]{}|\\/"
- Password: "admin123`~;:'\""

**Test Steps**:
1. Navigate to the login page
2. Enter "Admin<>[]{}|\\/" in the username field
3. Enter "admin123`~;:'\"" in the password field
4. Click the Login button

**Expected Results**:
- All special characters are accepted as input
- Characters are properly escaped and encoded
- Login fails with "Invalid credentials" error message
- No parsing errors or unexpected behavior

---

## Notes
- Special character handling is critical for security testing
- These tests help identify injection vulnerabilities (SQL, XSS, etc.)
- System should accept special characters but properly escape/sanitize them
- Related test cases: TC-LOGIN-002 (Invalid Credentials)
- Consider testing with different character encodings (UTF-8, UTF-16, etc.)
- Password fields should support special characters as they strengthen security
