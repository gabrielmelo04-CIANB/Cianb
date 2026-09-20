# CLAUDE.md — AI Assistant Guide for Cianb

This file provides context and conventions for AI assistants (Claude and others) working in this repository.

---

## Repository Overview

**Project**: Cianb
**Repository**: gabrielmelo04-CIANB/Cianb
**Status**: Initial Streamlit app

This repository contains a simple Streamlit page (`app.py`). This CLAUDE.md will be updated as the project grows to reflect the actual codebase structure, conventions, and workflows.

### Running the app

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Current State

The repository has no source code yet. When content is added, this file should be updated to reflect:

- Technology stack and languages used
- Directory structure and module organization
- Development setup and prerequisites
- Build and test commands
- Code style and conventions

---

## Git Workflow

### Branching

- Feature branches follow the naming pattern: `claude/<feature-description>-<session-id>`
- The main integration branch is typically `main` or `master`
- Never push directly to the default branch without a pull request

### Commit Messages

Write clear, descriptive commit messages:
- Use the imperative mood: "Add feature" not "Added feature"
- Keep the subject line under 72 characters
- Reference related issues or PRs when relevant

### Push Process

Always push with tracking:
```bash
git push -u origin <branch-name>
```

If push fails due to network issues, retry with exponential backoff (2s, 4s, 8s, 16s).

---

## Development Conventions (To Be Updated)

Once source code is added, document the following here:

### Code Style

- [ ] Language(s) in use
- [ ] Formatter and linter configuration
- [ ] Indentation style (tabs vs spaces, width)
- [ ] Naming conventions (camelCase, snake_case, PascalCase per context)

### Directory Structure

```
(To be filled in once project structure is established)
```

### Build & Test

```bash
# Install dependencies
# (command TBD)

# Run tests
# (command TBD)

# Build project
# (command TBD)
```

### Environment Variables

Document required environment variables here once the project defines them.

---

## Guidelines for AI Assistants

When working in this repository, follow these principles:

### General

- Read existing files before modifying them
- Prefer editing existing files over creating new ones
- Keep changes minimal and focused on the stated task
- Do not add unrequested features, refactors, or improvements
- Avoid over-engineering — minimum complexity for the current task

### Security

- Never introduce command injection, XSS, SQL injection, or other OWASP Top 10 vulnerabilities
- Validate at system boundaries (user input, external APIs) but trust internal code
- Do not commit secrets, credentials, or API keys

### Git Operations

- Work on the designated feature branch (see branch naming above)
- Commit with clear, descriptive messages
- Push to the feature branch when work is complete
- Never force-push without explicit user permission
- Never skip hooks (`--no-verify`) without explicit user permission

### What to Update in This File

When adding new features or making architectural decisions, update CLAUDE.md to reflect:

- New directories or modules introduced
- New dependencies or tools added
- Changes to the build or test process
- Newly established conventions or patterns

---

## Updating This File

This CLAUDE.md should be treated as a living document. Any AI assistant or developer who makes significant structural changes to the project should update the relevant sections of this file as part of that work.

Last updated: 2026-03-22
