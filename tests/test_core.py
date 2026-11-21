from __future__ import annotations

import pytest

import new_package
from new_package import greet


def test_greet_strips_the_name() -> None:
    assert greet("  Ada ") == "Hello, Ada!"


@pytest.mark.parametrize("name", ["", "   "])
def test_greet_rejects_empty_names(name: str) -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        greet(name)


def test_version_is_exposed() -> None:
    assert isinstance(new_package.__version__, str)
