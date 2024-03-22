def get_occurrence_number(chaine, character):
    number = 0;
    for letter in chaine:
        if letter == character:
            number += 1
    return number


def get_occurrence_number_count(chaine, character):
    return chaine.count(character)


def first_position_of_occurrence(chaine, character):
    for i, letter in enumerate(chaine):
        if letter == character:
            return i
    return -1


def get_message_with_interval_code_ascii(number_1, number_2):
    try:
        number_1 = int(number_1)
        number_2 = int(number_2)
    except ValueError:
        return "Input values must be integers."

    message = ""
    if number_1 < number_2:
        for i in range(number_1, number_2 + 1):
            message += "{} - ".format(chr(i))
    else:
        message = "{} is less than {}".format(number_2, number_1)
    return message


def format_in_majuscule(chaine):
    return chaine.upper()
