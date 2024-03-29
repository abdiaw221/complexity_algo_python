from td_tp_1.exercice_1 import get_occurrence_number, get_occurrence_number_count, first_position_of_occurrence, \
    get_message_with_interval_code_ascii

if __name__ == '__main__':
    print("TD_TP_1 started.")
    print("Exercise 1 started.")
    print("Occurrence number")
    print("Occurrence with for loop")
    message = input("Enter a message: ")

    ch = input("Enter a character: ")
    if not message or not ch:
        print("Message or character cannot be empty.")
    else:
        count = get_occurrence_number(message, ch)
        print("Number of occurrences count {} in message : '{}' is {}".format(ch, message, count))

    print("Second Example")

    message = input("Enter a message: ")
    ch = input("Enter a character: ")

    if not message or not ch:
        print("Message or character cannot be empty.")
    else:
        count_count = get_occurrence_number_count(message, ch)
        print("Number of occurrences count {} in message : '{}' is {}".format(ch, message, count_count))

    print("Exercise 2 started.")
    print("Returner the position of first occurrence")
    message = input("Enter a message: ")
    ch = input("Enter a character: ")

    if not message or not ch:
        print("Message or character cannot be empty.")
    else:
        position = first_position_of_occurrence(message, ch)
        print("First position of occurrence {} in message : '{}' is {}".format(ch, message, position))

    print("Exercise 3 started.")
    print("Returner ASCII code of the interval of two numbers between")
    number_a = input("Enter a number a: ")
    number_b = input("Enter a number b: ")
    message = get_message_with_interval_code_ascii(number_a, number_b)
    print("Code ASCII between interval {} {}:  is {}".format(number_a, number_b, message))
