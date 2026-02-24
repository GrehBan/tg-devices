#########
Changelog
#########

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

0.1.0 - 2026-02-24
==================

Added
-----
- Initial release of ``tg-devices``.
- Core ``DeviceProfileGenerator`` for creating realistic device configuration profiles.
- Support for simulating **Windows**, **macOS**, **Linux**, and **Android** environments.
- Added comprehensive Android device database including historical and projected 2026 flagship models (Samsung Galaxy S26, Pixel 11, etc.).
- Implemented Android OS versioning from Android 6.0 to projected Android 17.0.
- Included Telegram for Android version history and future projections (v11.x, v12.x).
- Weighted random generation logic to mirror real-world OS and version distribution statistics.
- Compatibility verification engine to ensure generated App versions are valid for the selected System version.
- Extensive enum definitions for controlled vocabulary:
  - ``OS`` (Operating Systems)
  - ``DeviceModel`` (Hardware identifiers)
  - ``SystemVersion`` (OS specific versions)
  - ``AppVersion`` (Telegram client versions)
- Integration of ``uv`` for modern Python package and dependency management.
- Strict static type checking configuration using ``mypy``.
- Comprehensive linting and formatting rules provided by ``ruff``.
- Python 3.14+ compatibility.

Fixed
-----
- Resolved directory naming typo: renamed ``tg_devices/copmatibility`` to ``tg_devices/compatibility``.
- Fixed type annotation issues in ``tg_devices/weight/provider.py`` to satisfy strict type checking.
- Corrected line length violations in introspection data files to adhere to PEP 8 standards.
