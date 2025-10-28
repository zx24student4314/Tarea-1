from __future__ import annotations

"""Calculadora simple: función dividir."""

from typing import Union

Number = Union[int, float]

def divide(a: Number, b: Number) -> float:
    """Devuelve la división en coma flotante de a entre b.

    Raises:
        ValueError: si b == 0 con el mensaje "División por cero".
    """
    if b == 0:
        raise ValueError("División por cero")
    return a / b
