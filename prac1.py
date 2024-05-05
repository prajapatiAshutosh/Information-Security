import numpy as np

class MonoalphabeticCipher:
    def __init__(self):
        self.key = None

    def generate_key(self):
        """Generate a random permutation of integers from 0 to 25."""
        self.key = np.random.permutation(26)

    def encrypt(self, plaintext):
        """Encrypt the plaintext using the generated key."""
        if not self.key:
            self.generate_key()

        ciphertext = ""
        for char in plaintext.lower():
            if char.isalpha():
                index = ord(char) - ord('a')
                encrypted_char = chr(self.key[index] + ord('a'))
                ciphertext += encrypted_char
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        """Decrypt the ciphertext using the generated key."""
        if not self.key:
            raise ValueError("Key not generated yet.")

        plaintext = ""
        for char in ciphertext.lower():
            if char.isalpha():
                index = self.key.tolist().index(ord(char) - ord('a'))
                decrypted_char = chr(index + ord('a'))
                plaintext += decrypted_char
            else:
                plaintext += char
        return plaintext

def main():
    cipher = MonoalphabeticCipher()
    plaintext = input("Enter a plaintext in alphabets only: ")
    encrypted_text = cipher.encrypt(plaintext)
    print("Encrypted:", encrypted_text)
    decrypted_text = cipher.decrypt(encrypted_text)
    print("Decrypted:", decrypted_text)

if __name__ == "__main__":
    main()
