"""Core device profile generator implementation."""

from typing import Unpack

from tg_devices.enums.os import OS
from tg_devices.generator.profile import OSProfile
from tg_devices.generator.protocols import IDeviceProfileGenerator
from tg_devices.random.protocols import IRandomProvider
from tg_devices.random.provider import StandardRandomProvider
from tg_devices.weight.protocols import IWeightProvider
from tg_devices.weight.provider import StaticWeightProvider, WeightParams


class DeviceProfileGenerator(IDeviceProfileGenerator):
    """Generates realistic Telegram client device profiles.

    Combines a randomness provider with a weight provider to produce
    statistically plausible and version-compatible device profiles.

    Args:
        random_provider: Custom randomness source. Defaults to
            ``StandardRandomProvider``.
        weight_provider: Custom weight/data source. Defaults to
            ``StaticWeightProvider``.
        **weight_params: Per-OS weight overrides forwarded to
            ``StaticWeightProvider`` (e.g. ``windows=40, android=60``).
    """

    def __init__(
        self,
        random_provider: IRandomProvider | None = None,
        weight_provider: IWeightProvider | None = None,
        **weight_params: Unpack[WeightParams],
    ) -> None:
        self._random_provider = random_provider or StandardRandomProvider()
        self._weight_provider = weight_provider or StaticWeightProvider(
            **weight_params
        )

    def generate_os_profile(self, os: OS | None = None) -> OSProfile:
        """Generate a complete device profile.

        Selects an OS (or uses the one provided), then picks a
        system version, a compatible app version, and a device model
        using weighted random selection.

        Args:
            os: Target operating system. If ``None``, an OS is
                chosen via weighted random selection.

        Returns:
            A frozen ``OSProfile`` with all fields populated.
        """
        chosen_os = os or self._random_provider.choice(
            population=self._weight_provider.get_os_names(),
            weights=self._weight_provider.get_os_probabilities(),
        )
        weights = self._weight_provider.get_os_weights(chosen_os)

        system_version = self._random_provider.choice(
            population=weights.system_version,
            weights=weights.weights.system_weights,
        )

        filtered_apps, filtered_weights = weights.compatibility_map[
            system_version
        ]
        app_version = self._random_provider.choice(
            population=filtered_apps, weights=filtered_weights
        )

        device_model = self._random_provider.choice(
            population=weights.device_model
        )

        return OSProfile(
            os=chosen_os.value,
            app_version=app_version.value,
            system_version=system_version.value,
            device_model=device_model.value,
        )
