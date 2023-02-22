
text = 'Bienvenidos a SysCursos'

def invert_text(text):
    
    reverse = ''
    for i in range(1, len(text) + 1):
        reverse += text[-i]

    return reverse

result = invert_text(text)

print(result)