"""Static weight provider implementation."""

from typing import TypedDict, Unpack, cast

from tg_devices.enums.os import OS
from tg_devices.weight.introspection import (
    ANDROID_APPS,
    ANDROID_APPS_WEIGHTS,
    ANDROID_COMPATIBILITY_MAP,
    ANDROID_DEVICE_MODEL,
    ANDROID_SYSTEMS,
    ANDROID_SYSTEMS_WEIGHTS,
    ANDROID_WEIGHTS_DT,
    LIN_APPS_WEIGHTS,
    LIN_SYSTEMS_WEIGHTS,
    LINUX_APPS,
    LINUX_COMPATIBILITY_MAP,
    LINUX_DEVICE_MODEL,
    LINUX_SYSTEMS,
    LINUX_WEIGHTS_DT,
    MAC_APPS,
    MAC_APPS_WEIGHTS,
    MAC_SYSTEMS,
    MAC_SYSTEMS_WEIGHTS,
    MACOS_COMPATIBILITY_MAP,
    MACOS_DEVICE_MODEL,
    MACOS_WEIGHTS_DT,
    OS_NAMES,
    WIN_APPS,
    WIN_APPS_WEIGHTS,
    WIN_SYSTEMS,
    WIN_SYSTEMS_WEIGHTS,
    WINDOWS_COMPATIBILITY_MAP,
    WINDOWS_DEVICE_MODEL,
    WINDOWS_WEIGHTS_DT,
)
from tg_devices.weight.protocols import IWeightProvider
from tg_devices.weight.weights import StaticOSWeights


class WeightParams(TypedDict, total=False):
    """Per-OS weight overrides for ``StaticWeightProvider``.

    All keys are optional. Provided weights must sum to <= 100;
    missing OS weights are distributed proportionally from the
    remaining budget.

    Attributes:
        windows: Weight for Windows (default 30).
        linux: Weight for Linux (default 5).
        macos: Weight for macOS (default 15).
        android: Weight for Android (default 50).
    """

    windows: int
    linux: int
    macos: int
    android: int


class StaticWeightProvider(IWeightProvider):
    """Provides pre-computed weight distributions for each OS.

    Uses static introspection data (version enums, weight mappings,
    compatibility maps) and builds per-instance ``StaticOSWeights``
    bundles based on the supplied weight parameters.

    Args:
        **weight_params: Per-OS weight overrides. Omitted OS weights
            are distributed proportionally from the remaining budget.
            All weights must sum to 100.

    Raises:
        ValueError: If provided weights sum to >= 100 with missing
            keys, or if final weights do not sum to 100.
    """

    windows_apps = WIN_APPS
    windows_systems = WIN_SYSTEMS
    macos_apps = MAC_APPS
    macos_systems = MAC_SYSTEMS
    linux_apps = LINUX_APPS
    linux_systems = LINUX_SYSTEMS
    android_apps = ANDROID_APPS
    android_systems = ANDROID_SYSTEMS
    windows_app_weights = WIN_APPS_WEIGHTS
    windows_system_weights = WIN_SYSTEMS_WEIGHTS
    macos_app_weights = MAC_APPS_WEIGHTS
    macos_system_weights = MAC_SYSTEMS_WEIGHTS
    linux_app_weights = LIN_APPS_WEIGHTS
    linux_system_weights = LIN_SYSTEMS_WEIGHTS
    android_app_weights = ANDROID_APPS_WEIGHTS
    android_system_weights = ANDROID_SYSTEMS_WEIGHTS
    os_names = OS_NAMES
    windows_compatibility_map = WINDOWS_COMPATIBILITY_MAP
    macos_compatibility_map = MACOS_COMPATIBILITY_MAP
    linux_compatibility_map = LINUX_COMPATIBILITY_MAP
    android_compatibility_map = ANDROID_COMPATIBILITY_MAP
    windows_device_model = WINDOWS_DEVICE_MODEL
    macos_device_model = MACOS_DEVICE_MODEL
    linux_device_model = LINUX_DEVICE_MODEL
    android_device_model = ANDROID_DEVICE_MODEL
    windows_weights_dt = WINDOWS_WEIGHTS_DT
    macos_weights_dt = MACOS_WEIGHTS_DT
    linux_weights_dt = LINUX_WEIGHTS_DT
    android_weights_dt = ANDROID_WEIGHTS_DT

    def __init__(self, **weight_params: Unpack[WeightParams]) -> None:
        defaults = {"windows": 30, "macos": 15, "linux": 5, "android": 50}

        weights: dict[str, int]
        if not weight_params:
            weights = dict(defaults)
        else:
            weights = cast(dict[str, int], dict(weight_params))

        missing_keys = [k for k in defaults if k not in weights]

        if missing_keys:
            provided_sum = sum(weights.values())
            if provided_sum >= 100:
                raise ValueError(
                    f"Sum of provided weights ({provided_sum})"
                    f" is >= 100, but keys {missing_keys} are missing."
                )

            remaining = 100 - provided_sum
            default_sum_missing = sum(defaults[k] for k in missing_keys)

            current_distributed = 0
            for i, key in enumerate(missing_keys):
                if i == len(missing_keys) - 1:
                    val = remaining - current_distributed
                else:
                    val = int(
                        round(
                            (defaults[key] / default_sum_missing) * remaining
                        )
                    )
                    current_distributed += val
                weights[key] = val

        if sum(weights.values()) != 100:
            raise ValueError("Weights must sum up to 100")

        self.map = {
            OS.WINDOWS: StaticOSWeights(
                app_version=self.windows_apps,
                system_version=self.windows_systems,
                device_model=self.windows_device_model,
                weight=weights["windows"],
                weights=self.windows_weights_dt,
                compatibility_map=self.windows_compatibility_map,
            ),
            OS.MACOS: StaticOSWeights(
                app_version=self.macos_apps,
                system_version=self.macos_systems,
                device_model=self.macos_device_model,
                weight=weights["macos"],
                weights=self.macos_weights_dt,
                compatibility_map=self.macos_compatibility_map,
            ),
            OS.LINUX: StaticOSWeights(
                app_version=self.linux_apps,
                system_version=self.linux_systems,
                device_model=self.linux_device_model,
                weight=weights["linux"],
                weights=self.linux_weights_dt,
                compatibility_map=self.linux_compatibility_map,
            ),
            OS.ANDROID: StaticOSWeights(
                app_version=self.android_apps,
                system_version=self.android_systems,
                device_model=self.android_device_model,
                weight=weights["android"],
                weights=self.android_weights_dt,
                compatibility_map=self.android_compatibility_map,
            ),
        }
        self.os_probabilities: tuple[int, ...] = tuple(
            weight.weight for weight in self.map.values()
        )

    def get_os_weights(self, os: OS) -> StaticOSWeights:
        """Return the weight bundle for a given OS.

        Args:
            os: The target operating system.

        Returns:
            A ``StaticOSWeights`` with versions, models, weights,
            and the pre-computed compatibility map.
        """
        return self.map[os]

    def get_os_names(self) -> tuple[OS, ...]:
        """Return all supported operating systems.

        Returns:
            Tuple of ``OS`` enum members.
        """
        return self.os_names

    def get_os_probabilities(self) -> tuple[int, ...]:
        """Return selection probabilities for each OS.

        Returns:
            Tuple of integer weights aligned with ``get_os_names()``.
        """
        return self.os_probabilities
