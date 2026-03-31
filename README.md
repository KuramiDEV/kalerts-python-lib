# kalerts

**kalerts** is a lightweight Python library for displaying **stylized one-line terminal alerts** with **ANSI colors**, clean formatting, and zero external dependencies.

It is designed for developers who want simple, readable console messages such as errors, warnings, debug logs, tips, and success notices — without setting up a full logging framework.

## Features

- One-line alert output
- ANSI color support
- Works on Windows, Linux, and macOS
- No external dependencies
- Simple API
- Automatic ANSI enabling on modern Windows terminals
- Different visual marker for each alert type

## Alert Types

`kalerts` includes the following built-in alert styles:

- `error`
- `success`
- `warn`
- `tip`
- `debug`
- `info`

Each alert type has:
- its own label
- its own marker
- its own terminal color

## Installation

```bash
pip install kalerts
```

## Quick Start

```python
import kalerts

kalerts.error("Something went wrong")
kalerts.success("Operation completed successfully")
kalerts.warn("Be careful with this step")
kalerts.tip("You can reuse this function later")
kalerts.debug("x = 10")
kalerts.info("Process started")
```

## Output Example

<img style="width:50%" src="https://github.com/KuramiDEV/SixSeven-Spicetify-Extension/blob/main/preview.png"/>

## Example

```python
import kalerts

def connect_database():
    kalerts.info("Connecting to database")
    kalerts.success("Database connected")

def validate_user_input(username):
    if not username:
        kalerts.error("Username cannot be empty")
        return

    if len(username) < 3:
        kalerts.warn("Username is very short")

    kalerts.tip("Use a memorable username")
    kalerts.debug(f"Validated username: {username}")

validate_user_input("ab")
connect_database()
```

## How It Works

Each function writes directly to the terminal output, so you do not need to use `print()`.

Example:

```python
import kalerts

kalerts.error("File not found")
```

Not:

```python
print(kalerts.error("File not found"))
```

## Compatibility

`kalerts` is compatible with:

- Python 3.8+
- Windows
- Linux
- macOS

On Windows, the library attempts to enable ANSI escape support automatically using the built-in `ctypes` module.

## Philosophy

`kalerts` focuses on simplicity:

- no configuration files
- no external dependencies
- no complex logger setup
- just readable and colorful terminal alerts

## License

This project is licensed under the MIT License.
