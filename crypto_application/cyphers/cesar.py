def cesar_cipher_encode(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            position = permute_message(char, shifted)
            encrypted_text += chr(position)
        else:
            encrypted_text += char
    return encrypted_text


def cesar_decipher_decode(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            position = permute_message(char, shifted)
            decrypted_text += chr(position)
        else:
            decrypted_text += char
    return decrypted_text


def permute_message(ciphertext, shifted):
    if ciphertext.islower():
        if shifted > ord('z'):
            shifted -= 26
        elif shifted < ord('a'):
            shifted += 26
    elif ciphertext.isupper():
        if shifted > ord('Z'):
            shifted -= 26
        elif shifted < ord('A'):
            shifted += 26
    return shifted


def main():
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted_text = cesar_cipher_encode(text, shift)
    print("Encrypted text:", encrypted_text)
    decrypted_text = cesar_decipher_decode(encrypted_text, shift)
    print("Decrypted text:", decrypted_text)


if __name__ == "__main__":
    # Documentation https://etablissementbertrandeborn.net/IMG/pdf/indice9_maths.pdf
    main()
