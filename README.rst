##########
tg-devices
##########

|License| |Python| |Mypy| |Ruff|

**tg-devices** is a robust Python library designed to generate realistic, statistically plausible, and technically compatible device profiles for Telegram clients.

It simulates various operating systems (Windows, macOS, Linux), system versions, app versions, and device models, ensuring that the generated combinations mirror real-world usage distributions and adhere to strict compatibility rules.

.. contents:: Table of Contents
   :depth: 2
   :local:

Features
========

- **Realistic Simulation**: Uses weighted random generation based on real-world market share data to create believable device profiles.
- **Cross-Platform Support**: Full support for **Windows**, **macOS**, **Linux**, and **Android** environments.
- **Compatibility Engine**: Intelligent verification logic ensures that generated App versions are strictly compatible with the selected System version (e.g., preventing legacy apps on new OSs or vice versa).
- **Extensive Device Database**: Includes thousands of device models, from legacy hardware to projected 2026 flagships (e.g., Samsung Galaxy S26, Pixel 11).
- **Type Safety**: Built with strict static type checking enabled (``mypy --strict``) for maximum reliability.
- **Modern Architecture**: Specific Enums for every component (``OS``, ``DeviceModel``, ``SystemVersion``, ``AppVersion``) and Protocol-based dependency injection for Randomness and Weight providers.

Requirements
============

- **Python**: 3.14+ (Bleeding Edge)
- **Package Manager**: ``uv`` (recommended) or ``pip``

Installation
============

Since this package is currently in active development, you can install it directly from the source:

.. code-block:: bash

    # Using uv (Recommended)
    uv add git+https://github.com/GrehBan/tg-devices.git

    # Using pip
    pip install git+https://github.com/GrehBan/tg-devices.git

Usage
=====

Basic Generation
----------------

The simplest way to use ``tg-devices`` is to instantiate the generator and call ``generate_os_profile``.

.. code-block:: python

    from tg_devices.generator.generator import DeviceProfileGenerator

    # Initialize the generator
    generator = DeviceProfileGenerator()

    # Generate a random profile
    profile = generator.generate_os_profile()

    print(f"OS: {profile.os}")                 # e.g., "Windows"
    print(f"System: {profile.system_version}") # e.g., "Windows 10 22H2"
    print(f"App: {profile.app_version}")       # e.g., "4.14.13 x64"
    print(f"Device: {profile.device_model}")   # e.g., "Desktop"

Custom OS Weight Distribution
-----------------------------

By default, ``StaticWeightProvider`` uses preset OS weights (Windows 30 %, macOS 15 %, Linux 5 %, Android 50 %).
You can override them by passing keyword arguments that sum to 100, or provide a partial set and let the library
distribute the remainder proportionally.

.. code-block:: python

    from tg_devices.generator.generator import DeviceProfileGenerator
    from tg_devices.weight.provider import StaticWeightProvider

    # Fully custom weights (must sum to 100)
    provider = StaticWeightProvider(windows=50, macos=10, linux=5, android=35)
    generator = DeviceProfileGenerator(weight_provider=provider)

    # Partial weights — the rest is distributed proportionally from the defaults
    provider = StaticWeightProvider(android=80)
    generator = DeviceProfileGenerator(weight_provider=provider)

Specific OS Generation
----------------------

You can force the generator to produce a profile for a specific Operating System using the ``OS`` enum.

.. code-block:: python

    from tg_devices.generator.generator import DeviceProfileGenerator
    from tg_devices.enums.os import OS

    generator = DeviceProfileGenerator()

    # Generate a macOS specific profile
    mac_profile = generator.generate_os_profile(os=OS.MACOS)
    print(f"Generated {mac_profile.os} running on {mac_profile.system_version}")

    # Generate an Android profile (includes projected 2026 devices)
    android_profile = generator.generate_os_profile(os=OS.ANDROID)
    print(f"Device: {android_profile.device_model}")  # e.g., "Samsung Galaxy S26 Ultra"
    print(f"System: {android_profile.system_version}") # e.g., "16.0"

Output Data Structure
---------------------

The generator returns an ``OSProfile`` dataclass (frozen) containing string representations of the profile components.

.. code-block:: python

    @dataclass(frozen=True)
    class OSProfile:
        os: str             # The Operating System name
        app_version: str    # The Telegram App version
        system_version: str # The specific OS version
        device_model: str   # The hardware model identifier

Development
===========

This project uses `uv <https://github.com/astral-sh/uv>`_ for dependency management and workflow automation.

Setup
-----

1. Clone the repository:

   .. code-block:: bash

       git clone https://github.com/GrehBan/tg-devices.git
       cd tg-devices

2. Sync dependencies:

   .. code-block:: bash

       uv sync

Code Quality
------------

We enforce strict code quality standards. Ensure all checks pass before committing.

**Linting & Formatting (Ruff):**

.. code-block:: bash

    uv run ruff check .
    uv run ruff format .

**Type Checking (Mypy):**

.. code-block:: bash

    uv run mypy .

License
=======

This project is licensed under the MIT License - see the LICENSE file for details.

Authors
=======

- **GrehBan** - `maximfeedback19@gmail.com`

.. |License| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT

.. |Python| image:: https://img.shields.io/badge/python-3.14+-blue.svg
   :target: https://www.python.org/downloads/

.. |Mypy| image:: https://img.shields.io/badge/mypy-checked-blue.svg
   :target: https://mypy-lang.org/

.. |Ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
   :target: https://github.com/astral-sh/ruff
