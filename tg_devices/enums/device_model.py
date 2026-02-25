"""Base class for device model enums."""

from enum import StrEnum


class DeviceModel(StrEnum):
    """Base enum for hardware device model identifiers.

    Platform-specific subclasses (e.g. ``WindowsDesktopModel``,
    ``AndroidModel``) define the concrete members.
    """
