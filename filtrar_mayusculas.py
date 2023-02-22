def filtrar_mayusculas():
    palabra = input('Ingresa una cadena de palabras')

    count = 0
    for letra in palabra:
        if letra.isupper():
            count += 1
            print(letra)

    return count

print(filtrar_mayusculas())