

def key_schedule (S, key):
    key_length = len(key)
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]

def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield format(K, '02X')  # Convertir a hexadecimal y rellenar con ceros si es necesario

def RC4(key):
    S = [i for i in range(256)]
    key_schedule(S, key)
    return PRGA(S)

def encrypt(text, key):
    key_bytes = [ord(char) for char in key]
    keystream_generator = RC4(key_bytes)

    encrypted_text = ""
    for char in text:
        keystream_byte = next(keystream_generator)
        encrypted_char = ord(char) ^ int(keystream_byte, 16)
        encrypted_text += format(encrypted_char, '02X')  # Convertir a hexadecimal y rellenar con ceros si es necesario

    return encrypted_text

# Ejemplo de uso:
key = "Secret"
plaintext = "Attack at dawn"

ciphertext = encrypt(plaintext, key)
print("Texto cifrado en hexadecimal:", ciphertext)