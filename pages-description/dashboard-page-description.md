# Dashboard Page

## Overview
The dashboard page is the main landing page displayed after successful login. It provides an overview of HR-related information through various cards and serves as the central hub for navigation to other system modules. This page is only accessible to authenticated users.

**URL**: `https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index`

## Page Structure

### Left Navigation Panel
- **Link**: OrangeHRM
  - Content: Company name/branding
  - Position: Top of navigation panel
  - Action: Navigates to OrangeHRM website in the same tab

- **Input Field**: Search
  - Type: Search input
  - Purpose: Search functionality for navigation items

- **Navigation Menu Items**:
  - Admin
  - PIM
  - Leave
  - Time
  - Recruitment
  - My Info
  - Performance
  - Dashboard (Default - highlighted/selected after sign in)
  - Directory
  - Maintenance
  - Claim
  - Buzz

### Top Header Strip
- **Title**: "Dashboard"
  - Position: Top left
- **Button**: Upgrade
  - Position: Right side of the strip
- **Button**: Username button
    It's divided in username image, user name and an down arrow.
  - Content: Displays the logged-in user's name
  - Position: Right side of the strip

### Second Header Strip
- **Icon**: Help icon
  - Position: Right side of the strip

### Dashboard Content Area (Cards Section)
Multiple information cards are displayed, each containing a title and content:

- **Card**: Time at Work
  - Contains work time-related information

- **Card**: My Actions
  - Contains action items or tasks for the user

- **Card**: Quick Launch
  - Provides quick access to common functions

- **Card**: Buzz Latest Posts
  - Displays recent social/communication updates

- **Card**: Employees on Leave Today
  - Shows information about employees currently on leave

- **Card**: Employee Distribution by Sub Unit
  - Displays employee distribution data by organizational sub-units

- **Card**: Employee Distribution by Location
  - Displays employee distribution data by location

## Element Hierarchy

```
Dashboard Page
├── Left Navigation Panel
│   ├── OrangeHRM Link (Top)
│   ├── Search Input
│   └── Navigation Menu
│       ├── Admin
│       ├── PIM
│       ├── Leave
│       ├── Time
│       ├── Recruitment
│       ├── My Info
│       ├── Performance
│       ├── Dashboard (Selected by default)
│       ├── Directory
│       ├── Maintenance
│       ├── Claim
│       └── Buzz
├── Top Header Strip
│   ├── "Dashboard" Title
│   ├── Upgrade Button (Right)
│   └── Username Button (Right)
├── Second Header Strip
│   └── Help Icon (Right)
└── Dashboard Content Area
    ├── Time at Work Card
    ├── My Actions Card
    ├── Quick Launch Card
    ├── Buzz Latest Posts Card
    ├── Employees on Leave Today Card
    ├── Employee Distribution by Sub Unit Card
    └── Employee Distribution by Location Card
```

## Behavior & Interactions
- **After Successful Login**: The application automatically navigates to the dashboard page, with the "Dashboard" menu item selected by default in the left navigation panel
- **Access Control**: This page is only accessible to authenticated users; attempting to access without valid credentials redirects to the login page
- **Navigation Menu**: Each menu item in the left panel is clickable and navigates to the corresponding module
- **Search Functionality**: The search input allows users to search for navigation items or other content
- **OrangeHRM Link**: Clicking navigates to the OrangeHRM website in the same tab
- **Username Button**: Clicking displays a submenu with the following options:
  - About
  - Support
  - Change Password
  - Logout
- **Upgrade Button**: Clicking opens a new page in a different tab to upgrade features
- **Help Icon**: Clicking displays resources and guides in a different page
- **Dashboard Cards**: Each card displays specific information and may be interactive (cards may have links, buttons, or expandable content)

## Notes
- The dashboard is the default landing page after authentication
- The left navigation panel is persistent across all pages (global navigation)
- Cards may have different layouts and content types depending on the information they display
- The "Dashboard" menu item is highlighted/selected by default when viewing this page
- Two separate header strips suggest a hierarchical header structure (main header + secondary toolbar)
