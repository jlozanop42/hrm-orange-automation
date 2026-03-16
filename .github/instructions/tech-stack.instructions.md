---
description: "Tech stack and dependencies for HR Orange Automation - Python 3.14, Playwright, and pipenv"
applyTo:
  - "**/*.py"
  - "**/Pipfile"
  - "**/Pipfile.lock"
  - "**/playwright.config.*"
  - "**/pyproject.toml"
---

# Tech Stack

## Overview

This project uses Python with Playwright for automated testing of a Human Resources Management website. Dependencies are managed through pipenv to ensure consistent environments across development and CI/CD.

## Core Technologies

### Python 3.14
- **Role**: Primary programming language for all automation code
- **Why**: Modern Python version with latest language features and performance improvements
- **Usage**: All test scripts, page objects, utilities, and helpers

### Playwright
- **Role**: UI automation framework for browser testing
- **Why**: Modern, fast, and reliable browser automation with excellent API
- **Features**:
  - Cross-browser support (Chromium, Firefox, WebKit)
  - Auto-waiting for elements
  - Network interception capabilities
  - Excellent debugging tools
  - Built-in screenshot and video recording
- **Usage**: All UI interactions, element locating, and browser control

### pipenv
- **Role**: Dependency and virtual environment management
- **Why**: Combines pip and virtualenv for simplified dependency management
- **Features**:
  - Automatic virtualenv creation
  - Dependency locking for reproducible builds
  - Separate dev and production dependencies
  - Security vulnerability scanning

## Installation & Setup

### Initial Setup
```bash
# Install dependencies and create virtual environment
pipenv install

# Install dev dependencies (if needed)
pipenv install --dev

# Activate virtual environment
pipenv shell
```

### Installing Playwright Browsers
```bash
# Install Playwright browser binaries (run after pipenv install)
pipenv run playwright install

# Or if already in pipenv shell
playwright install
```

### Adding Dependencies
```bash
# Add a production dependency
pipenv install package-name

# Add a development dependency (e.g., testing tools)
pipenv install --dev package-name
```

## Best Practices

### Python Code Standards
- Use Python 3.14 features and syntax
- Follow PEP 8 style guidelines
- Use type hints where appropriate for better code clarity
- Leverage modern Python features (pattern matching, structural pattern matching, etc.)

### Playwright Usage
- Use Playwright's sync API consistently throughout the project
- Leverage auto-waiting - avoid manual `sleep()` statements
- Use meaningful locators (preferably test IDs or accessibility selectors)
- Take advantage of Playwright's built-in assertions
- Use page object model to organize UI interactions

### Dependency Management
- Always use `pipenv install` to add dependencies (not pip directly)
- Commit both `Pipfile` and `Pipfile.lock` to version control
- Run `pipenv update` periodically to keep dependencies current
- Use `pipenv check` to scan for security vulnerabilities

## Common Commands

```bash
# Run tests (example)
pipenv run pytest

# Check for dependency vulnerabilities
pipenv check

# Update dependencies
pipenv update

# Show dependency graph
pipenv graph

# Exit virtual environment
exit
```

## Rules for AI Agents

### DO:
- Use Python 3.14 syntax and features
- Use Playwright for all browser automation
- Manage dependencies through pipenv
- Leverage Playwright's auto-waiting mechanisms
- Use async/await patterns when using Playwright's async API
- Reference official Playwright documentation for API usage

### DON'T:
- Use outdated Python syntax or deprecated features
- Mix Selenium or other automation frameworks with Playwright
- Install packages with pip directly (always use pipenv)
- Add unnecessary dependencies
- Use `time.sleep()` for waiting (use Playwright's built-in waits)

## Resources

- [Python 3.14 Documentation](https://docs.python.org/3.14/)
- [Playwright Python Documentation](https://playwright.dev/python/)
- [pipenv Documentation](https://pipenv.pypa.io/)
- [Playwright Best Practices](https://playwright.dev/python/docs/best-practices)

## Notes

- User is currently learning Playwright and Python - provide clear explanations and examples
- CI/CD integration (GitHub Actions) will be added in the future
- This framework is specifically designed for HR website automation testing
