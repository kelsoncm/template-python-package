"""{{DESCRIPTION}}"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from .core import greet

try:
    __version__ = version("new-package")
except PackageNotFoundError:  # pragma: no cover - execução a partir do código-fonte, sem instalar
    __version__ = "0.0.0"

__all__ = ["__version__", "greet"]
