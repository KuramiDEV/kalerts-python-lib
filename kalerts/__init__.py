from __future__ import annotations
import os
import sys

__version__ = "0.1.0"

_RESET = "\033[0m"
_BOLD = "\033[1m"


def _enable_windows_ansi() -> None:
    if os.name != "nt":
        return
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        mode = ctypes.c_uint32()
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            kernel32.SetConsoleMode(handle, mode.value | 0x0004)
    except Exception:
        pass


_enable_windows_ansi()


def _supports_color() -> bool:
    if os.environ.get("NO_COLOR"):
        return False
    if os.name == "nt":
        return True
    return sys.stdout.isatty()


_LEVELS = {
    "ERROR":   {"color": "\033[91m", "label": "ERROR",   "mark": "!!!"},
    "SUCCESS": {"color": "\033[92m", "label": "SUCCESS", "mark": "+++"},
    "WARN":    {"color": "\033[93m", "label": "WARN",    "mark": "!?!"},
    "TIP":     {"color": "\033[96m", "label": "TIP",     "mark": ">>>"},
    "DEBUG":   {"color": "\033[95m", "label": "DEBUG",   "mark": ":::"},
    "INFO":    {"color": "\033[94m", "label": "INFO",    "mark": "---"},
}


def _paint(text: str, color: str, bold: bool = False) -> str:
    if not _supports_color():
        return text
    prefix = color + (_BOLD if bold else "")
    return f"{prefix}{text}{_RESET}"


def _line(level: str, text: str) -> str:
    text = str(text).replace("\n", " ").strip()
    meta = _LEVELS[level]
    color = meta["color"]
    label = meta["label"]
    mark = meta["mark"]
    tag = _paint(f"[ {label} ]", color, bold=True)
    marker = _paint(mark, color, bold=True)
    return f"{tag} {marker} {text}"


def _emit(level: str, text: str) -> None:
    sys.stdout.write(_line(level, text) + "\n")
    sys.stdout.flush()


def error(text: str) -> None:
    _emit("ERROR", text)


def success(text: str) -> None:
    _emit("SUCCESS", text)


def warn(text: str) -> None:
    _emit("WARN", text)


def tip(text: str) -> None:
    _emit("TIP", text)


def debug(text: str) -> None:
    _emit("DEBUG", text)


def info(text: str) -> None:
    _emit("INFO", text)


__all__ = ["error", "success", "warn", "tip", "debug", "info"]
