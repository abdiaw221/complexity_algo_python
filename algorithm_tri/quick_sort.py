# Quick sort
def quick_sort(array_to_sort):
    # the recursive stop condition
    if not array_to_sort:
        return []
    else:
        # get the last element of the array (pivot)
        pivot = array_to_sort[-1]

        # array of smaller values of the pivot
        array_of_smaller_values = [value for value in array_to_sort if value < pivot]

        # array of bigger values of the pivot
        array_of_bigger_values = [value for value in array_to_sort[:-1] if value >= pivot]

        # we return the current iteration with a new array
        # smaller values at the beginning, pivot in the middle, bigger values in the end
        return quick_sort(array_of_smaller_values) + [pivot] + quick_sort(array_of_bigger_values)


# Test quick_sort
if __name__ == '__main__':
    init_array = [2018, 1998, 1986, 2020, 2006]
    output_array = quick_sort(init_array)
    print(output_array)
