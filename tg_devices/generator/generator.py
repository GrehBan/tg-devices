from tg_devices.enums.os import OS
from tg_devices.generator.profile import OSProfile
from tg_devices.generator.protocols import IDeviceProfileGenerator
from tg_devices.random.protocols import IRandomProvider
from tg_devices.random.provider import StandardRandomProvider
from tg_devices.weight.protocols import IWeightProvider
from tg_devices.weight.provider import StaticWeightProvider


class DeviceProfileGenerator(IDeviceProfileGenerator):
    def __init__(
        self,
        random_provider: IRandomProvider | None = None,
        weight_provider: IWeightProvider | None = None,
    ) -> None:
        self._random_provider = random_provider or StandardRandomProvider()
        self._weight_provider = weight_provider or StaticWeightProvider()

    def generate_os_profile(self, os: OS | None = None) -> OSProfile:

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
