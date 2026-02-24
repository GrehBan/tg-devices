import re

from tg_devices.enums.os import OS


def parse_version(version_str: str) -> tuple[int, ...]:
    # Extract only the numeric part (e.g., from "6.5.1 x64")
    match = re.search(r"(\d+(?:\.\d+)+)", version_str)
    if not match:
        return (0,)
    return tuple(map(int, match.group(1).split(".")))


def is_compatible(
    os: OS, sys_idx: int, app_idx: int, sys_ver: str, app_ver: str
) -> bool:
    app_v = parse_version(app_ver)
    sys_v = parse_version(sys_ver)

    # 1. User Rule: Telegram Desktop 6.x requires Windows 7+ and macOS 10.13+
    if app_v[0] >= 6:
        if os == OS.WINDOWS:
            # Win 7 is 6.1, Win 10 is 10.0
            if sys_v < (6, 1):
                return False
        elif os == OS.MACOS:
            # macOS 10.13
            if sys_v < (10, 13):
                return False

    # 2. Android Compatibility Rules
    if os == OS.ANDROID:
        # Telegram 10.x requires Android 6.0+
        if app_v[0] >= 10 and sys_v < (6, 0):
            return False
        # Telegram 11.x+ likely requires Android 7.0+ (projected)
        if app_v[0] >= 11 and sys_v < (7, 0):
            return False
        # Telegram 12.x+ likely requires Android 8.0+ (projected)
        if app_v[0] >= 12 and sys_v < (8, 0):
            return False

    # 3. Rule: Old app_version should not appear with new system_version.
    if os == OS.WINDOWS:
        if sys_idx >= 14 and app_idx <= 27:
            return False

    elif os == OS.MACOS:
        # If system is Sonoma+ (index 13+), avoid 4.x apps (index 0-30).
        if sys_idx >= 13 and app_idx <= 30:
            return False

    elif os == OS.ANDROID:
        # Avoid running very old apps (8.x, 9.x) on bleeding edge Android 15+
        # app_idx 0-1 are 8.x/9.x
        # sys_idx 12+ are Android 15/16/17
        if sys_idx >= 12 and app_idx <= 1:
            return False

    return True
