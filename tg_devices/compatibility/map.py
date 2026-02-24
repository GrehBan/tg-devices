from tg_devices.compatibility.inspection import is_compatible
from tg_devices.enums.app_version import AppVersion
from tg_devices.enums.os import OS
from tg_devices.enums.system_version import SystemVersion


def get_compatibility_map(
    os_name: OS,
    all_apps: tuple[AppVersion, ...],
    all_app_weights: tuple[int, ...],
    all_systems: tuple[SystemVersion, ...],
) -> dict[SystemVersion, tuple[tuple[AppVersion, ...], tuple[int, ...]]]:
    compat_map = {}
    for sys_idx, sys_ver in enumerate(all_systems):
        compatible_indices = [
            app_idx
            for app_idx, app_ver in enumerate(all_apps)
            if is_compatible(
                os_name, sys_idx, app_idx, sys_ver.value, app_ver.value
            )
        ]

        if not compatible_indices:
            filtered_apps = all_apps
            filtered_weights = all_app_weights
        else:
            filtered_apps = tuple(all_apps[i] for i in compatible_indices)
            filtered_weights = tuple(
                all_app_weights[i] for i in compatible_indices
            )

        compat_map[sys_ver] = (filtered_apps, filtered_weights)

    return compat_map
