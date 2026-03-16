---
description: "Page Object Model patterns and best practices for HR Orange Automation - Modern Playwright approach"
applyTo: "pages/**/*.py"
---

# Page Object Guidelines

## Overview

This document defines how to write page objects using modern Playwright patterns. **This is NOT Selenium** - avoid applying Selenium patterns.

## Core Principles

- **One class per page** or major UI component
- **Use Playwright's built-in locators** (`get_by_role`, `get_by_label`, etc.)
- **No BasePage inheritance** - use `self.page` directly
- **Return Locators or use ensure methods** - both patterns are valid
- **No string constants for locators** - old Selenium antipattern

## Locator Strategies

### Priority Order (MUST FOLLOW)

#### 1. PREFERRED: Built-in Locator Methods

Use Playwright's user-facing locators directly. No constants needed.

```python
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
    
    def login(self, username: str, password: str):
        # Direct use of built-in locators
        self.page.get_by_label("Username").fill(username)
        self.page.get_by_label("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
    
    def search_employee(self, name: str):
        self.page.get_by_placeholder("Search").fill(name)
        self.page.get_by_role("button", name="Search").click()
```

**Built-in Locator Methods (in priority order)**:
1. `page.get_by_role()` - ARIA roles (button, link, textbox, heading, checkbox, etc.)
2. `page.get_by_label()` - Form fields with associated `<label>`
3. `page.get_by_placeholder()` - Inputs with placeholder text
4. `page.get_by_text()` - Elements containing visible text
5. `page.get_by_test_id()` - Elements with `data-testid` attribute
6. `page.get_by_title()` - Elements with title attribute
7. `page.get_by_alt_text()` - Images with alt text

#### 2. FALLBACK: Properties Returning Locators

Use **ONLY** when:
- Same complex locator is reused multiple times
- HTML structure is complex and built-in locators don't work
- Need to chain locators for scoping

```python
from playwright.sync_api import Page, Locator

class EmployeeListPage:
    def __init__(self, page: Page):
        self.page = page
    
    # Property for reused/complex locator
    @property
    def employee_table(self) -> Locator:
        return self.page.locator("table.employees")
    
    @property
    def first_employee_row(self) -> Locator:
        return self.employee_table.locator("tbody tr").first
    
    def get_employee_name(self, row_index: int) -> str:
        # Reuse the property
        return self.employee_table.locator(f"tbody tr:nth-child({row_index}) td.name").inner_text()
    
    def click_add_button(self):
        # Simple actions use built-in locators directly
        self.page.get_by_role("button", name="Add Employee").click()
```

#### 3. NEVER: String Constants

**DO NOT** use string constants for locators. This is an old Selenium pattern.

```python
# ❌ WRONG - DO NOT DO THIS
class LoginPage:
    USERNAME_INPUT = "[data-testid='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = ".submit-btn"
    
    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)  # ❌ Wrong
        self.page.click(self.LOGIN_BUTTON)  # ❌ Wrong
```

### Locator Best Practices

**DO**:
- ✅ Prefer user-facing attributes (roles, labels, text)
- ✅ Use semantic HTML when possible
- ✅ Chain locators for scoping: `page.get_by_role("table").get_by_role("row").first`
- ✅ Use `page.locator()` for CSS/XPath only when built-in methods fail
- ✅ Use `exact=True` for precise text matching

**DON'T**:
- ❌ Use string constants for locators
- ❌ Rely on DOM structure (nth-child, complex CSS selectors)
- ❌ Use dynamic/generated class names
- ❌ Create wrapper methods around Playwright's page methods

### Lazy Locators (Critical Concept)

**In Playwright, locators are lazy** - they don't query the DOM until used.

```python
# This does NOT query the DOM:
locator = page.get_by_role("button", name="Submit")

# DOM query happens ONLY when you perform an action or assertion:
expect(locator).to_be_visible()  # ← DOM queried here
locator.click()                   # ← Or here
```

**Why This Matters**:
- Locators remain valid across re-renders
- No stale element references (unlike Selenium WebElement)
- Assertions naturally synchronize with UI
- Tests are more resilient to timing issues

## Page Object Patterns

### Pattern A: Return Locators (Conservative)

**When to Use**: Tests need full control over assertions

```python
from playwright.sync_api import Page, Locator

class OrdersPage:
    def __init__(self, page: Page):
        self.page = page
    
    def get_order_row(self, order_id: str) -> Locator:
        """Return locator for order row"""
        return self.page.get_by_role("row").filter(has_text=order_id)
    
    def get_order_name_cell(self, order_id: str) -> Locator:
        """Return locator for order name cell"""
        return self.get_order_row(order_id).locator("td:nth-child(2)")
    
    def get_status_badge(self, order_id: str) -> Locator:
        """Return locator for order status badge"""
        return self.get_order_row(order_id).locator(".status-badge")
```

**Characteristics**:
- ✅ Clear separation of concerns
- ✅ Test has full control over assertions
- ✅ Familiar to those transitioning from Selenium

### Pattern B: Ensure Methods (Playwright-Idiomatic)

**When to Use**: Validating UI readiness and state

```python
from playwright.sync_api import Page, expect

class OrdersPage:
    def __init__(self, page: Page):
        self.page = page
    
    def ensure_order_is_visible(self, order_id: str):
        """Ensure order appears in list (UI invariant)"""
        expect(self.page.get_by_role("row").filter(has_text=order_id)).to_be_visible()
    
    def ensure_page_loaded(self):
        """Ensure page is ready (UI invariant)"""
        expect(self.page.get_by_role("heading", name="My Orders")).to_be_visible()
        expect(self.page.get_by_role("table")).to_be_visible()
    
    def get_order_count(self) -> int:
        """Get number of orders displayed"""
        return self.page.get_by_role("row").count() - 1  # Exclude header
```

**Characteristics**:
- ✅ Strong synchronization
- ✅ Less test boilerplate
- ✅ Better error diagnostics
- ✅ More Playwright-idiomatic

**Both patterns are valid. Choose based on context.**

## Assertions in Page Objects

### What IS Acceptable (UI Invariants)

**✅ OK** - These enforce UI readiness, not business logic:

- Element visibility: `expect(locator).to_be_visible()`
- Element presence: `expect(locator).to_be_attached()`
- Text existence: `expect(locator).to_contain_text("something")`
- Element count: `expect(locator).to_have_count(5)`
- Page readiness: `expect(heading).to_be_visible()`
- State checks: `expect(checkbox).to_be_checked()`

### What IS NOT Acceptable (Business Logic)

**❌ NO** - These belong in tests:

- Business rules: "Order total should equal sum of items"
- Calculations: "Discount should be 10% of subtotal"
- Cross-page workflows: "Cart should update after adding item"
- Data validation: "Email format should be valid"
- Multi-step assertions: "User should see confirmation after submit"

### The Rule

> **The problem is not WHERE assertions live, but WHAT they assert.**

## Naming Conventions

Use clear, intent-revealing method names:

```python
# Pattern A - Return Locators
get_*()           # Returns Locator object
get_*_text()      # Returns string from element
get_*_count()     # Returns integer
get_*_attribute() # Returns attribute value

# Pattern B - Enforce UI Invariants
ensure_*()        # Contains expect() for UI state
verify_*()        # Alternative to ensure_*()

# Actions
click_*()         # Clicks an element
fill_*()          # Fills an input
select_*()        # Selects from dropdown
```

## Design Patterns

### Page Navigation Pattern

Return new page objects when navigation occurs:

```python
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
    
    def login(self, username: str, password: str):
        """Login and return dashboard page"""
        self.page.get_by_label("Username").fill(username)
        self.page.get_by_label("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
        
        # Return next page object
        from pages.dashboard_page import DashboardPage
        return DashboardPage(self.page)

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
    
    def navigate_to_employees(self):
        """Navigate to employees page"""
        self.page.get_by_role("link", name="Employees").click()
        
        from pages.employee_list_page import EmployeeListPage
        return EmployeeListPage(self.page)
```

### Locator Chaining for Scoping

Chain locators to scope within specific sections:

```python
class EmployeeListPage:
    def __init__(self, page: Page):
        self.page = page
    
    def get_employee_email(self, employee_name: str) -> str:
        """Get email for specific employee"""
        # Chain locators to scope within row
        employee_row = (
            self.page
            .get_by_role("table")
            .get_by_role("row")
            .filter(has_text=employee_name)
        )
        return employee_row.locator("td.email").inner_text()
    
    def delete_employee(self, employee_name: str):
        """Delete specific employee"""
        employee_row = self.page.get_by_role("row").filter(has_text=employee_name)
        employee_row.get_by_role("button", name="Delete").click()
```

## Complete Example

```python
from playwright.sync_api import Page, Locator, expect

class EmployeeDetailsPage:
    def __init__(self, page: Page):
        self.page = page
    
    # Pattern B - Ensure methods for UI invariants
    def ensure_page_loaded(self):
        """Ensure employee details page loaded"""
        expect(self.page.get_by_role("heading", name="Employee Details")).to_be_visible()
    
    def ensure_save_successful(self):
        """Ensure save confirmation appears"""
        expect(self.page.get_by_role("alert")).to_contain_text("Successfully saved")
    
    # Pattern A - Return locators for flexible assertions
    def get_name_input(self) -> Locator:
        """Get name input field"""
        return self.page.get_by_label("Full Name")
    
    def get_email_input(self) -> Locator:
        """Get email input field"""
        return self.page.get_by_label("Email Address")
    
    # Actions
    def fill_name(self, name: str):
        """Fill employee name"""
        self.get_name_input().fill(name)
    
    def fill_email(self, email: str):
        """Fill employee email"""
        self.get_email_input().fill(email)
    
    def click_save(self):
        """Click save button"""
        self.page.get_by_role("button", name="Save").click()
    
    # Convenience method combining actions
    def save_employee(self, name: str, email: str):
        """Fill and save employee details"""
        self.fill_name(name)
        self.fill_email(email)
        self.click_save()
```

## Best Practices Summary

### DO:
- ✅ Use built-in locators (`get_by_role`, `get_by_label`, etc.)
- ✅ Initialize with `self.page` (no BasePage)
- ✅ Return Locators OR use ensure methods (both valid)
- ✅ Use properties for complex/reused locators only
- ✅ Return page objects after navigation
- ✅ Chain locators for scoping
- ✅ Use clear, descriptive method names

### DON'T:
- ❌ Use string constants for locators
- ❌ Create BasePage with wrapper methods
- ❌ Use CSS/XPath when built-in locators work
- ❌ Put business logic in page objects
- ❌ Use dynamic class names or brittle selectors
- ❌ Apply Selenium patterns to Playwright

## Related Documentation

- See [testing.instructions.md](testing.instructions.md) for test writing guidelines
- See [architecture.instructions.md](architecture.instructions.md) for project structure
- [Playwright Locators Documentation](https://playwright.dev/python/docs/locators)
- [Playwright Best Practices](https://playwright.dev/python/docs/best-practices)
