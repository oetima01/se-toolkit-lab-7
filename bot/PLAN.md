# Bot Development Plan

This document describes the approach for building the LMS Telegram bot across four tasks.

## Architecture Overview

The bot follows a **layered architecture** with clear separation of concerns:

1. **Entry Point (`bot.py`)** — Handles Telegram updates or `--test` mode CLI input
2. **Handlers (`handlers/`)** — Pure functions that process commands and return text
3. **Services (`services/`)** — External API clients (LMS backend, LLM)
4. **Configuration (`config.py`)** — Environment variable loading with pydantic-settings

This design enables **testable handlers**: the same handler functions work from `--test` mode, unit tests, or Telegram without modification.

## Task 1: Scaffold (Current)

Create the project structure with placeholder handlers. Key deliverables:
- `bot.py` with `--test` mode for offline testing
- `handlers/` directory with command handlers (no Telegram dependency)
- `config.py` for environment variable loading
- `pyproject.toml` with bot dependencies
- This `PLAN.md` document

## Task 2: Backend Integration

Connect handlers to the LMS backend API:
- Create `services/lms_client.py` — HTTP client with Bearer token auth
- Update handlers to fetch real data from `/items/`, `/labs/`, `/scores/` endpoints
- Handle API errors gracefully (timeouts, 401, 500)
- Test with `--test` mode before deploying to Telegram

## Task 3: LLM Intent Routing

Add natural language support using an LLM:
- Create `services/llm_client.py` — LLM API client with tool calling
- Define tools for each handler (e.g., `get_scores(lab_name: str)`)
- Route plain text queries through the LLM to determine intent
- The LLM decides which tool to call based on tool descriptions
- Fallback to "I don't understand" for unrecognized intents

## Task 4: Docker Deployment

Containerize the bot for production:
- Create `bot/Dockerfile` with multi-stage build (similar to backend)
- Add bot service to `docker-compose.yml`
- Configure environment variables via `.env.docker.secret`
- Set up health checks and restart policies
- Deploy to VM and verify in Telegram

## Testing Strategy

- **Unit tests**: Test handlers in isolation (pytest)
- **Test mode**: `uv run bot.py --test "/command"` for manual testing
- **Integration tests**: Test API clients with mocked responses
- **E2E tests**: Deploy to VM and test in Telegram

## Git Workflow

For each task:
1. Create issue on GitHub
2. Create branch: `task-N-short-description`
3. Implement and test locally with `--test` mode
4. Create PR with "Closes #..." in description
5. Partner review, then merge
