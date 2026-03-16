---
description: "Test writing guidelines and best practices for HR Orange Automation - Modern Playwright testing approach"
applyTo: "tests/**/*.py"
---

# Testing Guidelines

## Overview

This document defines how to write tests using modern Playwright patterns with pytest. **This is NOT Selenium** - assertions and synchronization work fundamentally differently.

## Core Principles

- **ALWAYS use `expect()` for UI assertions** (not Python `assert`)
- Tests should be independent and idempotent
- One test file per feature or page
- Use fixtures for setup/teardown
- Focus on business logic; let page objects handle UI details

## Assertions Strategy

### CRITICAL: `expect()` vs `assert`

**Playwright `expect()` is fundamentally different from Selenium/Python assertions.**

| Feature | Playwright `expect()` | Python `assert` |
|---------|---------------------|----------------|
| Auto-waiting | ✅ Yes | ❌ No |
| Retrying | ✅ Until timeout | ❌ Immediate |
| Synchronization | ✅ Built-in | ❌ Manual |
| Diagnostics | ✅ Rich error messages | ❌ Basic |
| Flakiness | ✅ Resistant | ❌ High risk |

**ALWAYS use `expect()` for UI state checks.**

```python
from playwright.sync_api import expect

# ✅ CORRECT - Use expect()
expect(page.get_by_role("heading")).to_have_text("Dashboard")
expect(page).to_have_url(/.*\/dashboard/)
expect(login_page.get_error_locator()).to_be_visible()

# ❌ WRONG - Don't use assert for UI
assert page.url.endswith("/dashboard")  # Flaky - no auto-wait
assert element.is_visible()  # Flaky - immediate check
```

### When to Use Python `assert`

Use Python `assert` ONLY for:
- Pure Python business logic calculations
- Data transformations (non-UI data)
- API response validations
- Test setup validation

**Key Rule: If data comes from the DOM/UI, use `expect()` instead.**

```python
# ✅ CORRECT - Pure business logic (no UI)
total = calculate_order_total(items)  # Pure Python function
assert total == 150.00

discount = apply_discount(100, 0.1)
assert discount == 90.00

# ✅ CORRECT - API/test data validation (no UI)
api_response = api_client.get_order(order_id)
assert api_response['status'] == 'completed'

# ❌ WRONG - Data extracted from UI should use expect()
order_count = orders_page.get_order_count()  # Gets count from DOM
assert order_count == 5  # Should use expect() instead

# ✅ CORRECT - UI-derived data
expect(page.locator('.order-row')).to_have_count(5)
```

## Test Structure

### File Naming Convention

- **Pattern**: `test_*.py`
- **Descriptive names**: `test_employee_management.py`, not `test_emp.py`
- **Group by feature**: One feature or workflow per file

### Test Function Naming

```python
# ✅ GOOD - Descriptive, explains scenario
def test_successful_login_redirects_to_dashboard(page):
    ...

def test_invalid_credentials_show_error_message(page):
    ...

def test_employee_creation_with_all_required_fields(page):
    ...

# ❌ BAD - Vague, unclear
def test_login(page):
    ...

def test_error(page):
    ...
```

### AAA Pattern (Arrange, Act, Assert)

Structure tests clearly:

```python
from playwright.sync_api import expect
from pages.login_page import LoginPage
from data.test_users import ADMIN_USER
from utils.config import config

def test_successful_login_shows_welcome_message(page):
    # ARRANGE - Set up test data and navigate
    page.goto(config.BASE_URL)
    login_page = LoginPage(page)
    
    # ACT - Perform the action
    dashboard = login_page.login(ADMIN_USER['username'], ADMIN_USER['password'])
    
    # ASSERT - Verify outcome
    expect(page).to_have_url(/.*dashboard/)
    expect(dashboard.get_welcome_heading()).to_be_visible()
```

## Two Valid Testing Patterns

### Pattern A: Return Locators (Explicit Control)

Tests have full control over assertions:

```python
from playwright.sync_api import expect
from pages.orders_page import OrdersPage
from utils.config import config

def test_order_displays_correct_product_name(page, api_client):
    # Arrange
    order_id = api_client.create_order("Product A")
    page.goto(f"{config.BASE_URL}/orders")
    orders_page = OrdersPage(page)
    
    # Act & Assert
    expect(orders_page.get_order_row(order_id)).to_be_visible()
    expect(orders_page.get_order_name_cell(order_id)).to_have_text("Product A")
```

**Characteristics**:
- ✅ Test controls all assertions
- ✅ Clear what's being validated
- ✅ Familiar pattern

### Pattern B: Ensure Methods (Reduced Boilerplate)

Page objects handle UI invariants:

```python
from playwright.sync_api import expect
from pages.orders_page import OrdersPage
from utils.config import config

def test_order_appears_after_creation(page, api_client):
    # Arrange
    order_id = api_client.create_order("Product A")
    page.goto(f"{config.BASE_URL}/orders")
    orders_page = OrdersPage(page)
    
    # Act & Assert
    orders_page.ensure_page_loaded()  # UI invariant
    orders_page.ensure_order_is_visible(order_id)  # UI invariant
    
    # UI state assertion (count from DOM)
    expect(orders_page.get_order_rows()).to_have_count(1)
```

**Characteristics**:
- ✅ Less boilerplate
- ✅ Strong synchronization
- ✅ Clear test intent

**Both patterns are valid. Choose based on context.**

## Fixtures

### Basic Fixtures (conftest.py)

```python
# tests/conftest.py
import pytest
from playwright.sync_api import sync_playwright
from utils.config import config

@pytest.fixture(scope="function")
def browser():
    """Provide browser instance"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=config.HEADLESS)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """Provide page instance"""
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080}
    )
    page = context.new_page()
    yield page
    context.close()
```

### Custom Fixtures

```python
@pytest.fixture(scope="function")
def authenticated_page(page):
    """Provide pre-authenticated page"""
    from pages.login_page import LoginPage
    from data.test_users import ADMIN_USER
    
    page.goto(config.BASE_URL)
    login_page = LoginPage(page)
    login_page.login(ADMIN_USER['username'], ADMIN_USER['password'])
    
    yield page

@pytest.fixture(scope="function")
def api_client():
    """Provide API client for test data setup"""
    from utils.api_client import APIClient
    client = APIClient(config.API_BASE_URL)
    yield client
    client.cleanup()
```

### Using Fixtures

```python
def test_employee_list_loads(authenticated_page):
    """Test uses authenticated_page fixture"""
    from playwright.sync_api import expect
    from pages.employee_list_page import EmployeeListPage
    
    authenticated_page.goto(f"{config.BASE_URL}/employees")
    employee_page = EmployeeListPage(authenticated_page)
    
    employee_page.ensure_page_loaded()
    expect(employee_page.get_employee_rows()).to_have_count_greater_than(0)
```

## Common Assertions

### Page/URL Assertions

```python
# URL matching
expect(page).to_have_url("https://example.com/dashboard")
expect(page).to_have_url(/.*dashboard/)  # Regex

# Title
expect(page).to_have_title("Dashboard - HR Orange")
expect(page).to_have_title(/.*Dashboard/)
```

### Element Assertions

```python
# Visibility
expect(locator).to_be_visible()
expect(locator).to_be_hidden()

# Text content
expect(locator).to_have_text("Expected text")
expect(locator).to_have_text(/pattern/)
expect(locator).to_contain_text("partial")

# Attributes
expect(locator).to_have_attribute("href", "/dashboard")
expect(locator).to_have_class("active")

# State
expect(locator).to_be_enabled()
expect(locator).to_be_disabled()
expect(locator).to_be_checked()
expect(locator).to_be_editable()

# Count
expect(locator).to_have_count(5)
```

### Negative Assertions

```python
# Use 'not_' variants
expect(locator).not_to_be_visible()
expect(locator).not_to_have_text("Wrong text")
expect(page).not_to_have_url("/login")
```

## Test Independence

### ✅ DO: Independent Tests

Each test should set up its own state:

```python
def test_create_employee(page, api_client):
    # This test doesn't depend on any other test
    page.goto(f"{config.BASE_URL}/employees/new")
    employee_page = EmployeeNewPage(page)
    
    employee_page.fill_form("John Doe", "john@example.com")
    employee_page.click_save()
    
    expect(page.get_by_role("alert")).to_contain_text("Successfully created")
```

### ❌ DON'T: Dependent Tests

```python
# ❌ WRONG - Test depends on previous test
employee_id = None

def test_create_employee(page):
    global employee_id
    # Create employee
    employee_id = ...  # Bad - side effect

def test_edit_employee(page):
    global employee_id
    # Edit the employee from previous test - FLAKY!
    ...
```

## Data-Driven Tests

Use pytest parametrize for multiple scenarios:

```python
import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize("username,password,expected_error", [
    ("", "", "Username is required"),
    ("admin", "", "Password is required"),
    ("invalid", "wrong", "Invalid credentials"),
])
def test_login_validation_errors(page, username, password, expected_error):
    page.goto(config.BASE_URL)
    login_page = LoginPage(page)
    
    login_page.login(username, password)
    
    expect(login_page.get_error_locator()).to_have_text(expected_error)
```

## Setup Best Practices

### Use API for Setup, UI for Verification

```python
def test_employee_appears_in_list(page, api_client):
    # ARRANGE - Use API for fast setup
    employee_id = api_client.create_employee("John Doe", "john@example.com")
    
    # ACT - Use UI for verification
    page.goto(f"{config.BASE_URL}/employees")
    employee_page = EmployeeListPage(page)
    
    # ASSERT - UI state
    expect(employee_page.get_employee_row(employee_id)).to_be_visible()
```

### Avoid UI Setup When Possible

```python
# ❌ SLOW - Using UI for setup
def test_slow_employee_edit(page):
    # Don't navigate through UI to create employee
    page.goto(f"{config.BASE_URL}/employees/new")
    # Fill many forms...
    # Click save...
    # Then test edit functionality...

# ✅ FAST - Use API for setup
def test_fast_employee_edit(page, api_client):
    # Use API to create employee quickly
    employee_id = api_client.create_employee("John Doe", "john@example.com")
    
    # Test only what matters - the edit functionality
    page.goto(f"{config.BASE_URL}/employees/{employee_id}/edit")
    # Test edit...
```

## Error Handling

### Test Failures Should Be Clear

```python
def test_employee_creation_with_clear_failure(page):
    page.goto(f"{config.BASE_URL}/employees/new")
    employee_page = EmployeeNewPage(page)
    
    employee_page.fill_name("John Doe")
    employee_page.fill_email("john@example.com")
    employee_page.click_save()
    
    # Clear assertion - failure message will show what text was found
    expect(page.get_by_role("alert")).to_have_text(
        "Employee successfully created"
    )
```

## Best Practices Summary

### DO:
- ✅ **ALWAYS use `expect()` for UI assertions**
- ✅ Use Python `assert` only for business logic/calculations
- ✅ Keep tests independent and idempotent
- ✅ Use AAA pattern (Arrange, Act, Assert)
- ✅ Use descriptive test names
- ✅ Use fixtures for setup/teardown
- ✅ Use API for test data setup when possible
- ✅ Parametrize tests for multiple scenarios
- ✅ Make assertions explicit and clear

### DON'T:
- ❌ **Use Python `assert` for UI state** (use `expect()`)
- ❌ Use `time.sleep()` - if needed, you're missing an assertion
- ❌ Create inter-dependent tests
- ❌ Use UI for test data setup (use API)
- ❌ Hardcode URLs or credentials
- ❌ Share state between tests
- ❌ Swallow failures with try/except
- ❌ Test multiple unrelated scenarios in one test

## Playwright vs Selenium Mindset

**Remember: This is NOT Selenium!**

| Selenium (Old) | Playwright (Modern) |
|---------------|---------------------|
| Assertions are passive | Assertions are active (auto-wait) |
| Manual waits needed | Auto-waiting built-in |
| `assert element.is_visible()` | `expect(locator).to_be_visible()` |
| `WebDriverWait` patterns | Just use `expect()` |
| Flakiness = add more waits | Flakiness = missing assertion |

### Rule of Thumb

> **If you feel the need to add a `sleep()`, you're missing a Playwright assertion.**

## Complete Example

```python
# tests/test_employee_management.py
import pytest
from playwright.sync_api import expect
from pages.employee_list_page import EmployeeListPage
from pages.employee_new_page import EmployeeNewPage
from data.test_users import ADMIN_USER
from utils.config import config

@pytest.fixture(scope="function")
def employee_page(authenticated_page):
    """Navigate to employee list page"""
    authenticated_page.goto(f"{config.BASE_URL}/employees")
    return EmployeeListPage(authenticated_page)

def test_create_new_employee_successfully(authenticated_page):
    """Test creating a new employee with valid data"""
    # Arrange
    authenticated_page.goto(f"{config.BASE_URL}/employees/new")
    new_employee_page = EmployeeNewPage(authenticated_page)
    
    # Act
    new_employee_page.fill_name("John Doe")
    new_employee_page.fill_email("john.doe@example.com")
    new_employee_page.fill_department("Engineering")
    employee_list = new_employee_page.click_save()
    
    # Assert
    expect(authenticated_page.get_by_role("alert")).to_contain_text("Successfully created")
    employee_list.ensure_employee_visible("John Doe")

def test_empty_name_shows_validation_error(authenticated_page):
    """Test that empty name field shows validation error"""
    # Arrange
    authenticated_page.goto(f"{config.BASE_URL}/employees/new")
    new_employee_page = EmployeeNewPage(authenticated_page)
    
    # Act
    new_employee_page.fill_email("john.doe@example.com")
    new_employee_page.click_save()
    
    # Assert
    expect(new_employee_page.get_name_error()).to_have_text("Name is required")

@pytest.mark.parametrize("department", ["Engineering", "HR", "Sales"])
def test_employee_can_be_assigned_to_departments(authenticated_page, department, api_client):
    """Test employee creation for different departments"""
    # Arrange - Use API for setup
    employee_id = api_client.create_employee("Test User", f"test@{department.lower()}.com")
    
    # Act
    authenticated_page.goto(f"{config.BASE_URL}/employees/{employee_id}/edit")
    edit_page = EmployeeEditPage(authenticated_page)
    edit_page.select_department(department)
    edit_page.click_save()
    
    # Assert
    expect(authenticated_page.get_by_role("alert")).to_contain_text("Successfully updated")
```

## Related Documentation

- See [page-objects.instructions.md](page-objects.instructions.md) for page object guidelines
- See [architecture.instructions.md](architecture.instructions.md) for project structure
- [Playwright Assertions](https://playwright.dev/python/docs/test-assertions)
- [Pytest Documentation](https://docs.pytest.org/)
