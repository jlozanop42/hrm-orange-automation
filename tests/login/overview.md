# Login Feature - Test Cases Overview

## Feature Description
The Login feature provides authentication functionality for the HR Orange system. Users enter their username and password credentials to access the application. The feature includes error handling for invalid inputs, required field validation, and navigation to password recovery.

---

## Test Summary

| Category | Test Cases | Scenarios | File Count |
|----------|-----------|-----------|------------|
| Positive | 2 | 2 | 2 |
| Negative | 2 | 8 | 2 |
| Edge | 5 | 27 | 5 |
| UI/UX | 3 | 22 | 3 |
| **Total** | **12** | **59** | **12** |

---

## Valid Test Credentials

| Field | Value |
|-------|-------|
| Username | `Admin` |
| Password | `admin123` |

**Important Notes**:
- Username is **case-sensitive** (`Admin` ≠ `admin` ≠ `ADMIN`)
- No whitespace trimming (leading/trailing spaces cause authentication failure)
- Exact match required for successful login

---

## Expected URLs

| Action | URL |
|--------|-----|
| Successful Login → Dashboard | `https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index` |
| Forgot Password Link | `https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode` |

---

## Test Case Index

### Positive Test Cases

| ID | Test Case | Priority | File |
|----|-----------|----------|------|
| TC-LOGIN-001 | Successful Login | High | [successful-login.md](positive/successful-login.md) |
| TC-LOGIN-002 | Forgot Password Navigation | Medium | [forgot-password-navigation.md](positive/forgot-password-navigation.md) |

**Coverage**: 
- Valid credential authentication and dashboard navigation
- Password recovery link functionality

---

### Negative Test Cases

| ID | Test Case | Priority | File |
|----|-----------|----------|------|
| TC-LOGIN-003 | Invalid Credentials Attempts | High | [invalid-credentials.md](negative/invalid-credentials.md) |
| TC-LOGIN-004 | Required Field Validation | High | [required-fields.md](negative/required-fields.md) |

**Coverage**:
- Invalid username/password combinations (5 scenarios)
- Case sensitivity validation
- Empty field validation (3 scenarios)
- Error message display verification

---

### Edge Cases

| ID | Test Case | Priority | File |
|----|-----------|----------|------|
| TC-LOGIN-005 | Whitespace Handling | High | [whitespace-handling.md](edge/whitespace-handling.md) |
| TC-LOGIN-006 | Whitespace-Only Inputs | Medium | [whitespace-only-inputs.md](edge/whitespace-only-inputs.md) |
| TC-LOGIN-007 | Input Length Boundaries | Medium | [input-length-boundaries.md](edge/input-length-boundaries.md) |
| TC-LOGIN-008 | Special Characters | Medium | [special-characters.md](edge/special-characters.md) |
| TC-LOGIN-009 | Numeric-Only Inputs | Low | [numeric-only-inputs.md](edge/numeric-only-inputs.md) |

**Coverage**:
- Leading/trailing whitespace handling (5 scenarios)
- Whitespace-only inputs treated as empty (5 scenarios)
- Very long inputs and boundary conditions (5 scenarios)
- Special characters, SQL injection attempts, XSS, unicode (6 scenarios)
- Numeric-only username/password inputs (6 scenarios)

---

### UI/UX Test Cases

| ID | Test Case | Priority | File |
|----|-----------|----------|------|
| TC-LOGIN-010 | Error Message Display | High | [error-message-display.md](ui-ux/error-message-display.md) |
| TC-LOGIN-011 | Page Elements Verification | High | [page-elements-verification.md](ui-ux/page-elements-verification.md) |
| TC-LOGIN-012 | Field Interactions | High | [field-interactions.md](ui-ux/field-interactions.md) |

**Coverage**:
- Error banner and "Required" text visibility (6 scenarios)
- All page element presence and positioning (8 scenarios)
- Password masking, input acceptance, field clearing (8 scenarios)

---

## Known System Behaviors

### Authentication
- ✅ Valid credentials: `Admin` / `admin123` (exact match, case-sensitive)
- ❌ Invalid credentials: Any variation triggers "Invalid credentials" error
- ❌ Empty fields: Trigger "Required" validation error

### Error Handling
- **Invalid Credentials**: Page refreshes, both fields cleared, error banner appears above username field
- **Required Fields**: No page refresh, red "Required" text appears below empty field(s)

### Input Processing
- ❌ **No whitespace trimming**: Leading/trailing spaces are NOT removed
- ❌ **No input sanitization**: Special characters accepted as-is
- ✅ **Whitespace-only = empty**: Inputs with only spaces trigger required validation

### UI Behavior
- **Password Masking**: Password field type is "password", characters displayed as dots
- **Field Clearing**: Both username and password fields cleared after invalid login attempt
- **Error Positioning**: Error banner above username, "Required" errors below respective fields

---

## Test Execution Guidelines

### Recommended Execution Order

1. **Positive Test Cases** (TC-LOGIN-001 to TC-LOGIN-002)
   - Verify core functionality works
   - Establish baseline behavior
   - Priority: Run first

2. **Negative Test Cases** (TC-LOGIN-003 to TC-LOGIN-004)
   - Validate error handling
   - Verify security measures
   - Priority: Run second

3. **Edge Cases** (TC-LOGIN-005 to TC-LOGIN-009)
   - Test boundary conditions
   - Ensure robustness
   - Priority: Run third

4. **UI/UX Cases** (TC-LOGIN-010 to TC-LOGIN-012)
   - Verify visual elements
   - Validate user experience
   - Priority: Run last

### Prerequisites
- Access to HR Orange login page
- Valid test credentials (Admin / admin123)
- Dashboard page must be accessible for post-login verification
- Password reset page must be accessible for forgot password flow

### Test Data Requirements
- Valid credentials stored in configuration or environment variables
- Test data sets for invalid credentials, special characters, long strings
- Expected URLs for navigation verification

---

## Automation Considerations

### Wait Strategies
- **Explicit waits** for error banner visibility after invalid login
- **URL change waits** after successful login before asserting dashboard elements
- **Element state waits** for error text appearance after required field validation

### Verification Techniques
- **URL validation**: Use regex pattern matching for forgot password URL
- **Field clearing**: Verify input values are empty strings after invalid login
- **Password masking**: Verify input type attribute is "password"

### Selectors and Locators
- Use stable selectors (IDs, data-test attributes) when available
- Have fallback strategies for dynamic elements
- Consider element hierarchy for error message locators

### Test Data Management
- Parameterize credentials for easy updates
- Generate long strings programmatically for edge cases
- Store expected URLs in configuration for maintainability

---

## Scope Exclusions

### Not Covered
- ❌ Account lockout mechanisms (not implemented in the system)
- ❌ Password complexity requirements (no restrictions exist)
- ❌ "Remember me" functionality (not available)
- ❌ Multiple user roles (only one valid user exists)
- ❌ Session timeout scenarios (out of scope)
- ❌ Two-factor authentication (not implemented)
- ❌ CAPTCHA after failed attempts (not implemented)

---

## Dependencies

### Page Dependencies
- **Login Page**: Must be accessible for all test cases
- **Dashboard Page**: Required for successful login verification (TC-LOGIN-001)
- **Password Reset Page**: Required for forgot password flow (TC-LOGIN-002)

### External Dependencies
- None (no external APIs or services required for login testing)

---

## Related Documentation

| Document | Location | Purpose |
|----------|----------|---------|
| Login Page Description | [/pages-description/login-page-description.md](../../pages-description/login-page-description.md) | UI structure and element details |
| Dashboard Page Description | [/pages-description/dashboard-page-description.md](../../pages-description/dashboard-page-description.md) | Post-login page details |
| Login Page Object | [/pages/login_page.py](../../pages/login_page.py) | Page Object Model implementation |
| Test Implementation | [/tests/test_login.py](../test_login.py) | Automated test code |

---

## Notes

### Test Case Naming Convention
- **Format**: `TC-LOGIN-XXX` where XXX is a digit sequential number
- **File Naming**: lowercase-with-hyphens.md
- **Grouping**: Similar scenarios grouped into single test case files

### Priority Levels
| Priority | Description |
|----------|-------------|
| **High** | Critical functionality that must work for the system to be usable |
| **Medium** | Important functionality that affects user experience |
| **Low** | Nice-to-have validations or less common scenarios |

### Category Definitions
| Category | Purpose |
|----------|---------|
| **Positive** | Tests that verify expected successful behavior |
| **Negative** | Tests that verify proper error handling for invalid inputs |
| **Edge** | Tests that verify boundary conditions and unusual inputs |
| **UI/UX** | Tests that verify visual elements and user interface behavior |

---

## Maintenance

### Updating Test Cases
When system behavior changes:
1. Update affected test case files in respective category folders
2. Update this overview with new expectations
3. Update test data tables if credentials or URLs change
4. Add new test cases with next sequential TC number

### Adding New Test Cases
1. Determine appropriate category (positive/negative/edge/ui-ux)
2. Check if scenario fits into existing test case file or needs new file
3. Use next available TC-LOGIN-XXX number
4. Update this overview file with new test case entry
5. Update summary statistics

---

**Last Updated**: March 24, 2026  
**Total Test Cases**: 12  
**Total Scenarios**: 59  
**Status**: ✅ Complete
