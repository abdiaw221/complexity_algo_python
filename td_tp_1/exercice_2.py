# Cryptographic : Code de Vigenère
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


if __name__ == '__main__':
    texts = "Hey Hey, cet été là, le gang des niçois à été arrêté!"
    print(en_majuscule(texts))
