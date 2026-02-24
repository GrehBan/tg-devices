from typing import Protocol

from tg_devices.enums.os import OS
from tg_devices.generator.profile import OSProfile


class IDeviceProfileGenerator(Protocol):
    def generate_os_profile(self, os: OS | None = None) -> OSProfile: ...
