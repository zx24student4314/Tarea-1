def divide(a, b):
    """Divide a entre b usando división de coma flotante.

    Levanta ValueError("División por cero") si b == 0.
    """
    if b == 0:
        raise ValueError("División por cero")
    return a / b
