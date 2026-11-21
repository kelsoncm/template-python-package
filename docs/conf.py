"""Configuração do Sphinx."""

from __future__ import annotations

import sys
from importlib.metadata import version as package_version
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

project = "new-package"
author = "{{AUTHOR}}"
copyright = "{{YEAR}}, {{AUTHOR}}"
release = package_version("new-package")

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.githubpages",
    "sphinx.ext.viewcode",
]
autodoc_typehints = "description"
exclude_patterns = ["_build"]

html_theme = "furo"
html_title = f"new-package {release}"
