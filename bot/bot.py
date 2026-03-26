#!/usr/bin/env python3
"""LMS Telegram Bot entry point.

Usage:
    uv run bot.py              # Run as Telegram bot
    uv run bot.py --test "/start"  # Test mode: print response to stdout
"""

import argparse
import asyncio
import sys
from pathlib import Path

# Add bot directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from handlers import (
    handle_start,
    handle_help,
    handle_health,
    handle_labs,
    handle_scores,
)


def parse_command(text: str) -> tuple[str, str | None]:
    """Parse a command string into command and argument.

    Args:
        text: Input text like "/start" or "/scores lab-04"

    Returns:
        Tuple of (command, argument)
    """
    parts = text.strip().split(maxsplit=1)
    command = parts[0].lower()
    argument = parts[1] if len(parts) > 1 else None
    return command, argument


async def process_command(command: str, argument: str | None = None) -> str:
    """Route command to appropriate handler.

    Args:
        command: Command name (e.g., "/start", "/scores")
        argument: Optional command argument

    Returns:
        Handler response text
    """
    if command in ("/start", "start"):
        return await handle_start()
    elif command in ("/help", "help"):
        return await handle_help()
    elif command in ("/health", "health"):
        return await handle_health()
    elif command in ("/labs", "labs"):
        return await handle_labs()
    elif command in ("/scores", "scores"):
        return await handle_scores(lab_name=argument)
    else:
        return f"❓ Unknown command: {command}. Use /help to see available commands."


async def run_test_mode(command_text: str) -> None:
    """Run bot in test mode: print response to stdout.

    Args:
        command_text: Command to test (e.g., "/start", "/scores lab-04")
    """
    command, argument = parse_command(command_text)
    response = await process_command(command, argument)
    print(response)


async def run_telegram_mode() -> None:
    """Run bot as Telegram bot (to be implemented in Task 2)."""
    print("Telegram bot mode not yet implemented (Task 2)")
    print("For now, use --test mode to test handlers.")


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="LMS Telegram Bot",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    uv run bot.py --test "/start"
    uv run bot.py --test "/help"
    uv run bot.py --test "/health"
    uv run bot.py --test "/labs"
    uv run bot.py --test "/scores lab-04"
        """,
    )
    parser.add_argument(
        "--test",
        metavar="COMMAND",
        help="Test mode: run a command and print response to stdout",
    )

    args = parser.parse_args()

    if args.test:
        # Test mode: run command and exit
        asyncio.run(run_test_mode(args.test))
    else:
        # Telegram mode (placeholder for Task 2)
        asyncio.run(run_telegram_mode())


if __name__ == "__main__":
    main()
