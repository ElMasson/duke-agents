# Changelog

All notable changes to DUKE Agents will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive documentation in README.md
- Detailed CONTRIBUTING.md guide for contributors
- CHANGELOG.md for tracking version history

### Changed
- Enhanced README with more examples and advanced usage
- Updated project URLs in pyproject.toml

## [1.0.0] - 2024-01-15

### Added
- Initial release of DUKE Agents framework
- IPO (Input-Process-Output) architecture implementation
- AtomicAgent for discrete task execution
- CodeActAgent for code generation and execution
- Mistral AI integration with support for all models
- WorkflowMemory system with feedback loops
- Orchestrator for linear and LLM-driven workflows
- Context management and propagation
- Auto-retry mechanism with satisfaction scoring
- Sandboxed code execution option
- Full type safety with Pydantic models
- Comprehensive test suite
- Example scripts for common use cases
- Development tools configuration (black, flake8, mypy)

### Features
- Memory persistence across workflow steps
- Configurable retry logic and thresholds
- Extensible agent architecture
- Rich error handling and logging
- Environment-based configuration
- Support for .env files

### Security
- Sandboxed execution environment for generated code
- Input validation on all agent inputs
- Secure API key handling

### Documentation
- Complete API documentation
- Usage examples
- Architecture overview
- Development setup guide

[Unreleased]: https://github.com/elmasson/duke-agents/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/elmasson/duke-agents/releases/tag/v1.0.0