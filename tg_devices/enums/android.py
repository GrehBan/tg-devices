"""Android-specific device model, app version, and system version enums."""

from tg_devices.enums.app_version import AppVersion
from tg_devices.enums.device_model import DeviceModel
from tg_devices.enums.system_version import SystemVersion


class AndroidModel(DeviceModel):
    """Android smartphone model identifiers."""

    # --- Samsung ---
    SAMSUNG_GALAXY_S26_ULTRA = "Samsung Galaxy S26 Ultra"
    SAMSUNG_GALAXY_S26_PLUS = "Samsung Galaxy S26+"
    SAMSUNG_GALAXY_S26 = "Samsung Galaxy S26"
    SAMSUNG_GALAXY_S25_ULTRA = "Samsung Galaxy S25 Ultra"
    SAMSUNG_GALAXY_S25_PLUS = "Samsung Galaxy S25+"
    SAMSUNG_GALAXY_S25 = "Samsung Galaxy S25"
    SAMSUNG_GALAXY_S24_ULTRA = "Samsung Galaxy S24 Ultra"
    SAMSUNG_GALAXY_S24_PLUS = "Samsung Galaxy S24+"
    SAMSUNG_GALAXY_S24 = "Samsung Galaxy S24"
    SAMSUNG_GALAXY_S23_ULTRA = "Samsung Galaxy S23 Ultra"
    SAMSUNG_GALAXY_S23_PLUS = "Samsung Galaxy S23+"
    SAMSUNG_GALAXY_S23 = "Samsung Galaxy S23"
    SAMSUNG_GALAXY_S22_ULTRA = "Samsung Galaxy S22 Ultra"
    SAMSUNG_GALAXY_S22_PLUS = "Samsung Galaxy S22+"
    SAMSUNG_GALAXY_S22 = "Samsung Galaxy S22"
    SAMSUNG_GALAXY_S21_ULTRA = "Samsung Galaxy S21 Ultra"
    SAMSUNG_GALAXY_S21_PLUS = "Samsung Galaxy S21+"
    SAMSUNG_GALAXY_S21 = "Samsung Galaxy S21 5G"
    SAMSUNG_GALAXY_S20_FE = "Samsung Galaxy S20 FE 5G"
    SAMSUNG_GALAXY_A56 = "Samsung Galaxy A56"
    SAMSUNG_GALAXY_A55 = "Samsung Galaxy A55"
    SAMSUNG_GALAXY_A54 = "Samsung Galaxy A54 5G"
    SAMSUNG_GALAXY_A53 = "Samsung Galaxy A53 5G"
    SAMSUNG_GALAXY_A52S = "Samsung Galaxy A52s 5G"
    SAMSUNG_GALAXY_A35 = "Samsung Galaxy A35"
    SAMSUNG_GALAXY_A34 = "Samsung Galaxy A34 5G"
    SAMSUNG_GALAXY_Z_FOLD_7 = "Samsung Galaxy Z Fold 7"
    SAMSUNG_GALAXY_Z_FLIP_7 = "Samsung Galaxy Z Flip 7"
    SAMSUNG_GALAXY_Z_FOLD_6 = "Samsung Galaxy Z Fold 6"
    SAMSUNG_GALAXY_Z_FLIP_6 = "Samsung Galaxy Z Flip 6"
    SAMSUNG_GALAXY_Z_FOLD_5 = "Samsung Galaxy Z Fold 5"
    SAMSUNG_GALAXY_Z_FLIP_5 = "Samsung Galaxy Z Flip 5"

    # --- Google ---
    GOOGLE_PIXEL_11_PRO = "Google Pixel 11 Pro"
    GOOGLE_PIXEL_11 = "Google Pixel 11"
    GOOGLE_PIXEL_10_PRO = "Google Pixel 10 Pro"
    GOOGLE_PIXEL_10 = "Google Pixel 10"
    GOOGLE_PIXEL_9_PRO = "Google Pixel 9 Pro"
    GOOGLE_PIXEL_9 = "Google Pixel 9"
    GOOGLE_PIXEL_8_PRO = "Google Pixel 8 Pro"
    GOOGLE_PIXEL_8 = "Google Pixel 8"
    GOOGLE_PIXEL_7_PRO = "Google Pixel 7 Pro"
    GOOGLE_PIXEL_7 = "Google Pixel 7"
    GOOGLE_PIXEL_6A = "Google Pixel 6a"
    GOOGLE_PIXEL_7A = "Google Pixel 7a"
    GOOGLE_PIXEL_8A = "Google Pixel 8a"
    GOOGLE_PIXEL_9A = "Google Pixel 9a"
    GOOGLE_PIXEL_FOLD_2 = "Google Pixel Fold 2"

    # --- Xiaomi ---
    XIAOMI_16_ULTRA = "Xiaomi 16 Ultra"
    XIAOMI_16_PRO = "Xiaomi 16 Pro"
    XIAOMI_16 = "Xiaomi 16"
    XIAOMI_15_ULTRA = "Xiaomi 15 Ultra"
    XIAOMI_15_PRO = "Xiaomi 15 Pro"
    XIAOMI_15 = "Xiaomi 15"
    XIAOMI_14_ULTRA = "Xiaomi 14 Ultra"
    XIAOMI_14_PRO = "Xiaomi 14 Pro"
    XIAOMI_14 = "Xiaomi 14"
    XIAOMI_13_ULTRA = "Xiaomi 13 Ultra"
    XIAOMI_13_PRO = "Xiaomi 13 Pro"
    XIAOMI_13 = "Xiaomi 13"
    REDMI_NOTE_15_PRO_PLUS = "Redmi Note 15 Pro+"
    REDMI_NOTE_14_PRO_PLUS = "Redmi Note 14 Pro+"
    REDMI_NOTE_13_PRO_PLUS = "Redmi Note 13 Pro+"
    POCO_F8_PRO = "POCO F8 Pro"
    POCO_F7_PRO = "POCO F7 Pro"
    POCO_F6_PRO = "POCO F6 Pro"
    POCO_X7_PRO = "POCO X7 Pro"
    POCO_X6_PRO = "POCO X6 Pro"

    # --- OnePlus ---
    ONEPLUS_14 = "OnePlus 14"
    ONEPLUS_13 = "OnePlus 13"
    ONEPLUS_12 = "OnePlus 12"
    ONEPLUS_11 = "OnePlus 11"
    ONEPLUS_NORD_5 = "OnePlus Nord 5"
    ONEPLUS_NORD_4 = "OnePlus Nord 4"
    ONEPLUS_NORD_3 = "OnePlus Nord 3"

    # --- Nothing ---
    NOTHING_PHONE_4 = "Nothing Phone (4)"
    NOTHING_PHONE_3 = "Nothing Phone (3)"
    NOTHING_PHONE_2 = "Nothing Phone (2)"
    NOTHING_PHONE_2A = "Nothing Phone (2a)"

    # --- Motorola ---
    MOTOROLA_EDGE_60_PRO = "Motorola Edge 60 Pro"
    MOTOROLA_EDGE_50_PRO = "Motorola Edge 50 Pro"
    MOTOROLA_EDGE_40_PRO = "Motorola Edge 40 Pro"
    MOTOROLA_RAZR_60_ULTRA = "Motorola Razr 60 Ultra"
    MOTOROLA_RAZR_50_ULTRA = "Motorola Razr 50 Ultra"

    # --- Sony ---
    SONY_XPERIA_1_VIII = "Sony Xperia 1 VIII"
    SONY_XPERIA_1_VII = "Sony Xperia 1 VII"
    SONY_XPERIA_1_VI = "Sony Xperia 1 VI"
    SONY_XPERIA_5_VII = "Sony Xperia 5 VII"
    SONY_XPERIA_5_VI = "Sony Xperia 5 VI"


class AndroidAppVersion(AppVersion):
    """Telegram for Android version strings."""

    # Historical
    V8_9_3 = "8.9.3"
    V9_6_5 = "9.6.5"
    V10_0_1 = "10.0.1"
    V10_1_0 = "10.1.0"
    V10_2_3 = "10.2.3"
    V10_3_2 = "10.3.2"
    V10_4_1 = "10.4.1"
    V10_5_0 = "10.5.0"
    V10_6_1 = "10.6.1"
    V10_7_0 = "10.7.0"
    V10_8_1 = "10.8.1"
    V10_9_0 = "10.9.0"
    V10_10_1 = "10.10.1"
    V10_11_0 = "10.11.0"
    V10_12_0 = "10.12.0"
    V10_13_0 = "10.13.0"
    V10_14_0 = "10.14.0"

    # 2025 Predictions (11.x)
    V11_0_0 = "11.0.0"
    V11_1_2 = "11.1.2"
    V11_2_0 = "11.2.0"
    V11_3_4 = "11.3.4"
    V11_4_1 = "11.4.1"
    V11_5_0 = "11.5.0"
    V11_6_2 = "11.6.2"
    V11_7_1 = "11.7.1"
    V11_8_0 = "11.8.0"
    V11_9_3 = "11.9.3"

    # 2026 Predictions (12.x)
    V12_0_0 = "12.0.0"
    V12_1_1 = "12.1.1"
    V12_2_3 = "12.2.3"
    V12_3_0 = "12.3.0"
    V12_4_2 = "12.4.2"
    V12_5_0 = "12.5.0"  # Mid-2026 Stable


class AndroidSystemVersion(SystemVersion):
    """Android OS version strings (Marshmallow through Android 17)."""

    ANDROID_6_0 = "6.0"  # Marshmallow
    ANDROID_7_0 = "7.0"  # Nougat
    ANDROID_7_1 = "7.1"
    ANDROID_8_0 = "8.0"  # Oreo
    ANDROID_8_1 = "8.1"
    ANDROID_9_0 = "9.0"  # Pie
    ANDROID_10_0 = "10.0"  # Q
    ANDROID_11_0 = "11.0"  # R
    ANDROID_12_0 = "12.0"  # S
    ANDROID_12_1 = "12.1"  # S (12L)
    ANDROID_13_0 = "13.0"  # Tiramisu
    ANDROID_14_0 = "14.0"  # Upside Down Cake
    ANDROID_15_0 = "15.0"  # Vanilla Ice Cream (2024)
    ANDROID_16_0 = "16.0"  # 2025
    ANDROID_17_0 = "17.0"  # 2026
