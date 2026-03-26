"""Command handlers for the bot.

Handlers are plain functions that take input and return text.
They don't depend on Telegram — same logic works from --test mode,
unit tests, or the actual Telegram bot.
"""


async def handle_start(user_id: int | None = None) -> str:
    """Handle /start command.

    Args:
        user_id: Optional Telegram user ID (not used in test mode)

    Returns:
        Welcome message text
    """
    return (
        "👋 Welcome to the LMS Bot!\n\n"
        "I can help you check your lab scores, view available labs, "
        "and answer questions about your progress.\n\n"
        "Use /help to see all available commands."
    )


async def handle_help(user_id: int | None = None) -> str:
    """Handle /help command.

    Returns:
        List of available commands
    """
    return (
        "📚 Available commands:\n\n"
        "/start - Welcome message\n"
        "/help - Show this help message\n"
        "/health - Check bot and backend status\n"
        "/labs - List available labs\n"
        "/scores [lab_name] - Get your scores for a lab"
    )


async def handle_health(user_id: int | None = None) -> str:
    """Handle /health command.

    Returns:
        Health status message (placeholder for Task 2)
    """
    return "✅ Bot is running. Backend health check coming soon."


async def handle_labs(user_id: int | None = None) -> str:
    """Handle /labs command.

    Returns:
        List of available labs (placeholder for Task 2)
    """
    return "📋 Available labs will be shown here (Task 2)."


async def handle_scores(lab_name: str | None = None, user_id: int | None = None) -> str:
    """Handle /scores command.

    Args:
        lab_name: Optional lab name to filter scores
        user_id: Optional Telegram user ID

    Returns:
        Scores information (placeholder for Task 2)
    """
    if lab_name:
        return f"📊 Scores for {lab_name} will be shown here (Task 2)."
    return "📊 Your recent scores will be shown here (Task 2)."
