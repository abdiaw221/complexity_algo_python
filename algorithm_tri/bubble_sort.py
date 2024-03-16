# bubble sort

def bubble_sort(input_list):
    length_list = len(input_list)
    for i in range(length_list):
        for j in range(0, length_list - i - 1):
            if input_list[j] > input_list[j + 1]:
                # Permute value
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    return input_list


def bubble_sort_swap(input_array):
    swap = True
    input_array_length = len(input_array)
    while swap:
        swap = False
        for i in range(input_array_length - 1):
            if input_array[i] > input_array[i + 1]:
                input_array[i], input_array[i + 1] = input_array[i + 1], input_array[i]
                swap = True
    return input_array


if __name__ == '__main__':
    # Test bubble sort
    init_array = [11, 56, 23, 1, 45, 7, 0, 29, 17, 19, 2]
    output_array = bubble_sort(init_array)
    output_array_swap = bubble_sort_swap(init_array)
    print(output_array)
    print(output_array)
