---
description: "Project structure and organization for HR Orange Automation - Modern Playwright Python framework"
applyTo: "**/*.py"
---

# HR Orange Automation - Architecture

## Project Purpose

Automated testing framework for HR Orange website using:
- **Python 3.14**: Modern Python with latest features
- **Playwright (sync API)**: Browser automation framework
- **pytest**: Testing framework
- **pipenv**: Dependency and virtual environment management

**IMPORTANT**: This framework uses **Playwright's sync API**, NOT async. No `async`/`await` keywords.

## Project Structure

```
hrm-orange-automation/
├── pages/                    # Page Object Models
│   ├── __init__.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── employee_list_page.py
├── tests/                    # Test files
│   ├── __init__.py
│   ├── conftest.py          # pytest fixtures and configuration
│   ├── test_login.py
│   └── test_employee_management.py
├── utils/                    # Utilities and helpers
│   ├── __init__.py
│   ├── config.py            # Configuration management
│   ├── helpers.py           # Helper functions
│   └── api_client.py        # API client for test data setup
├── data/                     # Test data
│   ├── __init__.py
│   ├── test_users.py
│   └── test_employees.py
├── Pipfile                   # Dependencies
├── Pipfile.lock
├── pytest.ini               # pytest configuration
└── README.md
```

## Directory Responsibilities

### `pages/`
Contains Page Object Model classes representing web pages or UI components.

**See**: [page-objects.instructions.md](page-objects.instructions.md) for detailed patterns and guidelines.

**Key Principles**:
- One class per page or major UI component
- Use Playwright's built-in locators (`get_by_role`, `get_by_label`, etc.)
- No BasePage inheritance (modern Playwright doesn't need it)
- Return Locators OR use ensure methods (both patterns valid)

### `tests/`
Contains test files using pytest framework.

**See**: [testing.instructions.md](testing.instructions.md) for detailed test writing guidelines.

**Key Principles**:
- One test file per feature or workflow
- Use `expect()` for UI assertions (NOT Python `assert`)
- Tests should be independent and idempotent
- Use fixtures for setup/teardown
- Use API for test data setup when possible

### `utils/`
Common utilities, configuration, and helpers.

#### Configuration Module (`utils/config.py`)

Centralized configuration management using environment variables:

```python
# utils/config.py
import os
from dataclasses import dataclass

@dataclass
class Config:
    BASE_URL: str = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com")
    HEADLESS: bool = os.getenv("HEADLESS", "true").lower() == "true"
    TIMEOUT: int = int(os.getenv("TIMEOUT", "30000"))
    BROWSER: str = os.getenv("BROWSER", "chromium")

config = Config()
```

**Usage in tests/pages**:
```python
from utils.config import config

page.goto(config.BASE_URL)
```

#### Helper Functions (`utils/helpers.py`)

Reusable utility functions:

```python
# utils/helpers.py
import json
import uuid

def load_test_data(file_path: str) -> dict:
    """Load test data from JSON file"""
    with open(file_path, 'r') as f:
        return json.load(f)

def generate_random_email() -> str:
    """Generate random email for testing"""
    return f"test_{uuid.uuid4()}@example.com"

def format_date(date_obj) -> str:
    """Format date for UI input"""
    return date_obj.strftime("%Y-%m-%d")
```

#### API Client (`utils/api_client.py`)

API client for test data setup (faster than UI):

```python
# utils/api_client.py
import requests
from utils.config import config

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
    
    def create_employee(self, name: str, email: str) -> str:
        """Create employee via API and return ID"""
        response = self.session.post(
            f"{self.base_url}/api/employees",
            json={"name": name, "email": email}
        )
        return response.json()["id"]
    
    def cleanup(self):
        """Cleanup resources"""
        self.session.close()
```

### `data/`
Test data files and constants.

```python
# data/test_users.py
ADMIN_USER = {
    "username": "admin",
    "password": "admin123"
}

ESS_USER = {
    "username": "ess_user",
    "password": "ess123"
}

# data/test_employees.py
VALID_EMPLOYEE = {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com"
}
```

## pytest Configuration

### `conftest.py`

Shared fixtures for all tests:

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

### `pytest.ini`

pytest configuration:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
markers =
    smoke: Quick smoke tests
    regression: Full regression suite
    slow: Tests that take longer to run
```

## Design Patterns

### Page Navigation Pattern

Page objects return new page instances when navigation occurs:

```python
# pages/login_page.py
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
    
    def login(self, username: str, password: str):
        """Login and return dashboard page"""
        self.page.get_by_label("Username").fill(username)
        self.page.get_by_label("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
        
        from pages.dashboard_page import DashboardPage
        return DashboardPage(self.page)
```

### Separation of Concerns

- **Page Objects**: Handle UI interactions and locators
- **Tests**: Focus on business logic and scenarios
- **Fixtures**: Manage setup/teardown and test dependencies
- **Config**: Centralize environment-specific settings
- **Helpers**: Provide reusable utilities
- **Data**: Store test data separately from logic

### No BasePage Needed

**Modern Playwright doesn't need a BasePage class.** Instead:

- **Configuration**: Use `utils/config.py` for shared settings
- **Helper Functions**: Use `utils/helpers.py` for common operations
- **Fixtures**: Use pytest fixtures for setup/teardown
- **Direct Page Access**: Page objects access `self.page` directly

**Why no BasePage?**
- Playwright's API is already clean and powerful
- Adding wrapper methods creates unnecessary abstraction
- Fixtures provide better composition than inheritance
- Less code to maintain

## Core Principles

### 1. Modern Playwright Approach

This is **NOT Selenium**. Key differences:

| Selenium (Old) | Playwright (Modern) |
|----------------|---------------------|
| WebElement objects | Locators (lazy) |
| Explicit waits needed | Auto-waiting built-in |
| BasePage with wrappers | Direct `page` usage |
| String locator constants | Built-in locator methods |
| `assert element.is_visible()` | `expect(locator).to_be_visible()` |

### 2. Test Independence

- Each test should set up its own state
- No dependencies between tests
- Use fixtures for common setup
- Use API for fast test data creation

### 3. Performance

- Use API for test data setup (faster than UI)
- Only test UI workflows through the UI
- Keep tests focused and fast
- Use `authenticated_page` fixture to skip login when not testing it

### 4. Maintainability

- One responsibility per file/class
- Clear naming conventions
- Centralized configuration
- Reusable fixtures and helpers

## File Naming Conventions

```
pages/              # Page objects: {page_name}_page.py
  login_page.py
  dashboard_page.py
  
tests/              # Tests: test_{feature}.py
  test_login.py
  test_employee_management.py
  
utils/              # Utilities: {purpose}.py
  config.py
  helpers.py
  api_client.py
  
data/               # Data: test_{entity}.py
  test_users.py
  test_employees.py
```

## Related Documentation

- **[page-objects.instructions.md](page-objects.instructions.md)**: How to write page objects
  - Locator strategies (built-in methods, properties, never constants)
  - Page object patterns (return locators vs ensure methods)
  - Naming conventions and best practices
  
- **[testing.instructions.md](testing.instructions.md)**: How to write tests
  - Assertions strategy (`expect()` vs `assert`)
  - Test structure and fixtures
  - Testing best practices

## Quick Start

1. **Install dependencies**: `pipenv install`
2. **Activate environment**: `pipenv shell`
3. **Run tests**: `pytest`
4. **Run specific test**: `pytest tests/test_login.py`
5. **Run with markers**: `pytest -m smoke`

## References

- [Playwright Python Documentation](https://playwright.dev/python/)
- [pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://martinfowler.com/bliki/PageObject.html)

## Resources

- [Playwright Python Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://martinfowler.com/bliki/PageObject.html)
