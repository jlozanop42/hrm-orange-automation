# HR Orange Automation Framework

An automation framework for testing Human Resources Management workflows.

## Project Setup

This project includes custom AI agents and instruction files to help guide development and maintain consistency.

## Using the Custom Agent

### `@generate-instructions-file` Agent

This custom agent helps you create instruction files to document your framework's conventions, tech stack, architecture, and rules.

**How to use it:**

1. In GitHub Copilot Chat, type: `@generate-instructions-file`
2. Specify what you want to document (e.g., "architecture patterns", "testing rules", "API testing guidelines")
3. Answer any questions the agent asks
4. The agent will create a properly formatted `.instructions.md` file in `.github/instructions/`

**Example:**
```
@generate-instructions-file Create an instruction file for Page Object Model patterns
```

## Instruction Files

Instruction files are stored in `.github/instructions/` and automatically guide AI agents when working on specific parts of your codebase.

### Current Instruction Files

- **tech-stack.instructions.md**: Tech stack and dependencies (template - fill in your specific details)

### Suggested Instruction Files to Create

Use `@generate-instructions-file` to create these:

1. **architecture.instructions.md**: Framework structure and design patterns
2. **testing-rules.instructions.md**: Test writing standards and conventions
3. **page-objects.instructions.md**: Page Object Model best practices
4. **api-testing.instructions.md**: API automation patterns
5. **ci-cd.instructions.md**: CI/CD pipeline and deployment
6. **data-management.instructions.md**: Test data management strategies

## Getting Started

1. **Fill in tech stack details**: Edit `.github/instructions/tech-stack.instructions.md` with your actual technologies
2. **Create additional instruction files**: Use `@generate-instructions-file` for each area of your framework
3. **Set up your framework**: Add your actual automation code, tests, and configuration
4. **Iterate**: Update instruction files as your framework evolves

## Documentation

- Main instructions: [.github/copilot-instructions.md](.github/copilot-instructions.md)
- Custom agents: [.github/agents/](.github/agents/)
- Instruction files: [.github/instructions/](.github/instructions/)

## Need Help?

Ask GitHub Copilot Chat or use `@generate-instructions-file` to create more guidance documents.
