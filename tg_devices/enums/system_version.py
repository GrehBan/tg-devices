"""Base class for operating system version enums."""

from enum import StrEnum


class SystemVersion(StrEnum):
    """Base enum for OS version strings.

    Platform-specific subclasses (e.g. ``WindowsSystemVersion``,
    ``AndroidSystemVersion``) define the concrete members.
    """
