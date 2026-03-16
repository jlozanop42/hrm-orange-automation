# HR Orange Automation Framework

A modern test automation framework for Human Resources Management workflows using Python 3.14 and Playwright.

## Tech Stack

- **Python**: 3.14
- **Test Framework**: Playwright for Python
- **Package Manager**: pipenv
- **Test Runner**: pytest

## Project Structure

```
hrm-orange-automation/
├── pages/              # Page Object Models
├── tests/              # Test files
├── utils/              # Utility functions and helpers
├── data/               # Test data files
└── pages-description/  # Page structure documentation
```

## Getting Started

### Prerequisites

- Python 3.14+
- pipenv

### Installation

```bash
# Install dependencies
pipenv install

# Install Playwright browsers
pipenv run playwright install
```

### Running Tests

```bash
# Run all tests
pipenv run pytest

# Run specific test file
pipenv run pytest tests/test_login.py

# Run with headed browser
pipenv run pytest --headed

# Run with specific browser
pipenv run pytest --browser firefox
```

## Development

### AI-Assisted Development

This project uses GitHub Copilot with custom agents and instruction files to maintain consistency:

- **Custom Agents**: `@generate-instructions-file`, `@page-documenter`
- **Instruction Files**: Located in `.github/instructions/` - guide AI agents on tech stack, architecture, testing rules, and page objects
- **See**: [.github/copilot-instructions.md](.github/copilot-instructions.md) for details

### Contributing

When contributing to this project:

1. Review instruction files in `.github/instructions/` for coding standards
2. Follow the Page Object Model pattern for new pages
3. Write tests following the conventions in `testing.instructions.md`
4. Ensure all tests pass before submitting

## Documentation

- **AI Instructions**: [.github/copilot-instructions.md](.github/copilot-instructions.md)
- **Architecture Guide**: [.github/instructions/architecture.instructions.md](.github/instructions/architecture.instructions.md)
- **Testing Standards**: [.github/instructions/testing.instructions.md](.github/instructions/testing.instructions.md)
- **Page Objects Guide**: [.github/instructions/page-objects.instructions.md](.github/instructions/page-objects.instructions.md)
- **Tech Stack Details**: [.github/instructions/tech-stack.instructions.md](.github/instructions/tech-stack.instructions.md)
