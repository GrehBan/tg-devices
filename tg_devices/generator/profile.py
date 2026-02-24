from dataclasses import dataclass


@dataclass(frozen=True)
class OSProfile:
    os: str
    app_version: str
    system_version: str
    device_model: str
