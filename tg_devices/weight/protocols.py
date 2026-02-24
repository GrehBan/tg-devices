from typing import Protocol

from tg_devices.enums.os import OS
from tg_devices.weight.weights import StaticOSWeights


class IWeightProvider(Protocol):
    def get_os_weights(self, os: OS) -> StaticOSWeights: ...

    def get_os_names(self) -> tuple[OS, ...]: ...

    def get_os_probabilities(self) -> tuple[int, ...]: ...
