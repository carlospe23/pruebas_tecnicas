def filtrar_palabras(lista_palabras, n):
    filtradas = {palabra: len(palabra)  for palabra in lista_palabras if len(palabra) > n }
    return filtradas


print(filtrar_palabras(['pedro', 'uno', 'a', 'culo', 'zz'], 3))