# HR Orange Automation Framework

## Project Overview

This is an automation framework for testing a Human Resources Management website. The framework enables automated testing of HR workflows, user interactions, and business processes.

## Purpose

When working on this project, AI agents should understand:
- This is a test automation framework for an HR system
- Focus on maintainable, scalable test automation patterns
- Follow best practices for UI automation and API testing
- Ensure tests are reliable, fast, and easy to debug

## Quick Start Guide for AI Agents

1. **Before making changes**: Review relevant instruction files in `.github/instructions/`
2. **When adding features**: Follow the architecture patterns defined for this framework
3. **When writing tests**: Adhere to the testing standards and naming conventions
4. **When fixing bugs**: Check existing patterns before introducing new approaches

## Instruction Files

The following instruction files are available in `.github/instructions/`:

### Active Instructions
- **[Tech Stack](../.github/instructions/tech-stack.instructions.md)**: Technologies, frameworks, and dependencies used (Python 3.14, Playwright, pipenv)
- **[Architecture](../.github/instructions/architecture.instructions.md)**: Framework structure, design patterns, and organization
- **[Testing Rules](../.github/instructions/testing.instructions.md)**: Test writing standards, naming conventions, assertions
- **[Page Objects](../.github/instructions/page-objects.instructions.md)**: Page Object Model patterns and best practices

### Future Instructions (To Be Created)
- **API Testing**: API automation patterns and utilities
- **CI/CD**: Continuous integration and deployment guidelines
- **Data Management**: Test data strategies and fixtures

Use `@generate-instructions-file` to create additional instruction files as needed.

## Developer Background & Learning Preferences

**Experience Level:**
- New to Python and Playwright
- Experienced with automation testing using Selenium
- Familiar with test automation concepts and patterns

**Code Generation Guidelines:**
When generating or modifying Python code, ALWAYS provide:
1. **Python Concepts Explanation**: Brief explanation of any new Python-specific concepts, syntax, or patterns used (e.g., decorators, context managers, list comprehensions, type hints)
2. **Playwright Concepts Explanation**: Brief explanation of Playwright-specific features or patterns used (e.g., auto-waiting, locator strategies, page fixtures)
3. **Selenium vs Playwright**: When relevant, highlight key differences from Selenium approach

Keep explanations concise but clear, focusing on practical understanding.

**Automatic Documentation:**
After generating or modifying Python/Playwright code that introduces new concepts (decorators, type hints, Playwright locator strategies, fixtures, etc.), automatically invoke the `@create-python-doc` subagent to create simple reference documentation. Pass the generated code and any new concepts used as context. This helps build a knowledge base over time for developers learning Python and Playwright.

## Custom Agents

The framework includes specialized agents for specific workflows:

- **@page-documenter**: Creates structured markdown documentation for web pages based on natural language descriptions. Use when you need to document page layouts and components before creating page objects.

- **@create-python-doc**: Creates simple, beginner-friendly documentation for Python and Playwright concepts used in generated code. Automatically invoked after generating new Python/Playwright code to explain new concepts with practical examples.

- **@test-case-generator**: Generates comprehensive test case documentation organized by category folders (positive/, negative/, edge/, ui-ux/). Groups similar scenarios into single test case files. Creates structured markdown in test-cases/[feature]/[category]/[test-case-name].md with an overview.md index file.

## Getting Help

- Use `@generate-instructions-file` to create new instruction files
- Use `@page-documenter` to document page structures
- Use `@test-case-generator` to create comprehensive test case documentation
- Instruction files will be stored in `.github/instructions/`
- Page documentation will be stored in `/pages-description/`
- Test case documentation will be organized in `test-cases/[feature]/[category]/` with category folders (positive/, negative/, edge/, ui-ux/)
- Each test case file groups similar scenarios together
- Each feature includes an `overview.md` index file
- Each file applies to specific file patterns using the `applyTo` frontmatter

## Notes

This is a living document. As the framework evolves, update instruction files to reflect current practices and decisions.
