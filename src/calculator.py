def divide(a, b):
    """Divide a entre b (división en coma flotante).

    Lanza ValueError("División por cero") si b es 0.
    Lanza TypeError si los argumentos no son números.
    """
    try:
        if b == 0:
            raise ValueError("División por cero")
        return a / b
    except TypeError:
        raise TypeError("Los argumentos deben ser números")