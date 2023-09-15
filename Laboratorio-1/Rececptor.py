import operator
from scapy.all import ICMP, sniff
import time

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
    puntaje = 0
    conteo_letras = {}

    for letra in texto_plano:
        if letra.isalpha():
            conteo_letras[letra.lower()] = conteo_letras.get(letra.lower(), 0) + 1

    for letra, frecuencia in frecuencias_espanol.items():
        if letra in conteo_letras:
            puntaje += conteo_letras[letra] * frecuencia

    return puntaje

def descifrar_cesar(texto_cifrado, desplazamiento):
    texto_plano = ""
    for letra in texto_cifrado:
        if letra.isalpha():
            if letra.isupper():
                texto_plano += chr((ord(letra) - desplazamiento - 65 + 26) % 26 + 65)
            else:
                texto_plano += chr((ord(letra) - desplazamiento - 97 + 26) % 26 + 97)
        else:
            texto_plano += letra

    return texto_plano

def packet_handler(packet_list):
    # Ordenar los paquetes por tiempo de llegada
    packet_list.sort(key=lambda pkt: pkt.time)

    # Extraer el ciphertext de todos los paquetes en una cadena de texto
    ciphertext = b"".join([pkt[ICMP].load for pkt in packet_list]).decode('utf-8')

    puntajes = {}
    for corrimiento in range(27):  # Corrimiento comienza desde 0
        mensaje_descifrado = descifrar_cesar(ciphertext, corrimiento)
        puntaje = calcular_puntaje(mensaje_descifrado)
        puntajes[corrimiento] = puntaje
        
        if puntaje > 0.05:  # Cambia el umbral según tus necesidades
            mensaje_descifrado = mensaje_descifrado.replace(
                str(puntaje), "\033[32m" + str(puntaje) + "\033[0m"
            )
        
        print(f"Corrimiento {corrimiento}: {mensaje_descifrado}")

    mejor_corrimiento = max(puntajes.items(), key=operator.itemgetter(1))[0]
    print("\nMejor respuesta posible:")
    mensaje_descifrado = descifrar_cesar(ciphertext, mejor_corrimiento)
    mensaje_descifrado = mensaje_descifrado.replace(
        str(mejor_corrimiento), "\033[32m" + str(mejor_corrimiento) + "\033[0m"
    )
    print(f"\033[92mCorrimiento {mejor_corrimiento}: {mensaje_descifrado}\033[0m")


# Sniff para capturar paquetes ICMP
packet_list = []
timeout = 5

print("Esperando paquetes ICMP...")
while True:
    pkt = sniff(filter="icmp", count=1, timeout=timeout)
    
    if pkt:
        packet_list.append(pkt[0])
        print("Recibiendo paquete...")
        ciphertext = pkt[0][ICMP].load.decode('utf-8')
        print(f"Cifrado recibido: {ciphertext}")

    else:
        break

packet_handler(packet_list)