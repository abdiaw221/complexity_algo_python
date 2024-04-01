from td_tp_1.exercice_1 import get_occurrence_number, get_occurrence_number_count, first_position_of_occurrence, \
    get_message_with_interval_code_ascii, format_in_majuscule, revert_cast, is_numeric, is_palindrome

if __name__ == '__main__':
    print("TD_TP_1 started.")
    # print("Exercise 1 started.")
    # print("Occurrence number")
    # print("Occurrence with for loop")
    # message = input("Enter a message: ")
    #
    # ch = input("Enter a character: ")
    # if not message or not ch:
    #     print("Message or character cannot be empty.")
    # else:
    #     count = get_occurrence_number(message, ch)
    #     print("Number of occurrences count {} in message : '{}' is {}".format(ch, message, count))
    #
    # print("Second Example")
    #
    # message = input("Enter a message: ")
    # ch = input("Enter a character: ")
    #
    # if not message or not ch:
    #     print("Message or character cannot be empty.")
    # else:
    #     count_count = get_occurrence_number_count(message, ch)
    #     print("Number of occurrences count {} in message : '{}' is {}".format(ch, message, count_count))
    #
    # print("Exercise 2 started.")
    # print("Returner the position of first occurrence")
    # message = input("Enter a message: ")
    # ch = input("Enter a character: ")
    #
    # if not message or not ch:
    #     print("Message or character cannot be empty.")
    # else:
    #     position = first_position_of_occurrence(message, ch)
    #     print("First position of occurrence {} in message : '{}' is {}".format(ch, message, position))
    #
    # print("Exercise 3 started.")
    # print("Returner ASCII code of the interval of two numbers between")
    # number_a = input("Enter a number a: ")
    # number_b = input("Enter a number b: ")
    # message = get_message_with_interval_code_ascii(number_a, number_b)
    # print("Code ASCII between interval {} {}:  is {}".format(number_a, number_b, message))
    #

    # print("N 4 started.")
    # print("Returner chaine in majuscule")
    # message = input("Enter a chaine : ")
    #
    # if not message:
    #     print("No chaine")
    # else:
    #     convert_upper_message = format_in_majuscule(message)
    #     print("Converted message to upper case: ", convert_upper_message)

    # print("N 5 started.")
    # print("Return revert chaine cast")
    # message = input("Enter a chaine : ")
    #
    # if not message:
    #     print("No chaine")
    # else:
    #     convert_cast_message = revert_cast(message)
    #     print("Converted message to revert cast: ", convert_cast_message)

    # print("N 6 started.")
    # print("Return is numeric")
    # chaine_A = "ABCDEFGHIJK"
    # chaine_B = "1245468"
    # chaine_C = "ABA126"
    # # Expected False
    # print(is_numeric(chaine_A))
    # # Expected True
    # print(is_numeric(chaine_B))
    # # Expected False
    # print(is_numeric(chaine_C))
    #
    print("N 7 started.")
    print("Return is palindrome")

    print(is_palindrome("radar"))
    print(is_palindrome("kayak"))
    print(is_palindrome("kayaks"))
    print(is_palindrome("été"))

