MAXIMO = 22  # LIMITE = 20 + D (D = 2)


def desconto_valido(percentual):
    if percentual <= 0:
        return False
    return percentual <= MAXIMO
