import subprocess
import time
from scapy.all import IP, ICMP, send

def separar_caracteres_enviar_ping(texto, ip_destino):
    for caracter in texto:
        # Convierte el carácter a su valor ASCII
        valor_ascii = ord(caracter)
        
        # Modifica el bit menos significativo a 0 (paridad)
        valor_modificado = valor_ascii & 0b11111110
        
        print(f"Enviando caracter: {caracter}")
        
        # Construye el paquete ICMP con el valor modificado en el byte menos significativo del contador
        paquete_icmp = IP(dst=ip_destino)/ICMP()/bytes([valor_modificado])
        
        # Envía el paquete ICMP
        send(paquete_icmp)
        
        # Espera un momento antes de enviar el siguiente ping
        time.sleep(0.1)

# Obtén el texto a procesar y la dirección IP de destino
texto = input("Introduce el texto para procesar: ")
ip_destino = input("Introduce la dirección IP de destino para los paquetes ICMP: ")

# Llama a la función para separar los caracteres y enviar los paquetes ICMP
separar_caracteres_enviar_ping(texto, ip_destino)

print("Paquetes ICMP enviados con los caracteres modificados.")
