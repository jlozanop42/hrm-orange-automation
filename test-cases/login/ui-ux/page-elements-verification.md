# Page Elements Verification

**Test Case ID**: TC-LOGIN-011  
**Priority**: High  
**Category**: UI/UX

## Overview
Validates that all UI elements on the login page are present, properly positioned, and display correct content including logo, heading, labels, input fields, buttons, links, footer, and social media icons.

## Preconditions
- Navigate to the login page
- Login page is fully loaded
- Browser viewport is set to standard desktop size

---

## Test Scenarios

### Scenario 1: Logo and Branding Verification

**Test Data**:
- N/A

**Test Steps**:
1. Navigate to the login page
2. Locate the OrangeHRM logo/image at the top of the page
3. Verify logo has a title attribute
4. Check logo positioning

**Expected Results**:
- OrangeHRM logo is visible at the top of the page
- Logo image has a title attribute
- Logo is properly positioned and centered/aligned as per design
- Logo image loads without errors

---

### Scenario 2: Page Heading Verification

**Test Data**:
- N/A

**Test Steps**:
1. Navigate to the login page
2. Locate the heading element
3. Verify heading text content

**Expected Results**:
- "Login" heading is visible on the page
- Heading uses appropriate HTML semantic element (h1, h2, etc.)
- Heading text is clearly readable
- Heading is properly positioned above the login form

---

### Scenario 3: Input Fields and Labels Verification

**Test Data**:
- N/A

**Test Steps**:
1. Navigate to the login page
2. Locate the username input field and its label
3. Locate the password input field and its label
4. Verify labels are associated with inputs

**Expected Results**:
- Username input field is present with "Username" label
- Password input field is present with "Password" label
- Labels are properly associated with their respective input fields
- Input fields are clearly visible and properly sized
- Labels are positioned above or adjacent to input fields

---

### Scenario 4: Login Button Verification

**Test Data**:
- N/A

**Test Steps**:
1. Navigate to the login page
2. Locate the Login button
3. Verify button text and styling
4. Check button is clickable

**Expected Results**:
- Login button is visible and displays appropriate text
- Button is styled as a primary action button
- Button is enabled and clickable
- Button is properly positioned below the input fields

---

### Scenario 5: Forgot Password Link Verification

**Test Data**:
- N/A

**Test Steps**:
1. Navigate to the login page
2. Locate the "Forgot your password?" link
3. Verify link text and styling
4. Check link is clickable

**Expected Results**:
- "Forgot your password?" link is visible
- Link text displays exactly "Forgot your password?"
- Link is styled appropriately (underlined or distinct color)
- Link is clickable
- Link is positioned near the password field or login button

---

### Scenario 6: Footer Content Verification

**Test Data**:
- N/A

**Test Steps**:
1. Navigate to the login page
2. Scroll to the bottom of the page if necessary
3. Locate the footer section
4. Verify footer contains version and disclaimer text

**Expected Results**:
- Footer is visible at the bottom of the page
- Footer displays version information
- Footer displays disclaimer text
- Footer content is readable and properly formatted

---

### Scenario 7: Social Media Links Verification

**Test Data**:
- N/A

**Test Steps**:
1. Navigate to the login page
2. Locate social media icons at the bottom left
3. Verify all four social media platforms are present
4. Check icons are clickable

**Expected Results**:
- LinkedIn icon/link is present at bottom left
- YouTube icon/link is present at bottom left
- Twitter icon/link is present at bottom left
- Facebook icon/link is present at bottom left
- All icons are clickable
- Icons are properly styled and recognizable

---

### Scenario 8: Complete Page Layout Verification

**Test Data**:
- N/A

**Test Steps**:
1. Navigate to the login page
2. Perform a comprehensive visual verification
3. Check all elements are present in correct order
4. Verify page layout matches design specifications

**Expected Results**:
- All page elements are present: logo, heading, username field, password field, login button, forgot password link, footer, social media links
- Elements are arranged in logical order from top to bottom
- Page layout is centered and properly aligned
- No missing or broken UI components
- Page is responsive and elements are properly sized

---

## Notes
- This test case verifies the structural integrity of the login page
- All elements should be present regardless of interaction state
- Automation should verify both presence and visibility of elements
- Consider using visual regression testing for comprehensive UI validation
- Test should pass on first page load without any user interaction
- Verify elements using stable locators (IDs, data-test attributes, or semantic HTML)
