def binario_entero(numero_binario):
    decimal = 0
    aux = 0
    for numero in str(numero_binario):
        current = int(numero) * 2
        decimal = decimal + int(current) ** aux
        aux += 1

    return decimal

print(binario_entero(11010))