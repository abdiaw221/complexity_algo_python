def vigenere_cipher(text, key, mode='encrypt'):
    shift = len(text) % 16
    encrypted_text = ''
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            if mode == 'encrypt':
                shift = ord(key[i % key_length].upper()) - ord('A')
            elif mode == 'decrypt':
                shift = - (ord(key[i % key_length].upper()) - ord('A'))
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text


def main():
    text = input("Enter the text: ")
    key = input("Enter the key: ")
    mode = input("Encrypt or Decrypt? (e/d): ").lower()
    if mode == 'e':
        encrypted_text = vigenere_cipher(text, key)
        print("Encrypted text:", encrypted_text)
    elif mode == 'd':
        decrypted_text = vigenere_cipher(text, key, 'decrypt')
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
