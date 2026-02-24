from dataclasses import dataclass

from tg_devices.enums.app_version import AppVersion
from tg_devices.enums.device_model import DeviceModel
from tg_devices.enums.system_version import SystemVersion


@dataclass
class Weights:
    app_weights: tuple[int, ...]
    system_weights: tuple[int, ...]


@dataclass
class StaticOSWeights:
    app_version: tuple[AppVersion, ...]
    system_version: tuple[SystemVersion, ...]
    device_model: tuple[DeviceModel, ...]
    weight: int
    weights: Weights
    compatibility_map: dict[
        SystemVersion, tuple[tuple[AppVersion, ...], tuple[int, ...]]
    ]
