"""Configuration loader for the bot.

Reads settings from environment variables using pydantic-settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class BotSettings(BaseSettings):
    """Bot configuration loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env.bot.secret",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Telegram bot token
    bot_token: str = ""

    # LMS API settings
    lms_api_base_url: str = ""
    lms_api_key: str = ""

    # LLM settings (for Task 3)
    llm_api_key: str = ""
    llm_base_url: str = ""


def load_config() -> BotSettings:
    """Load and return bot configuration."""
    return BotSettings()
