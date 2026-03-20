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
- **Input Field**: Username
  - Label: "Username"
  - Type: Text input
- **Input Field**: Password
  - Label: "Password"
  - Type: Password input
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
│   ├── Username Input
│   │   └── "Username" Label
│   ├── Password Input
│   │   └── "Password" Label
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
