# Successful Login with Valid Credentials

**Test Case ID**: TC-LOGIN-001  
**Priority**: High  
**Category**: Positive

## Overview
Validates that a user can successfully log into the OrangeHRM system using valid credentials and is redirected to the dashboard page.

## Preconditions
- User is on the login page
- User has valid credentials (Admin/admin123)
- Browser is supported and up to date
- System is accessible and operational

---

## Test Scenarios

### Scenario 1: Login with Valid Admin Credentials

**Test Data**:
- Username: Admin
- Password: admin123

**Test Steps**:
1. Navigate to the OrangeHRM login page
2. Enter "Admin" in the Username field
3. Enter "admin123" in the Password field
4. Click the "Login" button

**Expected Results**:
- User is successfully authenticated
- Page redirects to dashboard URL: `https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index`
- Dashboard page is displayed
- "Dashboard" menu item is highlighted/selected in the navigation
- No error messages or banners are displayed
- User session is established

---

## Notes
- This is the primary happy path scenario for login functionality
- Credentials must match exactly (case-sensitive)
- Related test cases: TC-LOGIN-002 (Forgot Password Navigation)
- Session should persist across page refreshes until logout
