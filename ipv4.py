from scapy.all import IP, ICMP, send
import sys
import random

# Definir la secuencia de datos aleatorios
random_data = bytes([random.randint(0, 255) for _ in range(37)])

def send_icmp_packets(text):
    for char in text:
        data = char.encode() + b'\x00' * 10 # 10 espacios después del caracter
        data += random_data  # Agregar la secuencia de datos aleatorios definida
        packet = IP(dst="172.16.32.16") / ICMP() / data
        send(packet)

if len(sys.argv) != 2:
    sys.exit(1)

text_to_send = sys.argv[1]
send_icmp_packets(text_to_send)

