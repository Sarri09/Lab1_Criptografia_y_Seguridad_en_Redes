import sys

def cifrar_cesar(texto, corrimiento):
    resultado = []

    for caracter in texto:
        if caracter.isalpha():
            # Determinar si es una letra mayúscula o minúscula
            if caracter.isupper():
                inicio = ord('A')
            else:
                inicio = ord('a')
            
            # Aplicar el corrimiento
            nuevo_codigo = (ord(caracter) - inicio + corrimiento) % 26 + inicio
            nuevo_caracter = chr(nuevo_codigo)
            resultado.append(nuevo_caracter)
        else:
            resultado.append(caracter)
    
    return ''.join(resultado)

if len(sys.argv) != 3:
    sys.exit(1)

texto_original = sys.argv[1]
corrimiento = int(sys.argv[2])

texto_cifrado = cifrar_cesar(texto_original, corrimiento)
print(texto_cifrado)

