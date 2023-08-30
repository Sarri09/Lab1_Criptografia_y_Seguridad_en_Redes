import sys
from scapy.all import rdpcap

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def evaluate_text(text):
    # Definir la frecuencia de letras en español aquí
    letter_frequency = {
        'a': 11.72, 'b': 2.22, 'c': 4.68, 'd': 5.86, 'e': 13.68, 'f': 0.69, 'g': 1.01,
        'h': 0.70, 'i': 6.25, 'j': 0.44, 'k': 0.02, 'l': 4.97, 'm': 3.15, 'n': 6.71,
        'o': 8.68, 'p': 2.51, 'q': 0.88, 'r': 6.87, 's': 7.98, 't': 4.63, 'u': 3.93,
        'v': 0.90, 'w': 0.02, 'x': 0.22, 'y': 0.90, 'z': 0.52
    }
    
    score = 0
    for char in text.lower():
        if char in letter_frequency:
            score += letter_frequency[char]
    return score

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decrypt_icmp_payload.py <path_to_pcapng>")
        sys.exit(1)
    
    pcap_file = sys.argv[1]
    packets = rdpcap(pcap_file)
    
    icmp_payloads = []
    for packet in packets:
        if packet.haslayer("ICMP"):
            icmp_payload = packet.getlayer("ICMP").load
            if icmp_payload:
                first_char = chr(icmp_payload[0])
                icmp_payloads.append(first_char)
    
    encrypted_message = "".join(icmp_payloads)
     
    best_score = 0
    best_shift = 0
    best_message = ""
    
    for shift in range(26):
        decrypted_text = caesar_decrypt(encrypted_message, shift)
        score = evaluate_text(decrypted_text)
        
        if score > best_score:
            best_score = score
            best_shift = shift
            best_message = decrypted_text
     
    for shift in range(26):
        decrypted_text = caesar_decrypt(encrypted_message, shift)
        score = evaluate_text(decrypted_text)
        if score == best_score:
            print("\033[32m[{}] {}\033[0m".format(shift, decrypted_text))  # Marcar en verde la opción más probable
        else:
            print("[{}] {}".format(shift, decrypted_text))

