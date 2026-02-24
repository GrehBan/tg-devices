from tg_devices.compatibility.map import get_compatibility_map
from tg_devices.enums.android import AndroidModel
from tg_devices.enums.linux import LinuxDesktopModel
from tg_devices.enums.macos import MacOSDesktopModel
from tg_devices.enums.os import OS
from tg_devices.enums.windows import WindowsDesktopModel
from tg_devices.weight.introspection import (
    ANDROID_APPS,
    ANDROID_APPS_WEIGHTS,
    ANDROID_SYSTEMS,
    ANDROID_SYSTEMS_WEIGHTS,
    LIN_APPS_WEIGHTS,
    LIN_SYSTEMS_WEIGHTS,
    LINUX_APPS,
    LINUX_SYSTEMS,
    MAC_APPS,
    MAC_APPS_WEIGHTS,
    MAC_SYSTEMS,
    MAC_SYSTEMS_WEIGHTS,
    WIN_APPS,
    WIN_APPS_WEIGHTS,
    WIN_SYSTEMS,
    WIN_SYSTEMS_WEIGHTS,
)
from tg_devices.weight.protocols import IWeightProvider
from tg_devices.weight.weights import StaticOSWeights, Weights


class StaticWeightProvider(IWeightProvider):
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

    map = {
        OS.WINDOWS: StaticOSWeights(
            app_version=windows_apps,
            system_version=windows_systems,
            device_model=tuple(WindowsDesktopModel),
            weight=30,
            weights=Weights(
                app_weights=windows_app_weights,
                system_weights=windows_system_weights,
            ),
            compatibility_map=get_compatibility_map(
                OS.WINDOWS, windows_apps, windows_app_weights, windows_systems
            ),
        ),
        OS.MACOS: StaticOSWeights(
            app_version=macos_apps,
            system_version=macos_systems,
            device_model=tuple(MacOSDesktopModel),
            weight=15,
            weights=Weights(
                app_weights=macos_app_weights,
                system_weights=macos_system_weights,
            ),
            compatibility_map=get_compatibility_map(
                OS.MACOS, macos_apps, macos_app_weights, macos_systems
            ),
        ),
        OS.LINUX: StaticOSWeights(
            app_version=linux_apps,
            system_version=linux_systems,
            device_model=tuple(LinuxDesktopModel),
            weight=5,
            weights=Weights(
                app_weights=linux_app_weights,
                system_weights=linux_system_weights,
            ),
            compatibility_map=get_compatibility_map(
                OS.LINUX, linux_apps, linux_app_weights, linux_systems
            ),
        ),
        OS.ANDROID: StaticOSWeights(
            app_version=android_apps,
            system_version=android_systems,
            device_model=tuple(AndroidModel),
            weight=50,
            weights=Weights(
                app_weights=android_app_weights,
                system_weights=android_system_weights,
            ),
            compatibility_map=get_compatibility_map(
                OS.ANDROID, android_apps, android_app_weights, android_systems
            ),
        ),
    }

    os_names: tuple[OS, ...] = tuple(OS)
    os_probabilities: tuple[int, ...] = tuple(
        weight.weight for weight in map.values()
    )

    def get_os_weights(self, os: OS) -> StaticOSWeights:
        return self.map[os]

    def get_os_names(self) -> tuple[OS, ...]:
        return self.os_names

    def get_os_probabilities(self) -> tuple[int, ...]:
        return self.os_probabilities
