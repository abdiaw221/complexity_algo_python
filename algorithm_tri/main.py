from time import time
from random import randint
from algorithm_tri.bubble_sort import bubble_sort
from algorithm_tri.fusion_sort import merge_sort
from algorithm_tri.insertion_sort import insertion_sort
from algorithm_tri.quick_sort import quick_sort
from algorithm_tri.selection_sort import selection_sort
import matplotlib.pyplot as plt


def generate_random_list(_size):
    return [randint(0, _size) for _ in range(_size)]


def measure_time(algorithm, arr):
    start_time = time()
    algorithm(arr)
    end_time = time()
    return end_time - start_time


if __name__ == '__main__':
    print("Sorting algorithm")

    list_sizes = [1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 7000, 8000]

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort
    }

    execution_times = {algo_name: [] for algo_name in algorithms.keys()}

    for size in list_sizes:
        random_list = generate_random_list(size)
        for algo_name, algo_func in algorithms.items():
            arr_copy = random_list.copy()
            execution_time = measure_time(algo_func, arr_copy)
            execution_times[algo_name].append(execution_time)
            print(f"Execution time of {algo_name}: {execution_time} sec on a list of size {size}")

    plt.figure(figsize=(10, 6))

    # Plotting
    for algo_name, times in execution_times.items():
        plt.plot(list_sizes, times, label=algo_name)

    plt.title('Comparaison des temps d\'exécution des algorithmes de tri')
    plt.xlabel('Taille de la liste')
    plt.ylabel('Temps d\'exécution (s)')
    plt.legend()
    plt.grid(True)
    plt.show()

    #
    # # bubble sort
    # names = ["Bubble Sort"]
    # start = time()
    # sorted_array_bubble = bubble_sort(generate_array)
    # end = time()
    # time_bubble = end - start
    # print(f"Execution time of bubble sort: {time_bubble} sec")
    #
    # # merge sort
    # names.append("Merge Sort")
    # start = time()
    # sorted_array_merge = merge_sort(generate_array)
    # end = time()
    # time_merge = end - start
    # print(f"Execution time of merge sort: {time_merge} sec")
    #
    # # insertion sort
    # names.append("Insertion Sort")
    # start = time()
    # sorted_array_insertion = insertion_sort(generate_array)
    # end = time()
    # time_insertion = end - start
    # print(f"Execution time of insertion sort: {time_insertion} sec")
    #
    # # insertion sort
    # names.append("Quick Sort")
    # start = time()
    # sorted_array_quick = quick_sort(generate_array)
    # end = time()
    # time_quick = end - start
    # print(f"Execution time of insertion sort: {time_quick} sec")
    #
    # # quick sort
    # names.append("Selection Sort")
    # start = time()
    # sorted_array_selection = selection_sort(generate_array)
    # end = time()
    # time_selection = end - start
    # print(f"Execution time of selection sort: {time_selection} sec")
