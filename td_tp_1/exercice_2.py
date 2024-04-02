# Cryptographic : Code de Vigenère
from unidecode import unidecode
import re


def en_majuscule(chaine):
    chaine_majuscule = ""
    for character in chaine:
        if 'a' <= character <= 'z':
            chaine_majuscule += chr(ord(character) - 32)
        elif 'à' <= character <= 'ÿ':
            chaine_majuscule += chr(ord(character) - 32)
        elif character == 'ç':
            chaine_majuscule += 'Ç'
        else:
            chaine_majuscule += character
    return chaine_majuscule


def del_special_character(chaine):
    chaine_propre = re.sub(r'[^a-zA-Z]', '', chaine)
    return chaine_propre


def en_majuscule_only(chaine):
    majuscule = en_majuscule(chaine)
    only_majuscule_only = unidecode(majuscule)
    del_special_characters = del_special_character(only_majuscule_only)
    return del_special_characters


def vigenere_encode(chaine, key):
    encrypted_text = ''
    key_length = len(key)
    for i, char in enumerate(chaine):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text


def vigenere_encode_rec(chaine, key, index=0, encrypted_text=''):
    if index == len(chaine):
        return encrypted_text

    char = chaine[index]
    key_length = len(key)
    if char.isalpha():
        shift = ord(key[index % key_length]) - ord('A')
        encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        encrypted_text += char

    return vigenere_encode_rec(chaine, key, index + 1, encrypted_text)


def vigenere_decode(encrypted_text, key):
    decoded_text = ''
    key_length = len(key)
    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            shift = -ord(key[i % key_length]) - ord('A')
            decoded_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            decoded_text += char
    return decoded_text


if __name__ == '__main__':
    texts = "Hey Hey, cet été là, le gang des niçois à été arrêté!"
    text_en_majuscule = en_majuscule(texts)
    print(text_en_majuscule)
    text_en_majuscule_only = en_majuscule_only(text_en_majuscule)
    print(text_en_majuscule_only)
    vigenere_encoded = vigenere_encode(text_en_majuscule_only, 'ABC')
    print(vigenere_encoded)
    print("Question 11 : calcul de la complexité de la fonction vigenere_encode")
    vigenere_encode_recursive = vigenere_encode_rec(text_en_majuscule_only, 'ABC')
    print(vigenere_encode_recursive)
    print("Decrypted Text Encoded")
    decrypted_text = vigenere_decode(vigenere_encoded, 'ABC')
    print(decrypted_text)
    # Pour le choix du clé, afin que le message soit plus robuste:

    # 1 - Aussi longue que le message : La longueur de la clé doit être au moins égale à celle du message.
    # Cela empêche les attaquants de deviner des parties de la clé en fonction du contexte du message.

    # 2 - Aléatoire et suffisamment complexe : La clé doit être générée de manière aléatoire et contenir un mélange
    # de lettres majuscules, de chiffres et de caractères spéciaux.
    # Cela rendra le processus de cryptanalyse plus difficile pour les attaquants.

    # 3 - Non basée sur un mot du dictionnaire : Évitez d'utiliser des mots du dictionnaire
    # ou des phrases courantes comme clé. Les attaquants utilisent souvent des techniques
    # de force brute ou des attaques par dictionnaire pour casser de telles clés.

    # 4 - Utilisée une seule fois (pour le chiffrement d'un seul message) :
    # Pour une sécurité maximale, utilisez la clé une seule fois (principe de l'usage unique),
    # puis détruisez-la après usage. Cela empêche les attaques de répétition et améliore la sécurité globale.

    # 5 - Changeante et régulièrement mise à jour : Si vous utilisez le chiffrement de Vigenère pour plusieurs messages,
    # il est recommandé de changer la clé régulièrement.
    # Une pratique courante est de changer la clé après chaque utilisation ou après un certain nombre de messages.
