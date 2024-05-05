import numpy as np

def generate_key(shift=0):
    alphabet = np.array(
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z'])

    a_to_int = 97
    arr = np.array(range(0, 26))
    arr = (arr + shift) % 26  # Applying modulo 26
    keys = []

    for i in arr:
        keys.append(chr(i + a_to_int))

    return keys

def encryption(plain_text, key):
    p_arr = ''.join(plain_text.split())
    data = list(p_arr)
    cipher = []

    for i in data:
        cipher.append(key[ord(i) - 97])
    return cipher

def decryption(cipher_text, key):
    cipher = cipher_text
    plain_text = []

    for i in cipher:
        plain_text.append(key.index(i))
    return plain_text

def main():
    keys = generate_key(3)  # Shifting letters by -3 positions
    message = input("Give a plain text in alphabet only: ")
    cipher = encryption(message, keys)
    print("Encrypted message:", ''.join(cipher))

    # Decrypting the cipher text
    d_key = generate_key(3)  # Generating decryption key with +3 shift
    plain_text = decryption(cipher, d_key)
    print("Decrypted message:", ''.join(chr(i + 97) for i in plain_text))

if __name__ == "__main__":
    main()
