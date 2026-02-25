"""Supported operating system enumeration."""

from enum import StrEnum


class OS(StrEnum):
    """Operating systems supported by the device profile generator."""

    WINDOWS = "Windows"
    MACOS = "macOS"
    LINUX = "Linux"
    ANDROID = "Android"
