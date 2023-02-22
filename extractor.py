
def digits_extracter(text):
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    extracted_digits = []

    for i in text:
        if i in digits:
            extracted_digits.append(i)
    
    return extracted_digits


def digits_sorter(extracted_digits):

    n = len(extracted_digits)
    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)

            if extracted_digits[j] > extracted_digits[j + 1]:
                extracted_digits[j], extracted_digits[j + 1] = extracted_digits[j + 1], extracted_digits[j]

    return "".join(extracted_digits)


if __name__ == '__main__':

    text = '3ha4sa2df3as5f3ad5a4sdf8df6'

    extracted_digits = digits_extracter(text)
    sorted_digits = digits_sorter(extracted_digits)

    result = sum(int(digit) for digit in sorted_digits)

    print(f'La cadena ingresada fue {text}')

    print(f'Los digitos extraidos fueron {extracted_digits}')

    print(f'los digitos ordenados son {sorted_digits}')

    print(f'la suma de todos los digitos es {result}')


