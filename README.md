# EHR Agent

An intelligent browser automation agent for Electronic Health Record (EHR) systems using Playwright and Claude Code.

## Features

- **Browser Automation**: Automate web interactions with EHR systems using Playwright
- **Claude Integration**: Leverage Claude's AI capabilities for intelligent decision-making
- **Headless Operation**: Run browser automation in headless mode for CI/CD environments

## Usage

### Local Development

The agent provides browser automation tools that can be used to navigate and interact with EHR systems:

```python
from ehr_agent.tools import navigate

# Navigate to a URL and get the page title
title = navigate("https://example-ehr-system.com")
print(f"Page title: {title}")
```

### Available Tools

- `navigate(url: str) -> str`: Opens a URL in headless Chromium and returns the page title

### CI/CD Integration

When you create or update a pull request, Claude will automatically:

1. **Analyze your changes** using the registered tools
2. **Run browser automation tests** if applicable  
3. **Comment on the PR** with insights and suggestions

The workflow requires the `CLAUDE_API_KEY` secret to be configured in your repository settings.

## Installation

```bash
# Clone the repository
git clone https://github.com/DanielVelaJ/ehr-agent.git
cd ehr-agent

# Install dependencies
poetry install

# Install Playwright browsers
poetry run playwright install chromium
```

## Development

```bash
# Run the agent locally
poetry run python -m ehr_agent

# Run tests
poetry run pytest

# Format code
poetry run black .
```

## Requirements

- Python 3.12+
- Poetry for dependency management
- Playwright for browser automation
- Claude Code SDK for AI integration

## License

MIT License