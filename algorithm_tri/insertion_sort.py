def insertion_sort(input_to_sort):
    length = len(input_to_sort)
    for i in range(1, length):
        key = input_to_sort[i]
        position = i - 1

        while position >= 0 and key < input_to_sort[position]:
            input_to_sort[position + 1] = input_to_sort[position]
            position -= 1

        input_to_sort[position + 1] = key
    return input_to_sort


if __name__ == '__main__':
    array_to_sort = [34, 26, 31, 44, 55, 20]
    output = insertion_sort(array_to_sort)
    print(output)
