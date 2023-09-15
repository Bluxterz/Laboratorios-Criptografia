def cifrar_cesar(texto, corrimiento):
    """
    Cifra un texto utilizando el algoritmo César.

    Parámetros:
      texto (str): El texto a cifrar.
      corrimiento (int): El número de posiciones a desplazar.

    Devuelve:
      str: El texto cifrado.
    """

    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = alfabeto.upper()
    mensaje_cifrado = ""

    for letra in texto:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            letra_cifrada = alfabeto[(indice + corrimiento) % 26]
        elif letra in alfabeto_mayusculas:
            indice = alfabeto_mayusculas.index(letra)
            letra_cifrada = alfabeto_mayusculas[(indice + corrimiento) % 26]
        else:
            letra_cifrada = letra

        mensaje_cifrado += letra_cifrada

    return mensaje_cifrado

if __name__ == "__main__":
    texto = input("Introduce el texto a cifrar: ")
    corrimiento = int(input("Introduce el corrimiento: "))

    mensaje_cifrado = cifrar_cesar(texto, corrimiento)
    print("El texto cifrado es:", mensaje_cifrado)
