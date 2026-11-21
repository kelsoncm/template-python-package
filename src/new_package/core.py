"""Exemplo de módulo: troque pelo código do pacote."""

from __future__ import annotations


def greet(name: str) -> str:
    """Devolve uma saudação para ``name``.

    :param name: nome de quem será saudado; não pode ser vazio.
    :raises ValueError: se ``name`` for vazio ou só tiver espaços.
    """
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be empty")
    return f"Hello, {cleaned}!"
