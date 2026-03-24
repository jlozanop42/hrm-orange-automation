# Invalid Credentials Login Attempts

**Test Case ID**: TC-LOGIN-003  
**Priority**: High  
**Category**: Negative

## Overview
Validates that the system properly rejects login attempts with invalid credentials and displays appropriate error messages. Tests various combinations of invalid usernames and passwords, including case sensitivity validation.

## Preconditions
- User is on the HR Orange login page
- Valid credentials for testing: Username = "Admin", Password = "admin123"
- Browser is open and page is fully loaded

---

## Test Scenarios

### Scenario 1: Invalid Username with Valid Password

**Test Data**:
- Username: WrongUser
- Password: admin123

**Test Steps**:
1. Navigate to the login page
2. Enter "WrongUser" in the username field
3. Enter "admin123" in the password field
4. Click the Login button

**Expected Results**:
- Login attempt is rejected
- Page refreshes
- Error banner appears above username field with message "Invalid credentials"
- Both username and password fields are cleared
- User remains on the login page

---

### Scenario 2: Valid Username with Invalid Password

**Test Data**:
- Username: Admin
- Password: wrongpassword

**Test Steps**:
1. Navigate to the login page
2. Enter "Admin" in the username field
3. Enter "wrongpassword" in the password field
4. Click the Login button

**Expected Results**:
- Login attempt is rejected
- Page refreshes
- Error banner appears above username field with message "Invalid credentials"
- Both username and password fields are cleared
- User remains on the login page

---

### Scenario 3: Both Username and Password Invalid

**Test Data**:
- Username: InvalidUser
- Password: wrongpass123

**Test Steps**:
1. Navigate to the login page
2. Enter "InvalidUser" in the username field
3. Enter "wrongpass123" in the password field
4. Click the Login button

**Expected Results**:
- Login attempt is rejected
- Page refreshes
- Error banner appears above username field with message "Invalid credentials"
- Both username and password fields are cleared
- User remains on the login page

---

### Scenario 4: Lowercase Username with Valid Password (Case Sensitivity)

**Test Data**:
- Username: admin (lowercase)
- Password: admin123

**Test Steps**:
1. Navigate to the login page
2. Enter "admin" (lowercase) in the username field
3. Enter "admin123" in the password field
4. Click the Login button

**Expected Results**:
- Login attempt is rejected due to case sensitivity
- Page refreshes
- Error banner appears above username field with message "Invalid credentials"
- Both username and password fields are cleared
- User remains on the login page

---

### Scenario 5: Uppercase Username with Valid Password (Case Sensitivity)

**Test Data**:
- Username: ADMIN (uppercase)
- Password: admin123

**Test Steps**:
1. Navigate to the login page
2. Enter "ADMIN" (uppercase) in the username field
3. Enter "admin123" in the password field
4. Click the Login button

**Expected Results**:
- Login attempt is rejected due to case sensitivity
- Page refreshes
- Error banner appears above username field with message "Invalid credentials"
- Both username and password fields are cleared
- User remains on the login page

---

## Notes
- Username field is case-sensitive; only "Admin" (exact case) is valid
- The system does not perform whitespace trimming; spaces are treated as part of the input
- Error message is generic ("Invalid credentials") for security reasons - does not indicate which field is incorrect
- Related test cases: TC-LOGIN-001 (Successful Login), TC-LOGIN-004 (Required Field Validation)
