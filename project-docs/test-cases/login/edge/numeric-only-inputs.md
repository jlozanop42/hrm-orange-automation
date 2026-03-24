# Numeric-Only Inputs in Login Fields

**Test Case ID**: TC-LOGIN-009  
**Priority**: Low  
**Category**: Edge

## Overview
Validates that the system properly handles numeric-only inputs in username and password fields. Numeric values are accepted as valid input characters and processed correctly.

## Preconditions
- Login page is accessible
- Numeric-only inputs are accepted in input fields
- Valid credentials are: Admin / admin123
- System does not restrict input to alphabetic characters only

---

## Test Scenarios

### Scenario 1: Numeric-Only Username

**Test Data**:
- Username: "12345"
- Password: admin123

**Test Steps**:
1. Navigate to the login page
2. Enter "12345" in the username field
3. Enter "admin123" in the password field
4. Click the Login button

**Expected Results**:
- Numeric input is accepted in username field
- Login fails with "Invalid credentials" error message
- No validation error about input type
- System treats numeric input as valid text

---

### Scenario 2: Numeric-Only Password

**Test Data**:
- Username: Admin
- Password: "98765432"

**Test Steps**:
1. Navigate to the login page
2. Enter "Admin" in the username field
3. Enter "98765432" in the password field
4. Click the Login button

**Expected Results**:
- Numeric input is accepted in password field
- Password is properly masked
- Login fails with "Invalid credentials" error message
- No validation error about input type

---

### Scenario 3: Numeric-Only in Both Fields

**Test Data**:
- Username: "123456"
- Password: "789012"

**Test Steps**:
1. Navigate to the login page
2. Enter "123456" in the username field
3. Enter "789012" in the password field
4. Click the Login button

**Expected Results**:
- Numeric inputs are accepted in both fields
- Login fails with "Invalid credentials" error message
- No validation errors about input type
- System processes numeric inputs as text

---

### Scenario 4: Large Numeric Values

**Test Data**:
- Username: "999999999999999999"
- Password: "123456789012345678"

**Test Steps**:
1. Navigate to the login page
2. Enter "999999999999999999" in the username field
3. Enter "123456789012345678" in the password field
4. Click the Login button

**Expected Results**:
- Large numeric values are accepted as text (not parsed as numbers)
- No overflow errors or unexpected behavior
- Login fails with "Invalid credentials" error message
- Values are not converted to scientific notation

---

### Scenario 5: Numeric with Leading Zeros

**Test Data**:
- Username: "00123"
- Password: "00789"

**Test Steps**:
1. Navigate to the login page
2. Enter "00123" in the username field
3. Enter "00789" in the password field
4. Click the Login button

**Expected Results**:
- Leading zeros are preserved (not stripped)
- Inputs are treated as text, not numbers
- Login fails with "Invalid credentials" error message
- "00123" is not converted to "123"

---

### Scenario 6: Negative Numbers and Decimal Points

**Test Data**:
- Username: "-123"
- Password: "45.67"

**Test Steps**:
1. Navigate to the login page
2. Enter "-123" in the username field
3. Enter "45.67" in the password field
4. Click the Login button

**Expected Results**:
- Negative signs and decimal points are accepted as special characters
- Inputs are treated as text strings
- Login fails with "Invalid credentials" error message
- No numeric parsing or validation

---

## Notes
- Numeric inputs should be treated as text, not parsed as numbers
- This ensures flexibility for usernames/passwords that may be purely numeric
- Leading zeros should be preserved
- Related test cases: TC-LOGIN-008 (Special Characters), TC-LOGIN-002 (Invalid Credentials)
- Some systems use numeric-only employee IDs as usernames
- Password fields commonly include numbers, so pure numeric passwords should be supported
