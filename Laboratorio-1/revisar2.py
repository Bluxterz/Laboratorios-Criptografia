import operator
from scapy.all import *
from scapy.layers.inet import *
import argparse

# Frecuencias de letras para el idioma español
frecuencias_espanol = {
    'a': 0.115,
    'b': 0.022,
    'c': 0.047,
    'd': 0.057,
    'e': 0.141,
    'f': 0.009,
    'g': 0.01,
    'h': 0.007,
    'i': 0.062,
    'j': 0.004,
    'k': 0.001,
    'l': 0.049,
    'm': 0.031,
    'n': 0.067,
    'o': 0.086,
    'p': 0.025,
    'q': 0.009,
    'r': 0.068,
    's': 0.08,
    't': 0.05,
    'u': 0.024,
    'v': 0.009,
    'w': 0.001,
    'x': 0.002,
    'y': 0.01,
    'z': 0.005
}

def calcular_puntaje(texto_plano):
    """Calcula el puntaje de un texto plano basado en las frecuencias de letras del idioma español."""
    puntaje = 0
    conteo_letras = {}
    for letra in texto_plano:
        if letra.isalpha():
            if letra.lower() in conteo_letras:
                conteo_letras[letra.lower()] += 1
            else:
                conteo_letras[letra.lower()] = 1

    for letra, frecuencia in frecuencias_espanol.items():
        if letra in conteo_letras:
            puntaje += conteo_letras[letra] * frecuencia

    return puntaje

def descifrar_cesar(texto_cifrado):
    puntajes = {}
    for desplazamiento in range(26):
        texto_plano = ""
        for letra in texto_cifrado:
            if letra.isalpha():
                if letra.isupper():
                    texto_plano += chr((ord(letra) - desplazamiento - 65) % 26 + 65)
                else:
                    texto_plano += chr((ord(letra) - desplazamiento - 97) % 26 + 97)
            else:
                texto_plano += letra
        puntaje = calcular_puntaje(texto_plano)
        puntajes[desplazamiento] = puntaje
        print(f"Desplazamiento {desplazamiento}: {texto_plano}")

    mejor_desplazamiento = max(puntajes.items(), key=operator.itemgetter(1))[0]
    print("\nMejor respuesta posible:")
    print(f"\033[92mDesplazamiento {mejor_desplazamiento}: {cesar_desplazado(texto_cifrado, mejor_desplazamiento)}\033[0m")

def cesar_desplazado(texto_cifrado, desplazamiento):
    """Realiza un desplazamiento César en un texto cifrado por una cantidad dada de posiciones."""
    texto_plano = ""
    for letra in texto_cifrado:
        if letra.isalpha():
            if letra.isupper():
                texto_plano += chr((ord(letra) - desplazamiento - 65) % 26 + 65)
            else:
                texto_plano += chr((ord(letra) - desplazamiento - 97) % 26 + 97)
        else:
            texto_plano += letra
    return texto_plano

def leer_archivo_pcapng(nombre_archivo):
    paquetes = rdpcap(nombre_archivo)
    paquetes_icmp = [p for p in paquetes if ICMP in p]
    dict_id = {}
    for paquete in paquetes_icmp:
        if paquete[ICMP].id in dict_id:
            dict_id[paquete[ICMP].id] += paquete[Raw].load.decode('utf-8')[0]
        else:
            dict_id[paquete[ICMP].id] = paquete[Raw].load.decode('utf-8')[0]
    return dict_id

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lee un archivo pcapng y extrae el primer carácter de cada campo de datos de paquetes ICMP agrupados por ID.')
    parser.add_argument('nombre_archivo', help='Ruta al archivo pcapng')
    args = parser.parse_args()

    dict_id = leer_archivo_pcapng(args.nombre_archivo)
    for clave, valor in dict_id.items():
        print(f'ID: {clave}, Datos: {valor}')
        descifrar_cesar(valor)
