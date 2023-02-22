
def multiply(numero1, numero2):

    result = 0
    for _ in range(1,numero2 + 1):
        result += numero1
    
    return result


if __name__ == '__main__':

    numero1 = int(input('Digite el numero que desea multiplicar: '))
    numero2 = int(input(f'Digite el numero por el que desea multiplicar {numero1}: '))

    result = multiply(numero1, numero2)

    print(f'el resultado de {numero1} por {numero2} es igual a: {result}')