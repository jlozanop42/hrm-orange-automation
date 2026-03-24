# Field Interactions and Behavior

**Test Case ID**: TC-LOGIN-012  
**Priority**: High  
**Category**: UI/UX

## Overview
Validates the interactive behavior of input fields on the login page including password masking, text input acceptance, and field clearing after invalid login attempts.

## Preconditions
- Navigate to the login page
- Login page is fully loaded
- Input fields are visible and enabled

---

## Test Scenarios

### Scenario 1: Password Field Masking

**Test Data**:
- Password: TestPassword123

**Test Steps**:
1. Navigate to the login page
2. Locate the password input field
3. Verify the field type attribute is "password"
4. Enter a password into the field
5. Observe the displayed characters

**Expected Results**:
- Password field has type="password" attribute
- Characters entered are masked (displayed as dots or asterisks)
- Actual password text is not visible in the field
- Password remains masked while typing
- Password remains masked after input is complete

---

### Scenario 2: Username Field Accepts Text Input

**Test Data**:
- Username: TestUser123

**Test Steps**:
1. Navigate to the login page
2. Click on the username input field
3. Type alphanumeric text
4. Verify text appears in the field

**Expected Results**:
- Username field accepts keyboard input
- Text appears in plain text (not masked)
- Entered text is visible and readable
- Field displays the complete entered username
- No character limit prevents reasonable username entry

---

### Scenario 3: Password Field Accepts Text Input

**Test Data**:
- Password: SecureP@ssw0rd!

**Test Steps**:
1. Navigate to the login page
2. Click on the password input field
3. Type alphanumeric text with special characters
4. Verify input is accepted

**Expected Results**:
- Password field accepts keyboard input
- Field accepts letters, numbers, and special characters
- Characters are masked as they are typed
- No character limit prevents reasonable password entry
- All standard keyboard characters are accepted

---

### Scenario 4: Username Field Accepts Special Characters

**Test Data**:
- Username: user@company.com

**Test Steps**:
1. Navigate to the login page
2. Click on the username input field
3. Type text including special characters (@ and .)
4. Verify input is accepted

**Expected Results**:
- Username field accepts special characters
- Email format usernames are supported
- @ and . characters are accepted
- Text is displayed as typed (in plain text)

---

### Scenario 5: Fields Cleared After Invalid Login Attempt

**Test Data**:
- Username: InvalidUser
- Password: InvalidPass123

**Test Steps**:
1. Navigate to the login page
2. Enter invalid username
3. Enter invalid password
4. Click the Login button
5. Wait for page refresh
6. Observe the state of both input fields

**Expected Results**:
- Page refreshes after login attempt
- Username field is cleared (empty)
- Password field is cleared (empty)
- Both fields are ready for new input
- Error banner is displayed showing "Invalid credentials"

---

### Scenario 6: Username Field Retains Value on Required Error

**Test Data**:
- Username: ValidUser
- Password: (empty)

**Test Steps**:
1. Navigate to the login page
2. Enter username
3. Leave password field empty
4. Click the Login button
5. Observe the username field state

**Expected Results**:
- Username field retains the entered value
- No page refresh occurs
- "Required" error appears below password field only
- Username field value remains visible and editable

---

### Scenario 7: Password Field Retains Value on Required Error

**Test Data**:
- Username: (empty)
- Password: ValidPassword123

**Test Steps**:
1. Navigate to the login page
2. Leave username field empty
3. Enter password
4. Click the Login button
5. Observe the password field state

**Expected Results**:
- Password field retains the entered value (as masked characters)
- No page refresh occurs
- "Required" error appears below username field only
- Password field value remains present (though masked)

---

### Scenario 8: Field Focus and Navigation

**Test Data**:
- N/A

**Test Steps**:
1. Navigate to the login page
2. Click on the username field
3. Verify field receives focus
4. Press Tab key
5. Verify focus moves to password field
6. Press Tab key again
7. Verify focus moves to Login button

**Expected Results**:
- Username field receives focus when clicked
- Tab key navigates from username to password field
- Tab key navigates from password to Login button
- Keyboard navigation follows logical tab order
- Focused fields show visual focus indicator

---

## Notes
- Password masking is a critical security feature and must always function correctly
- Field clearing after invalid login is a security best practice (prevents password shoulder surfing)
- Field retention on "Required" errors is a UX best practice (prevents data loss)
- The behavior differs based on error type: page refresh for invalid credentials vs. no refresh for required field errors
- Automation should verify actual DOM attributes (type="password") not just visual appearance
- Consider testing with different input types: alphanumeric, special characters, unicode characters
- Verify fields are enabled and not set to readonly or disabled states
