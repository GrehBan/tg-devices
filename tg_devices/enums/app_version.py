"""Base class for Telegram application version enums."""

from enum import StrEnum


class AppVersion(StrEnum):
    """Base enum for Telegram client version strings.

    Platform-specific subclasses (e.g. ``WindowsAppVersion``,
    ``AndroidAppVersion``) define the concrete members.
    """
