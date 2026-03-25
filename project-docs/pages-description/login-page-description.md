# Login Page

## Overview
The login page is the entry point for users to access the HR Orange system. It provides authentication functionality and additional support options.

## Page Structure

### Header Section
- **Image**: OrangeHRM logo/branding
  - Title attribute: "OrangeHRM"
  - Position: Top of page

### Login Form Section
- **Heading**: "Login"
  - Position: Below header image
- **Error Banner**: Invalid credentials message (displayed conditionally)
  - Text: "Invalid credentials"
  - Position: Above username input
  - Visibility: Only shown after failed login attempt
  - Error message: "Required" (displayed below input in red when empty and the login button is clicked)
- **Input Field**: Username
  - Label: "Username"
  - Type: Text input
  - Case-sensitivity: Not case-sensitive (e.g., "Admin", "ADMIN", and "admin" are treated identically)
- **Input Field**: Password
  - Label: "Password"
  - Type: Password input
  - Validation: Required field
  - Error message: "Required" (displayed below input in red when empty and the login button is clicked)
- **Button**: Login
  - Action: Submit credentials
  - Position: Below password input

### Support Section
- **Link**: "Forgot your password?"
  - Position: Below login button
  - Action: Navigate to password recovery

### Footer Section
- **Text**: OrangeHRM version information
- **Text**: Disclaimer/legal text
  - Position: Associated with version

### Social Media Section
- **Position**: Bottom left corner
- **Links**: Social media navigation
  - LinkedIn link
  - YouTube link
  - Twitter link
  - Facebook link

## Element Hierarchy

```
Top of page
├── Header
│   └── OrangeHRM Image/Logo (with title attribute)
├── Login Form
│   ├── "Login" Heading
│   ├── Error Banner (conditional - appears after invalid credentials)
│   │   └── "Invalid credentials" message
│   ├── Username Input
│   │   ├── "Username" Label
│   │   └── "Required" error text (conditional - appears below when empty and login button is clicked)
│   ├── Password Input
│   │   ├── "Password" Label
│   │   └── "Required" error text (conditional - appears below when empty and login button is clicked)
│   └── Login Button
├── Support Section
│   └── "Forgot your password?" Link
├── Footer
│   ├── OrangeHRM Version Text
│   └── Disclaimer Text
└── Social Media Links (Bottom Left)
    ├── LinkedIn
    ├── YouTube
    ├── Twitter
    └── Facebook
```

## Behavior & Interactions

### Successful Login
- **Action**: User enters valid username and password, then clicks the Login button
- **Result**: Application redirects to the dashboard page
- **Note**: No success message is displayed - the navigation itself indicates successful authentication
- **Username Behavior**: Username input is case-insensitive ("Admin", "ADMIN", and "admin" are all accepted as the same credentials)

### Invalid Credentials
- **Action**: User enters invalid username OR invalid password and clicks the Login button
- **Result**: 
  - Page is refreshed
  - Both input fields are cleared out
  - Error banner is displayed above the username field
  - Error message text: "Invalid credentials"

### Required Field Validation
- **Action**: User leaves username OR password field empty and clicks the Login button
- **Result**:
  - Red error text is displayed below the empty input field(s)
  - Error message text: "Required"
  - No page refresh occurs - validation is immediate

### Forgot Password Flow
- **Action**: User clicks the "Forgot your password?" link
- **Result**: User is redirected to a different page for password recovery

## Notes
- All form inputs have associated labels for accessibility
- Social media links are specifically positioned at bottom left
- Footer contains both informational elements (version, disclaimer)
- Single support link for password recovery functionality
- Clean, simple layout focused on authentication

## Purpose for Automation
This documentation serves as a reference when creating:
- Page Object Model classes for the login page
- Test cases for login functionality
- Element locator strategies
- Accessibility validation tests
