# Copilot Instructions for Darliewithrow/master Repository

## Repository Purpose

This repository serves as a guide for contributors who encounter the "Uploads are disabled" error when trying to contribute to the Ethereum EIPs repository. It provides step-by-step instructions for the proper GitHub workflow: forking, cloning, creating branches, making changes, and submitting pull requests.

## Repository Structure

```
.
├── README.md                    # Main guide for contributing to Ethereum EIPs
├── CONTRIBUTING.md              # Contribution guidelines for this repository
├── LICENSE                      # MIT License
├── copilot-instructions.md      # Root-level Copilot instructions reference
└── .github/
    ├── copilot-instructions.md  # This file — repository-wide Copilot instructions
    ├── agents/                  # Custom agent configurations
    ├── instructions/            # Coding guidelines for specific file patterns
    └── workflows/               # GitHub Actions workflows
```

## Coding Standards and Conventions

### Markdown Style
- Use clear, concise language
- Follow standard Markdown formatting
- Use code blocks with language identifiers for syntax highlighting
- Include descriptive headings and subheadings
- Use bullet points and numbered lists for step-by-step instructions

### Documentation Guidelines
- Write for beginners who may be unfamiliar with GitHub workflows
- Include explanations for why certain steps are necessary
- Provide complete examples with placeholders (e.g., `YOUR-USERNAME`)
- Link to official documentation for deeper dives
- Keep instructions up-to-date with current GitHub UI and terminology

### Content Organization
- Start with the problem/context
- Provide clear step-by-step solutions
- Include troubleshooting tips where relevant
- End with additional resources and help channels

## Contributing to This Repository

### Types of Contributions Welcome
- Improvements to clarity and readability
- Updates to reflect GitHub UI changes
- Additional examples or use cases
- Fixing typos or broken links
- Adding new sections for common questions

### Making Changes
1. Fork this repository
2. Create a feature branch from `main`
3. Make your changes to the documentation
4. Ensure all links are working
5. Verify Markdown formatting is correct
6. Submit a pull request with a clear description

## Build and Test Instructions

This repository contains only Markdown documentation, so there are no build steps. However, you should:

### Validation Steps
1. **Check Markdown syntax**: Ensure all Markdown is properly formatted
2. **Verify links**: Test that all URLs are valid and accessible
3. **Review formatting**: Preview the rendered Markdown to ensure it displays correctly
4. **Proofread**: Check for spelling and grammar errors

## Project-Specific Guidelines

### Audience Awareness
- Target audience: Developers new to contributing to open-source projects
- Assume basic familiarity with Git but explain GitHub-specific workflows
- Use inclusive language and avoid jargon without explanation

### Link Maintenance
- Use persistent links (not subject to URL changes)
- Prefer official documentation over third-party sources
- Include the Ethereum community resources that are actively maintained

### Scope
- This is a guide repository, not the actual EIPs repository
- Keep focus on the contribution workflow
- Direct users to ethereum/EIPs for actual EIP submissions

## Quality Standards

When making changes:
- Ensure accuracy of technical information
- Maintain consistency with existing writing style
- Keep instructions sequential and easy to follow
- Test any code snippets or commands provided
- Consider the user experience of someone following the guide
