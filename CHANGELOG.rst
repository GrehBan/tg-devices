#########
Changelog
#########

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

0.1.1 - 2026-02-25
==================

Added
-----
- ``WeightParams`` ``TypedDict`` enabling customizable per-OS weight distribution when instantiating ``StaticWeightProvider`` (e.g., ``StaticWeightProvider(windows=40, android=60)``).
- ``StaticWeightProvider.__init__`` now accepts ``**weight_params: Unpack[WeightParams]``; missing OS weights are distributed proportionally from the remaining budget (weights must sum to 100).
- Pre-computed compatibility maps at module level (``WINDOWS_COMPATIBILITY_MAP``, ``MACOS_COMPATIBILITY_MAP``, ``LINUX_COMPATIBILITY_MAP``, ``ANDROID_COMPATIBILITY_MAP``) to avoid redundant computation on every provider instantiation.
- Pre-computed ``Weights`` dataclass instances (``WINDOWS_WEIGHTS_DT``, ``MACOS_WEIGHTS_DT``, ``LINUX_WEIGHTS_DT``, ``ANDROID_WEIGHTS_DT``) exposed from ``introspection`` module.
- Pre-computed device model tuples (``WINDOWS_DEVICE_MODEL``, ``MACOS_DEVICE_MODEL``, ``LINUX_DEVICE_MODEL``, ``ANDROID_DEVICE_MODEL``) and ``OS_NAMES`` exposed from ``introspection`` module.
- ``py.typed`` marker file added for PEP 561 compliance (package now advertises inline type information).

Changed
-------
- ``StaticWeightProvider.map`` and ``os_probabilities`` are now instance attributes built inside ``__init__`` instead of class-level attributes, supporting per-instance weight configuration.
- All weight mapping constants (``WINDOWS_APP_WEIGHTS``, ``MACOS_APP_WEIGHTS``, etc.) are now annotated with ``Final``.
- Replaced ``zip(*dict.items())`` tuple unpacking with explicit ``tuple(dict.keys())`` / ``tuple(dict.values())`` calls, each annotated with ``Final``.

Removed
-------
- Removed ``uv.lock`` from version control.

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
