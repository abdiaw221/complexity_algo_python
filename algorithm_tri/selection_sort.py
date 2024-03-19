def selection_sort(array_to_sort):
    length = len(array_to_sort)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if array_to_sort[j] < array_to_sort[min_index]:
                min_index = j
        if min_index != i:
            array_to_sort[i], array_to_sort[min_index] = array_to_sort[min_index], array_to_sort[i]

    return array_to_sort


if __name__ == '__main__':
    input_array = [12, 23, 17, 45, 2, 10, 0, 26, 34, 3]
    output_array = selection_sort(input_array)
    print(output_array)
