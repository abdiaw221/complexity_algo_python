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


if __name__ == '__main__':
    texts = "Hey Hey, cet été là, le gang des niçois à été arrêté!"
    print(en_majuscule(texts))
    print(en_majuscule_only(texts))
