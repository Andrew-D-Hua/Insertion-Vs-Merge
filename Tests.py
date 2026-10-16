import random
import timeit

# Insertion Sort from https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/
def Insertion_Sort(array):
    for number_idx in range(1, len(array)):
        current_key = array[number_idx]
        past_index = number_idx - 1

        # Iterates through to find where to insert
        while past_index >= 0 and current_key < array[past_index]:
            array[past_index + 1] = array[past_index]
            past_index -=1
        array[past_index + 1] = current_key

    return array

# -------------------------------------------------- #

# Merge Sort from https://www.w3schools.com/python/python_dsa_mergesort.asp
def Merge_Sort(array):
    # Base Case
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left_half = array[0:middle]
    right_half = array[middle:]

    # Sort left and right half
    sorted_left = Merge_Sort(left_half)
    sorted_right = Merge_Sort(right_half)

    sorted_list = helper_merge(sorted_left,sorted_right)
    return sorted_list


def helper_merge(sorted_left_half, sorted_right_half):
    left_index = 0
    right_index = 0

    sorted_list = []

    left_length = len(sorted_left_half)
    right_length = len(sorted_right_half)

    while left_index < left_length and right_index < right_length:
        left_item = sorted_left_half[left_index]
        right_item = sorted_right_half[right_index]

        if left_item <= right_item:
            sorted_list.append(left_item)
            left_index+= 1
        else:
            sorted_list.append(right_item)
            right_index += 1

    sorted_list.extend(sorted_left_half[left_index:])
    sorted_list.extend(sorted_right_half[right_index:])

    return sorted_list

def create_random_list(size):
    random_list = [i for i in range(size)]
    random.shuffle(random_list)
    return random_list

# -------------------------------------------------- #

# Data collection functions
def time_test(trial_num, repeats, size):
    trial_number = trial_num
    repeats_per_list = repeats
    list_size = size

    insertion_total = 0
    merge_total = 0
    for i in range(trial_number):
        random_list = create_random_list(list_size)

        insertion_elapsed = timeit.timeit(lambda: Insertion_Sort(random_list.copy()), number = repeats_per_list)
        insertion_total += insertion_elapsed

        merge_elapsed_1 = timeit.timeit(lambda: Merge_Sort(random_list.copy()), number = repeats_per_list)
        merge_total += merge_elapsed_1

    total_runs = trial_number * repeats_per_list
    average_insertion = (insertion_total/total_runs)
    average_merge = (merge_total/total_runs)

    improvement_percentage = (average_merge - average_insertion) / average_merge * 100
    improvement_percentage = round(improvement_percentage, 2)

    return improvement_percentage

# -------------------------------------------------- #
if __name__ == "__main__":
    # Check random list of 1
    trial_number = 1000
    repeats_per_list = 100
    input_size = 1

    input_1_test = time_test(trial_number, repeats_per_list, input_size)
    print(f"Insertion provided a {input_1_test}% improvement compared to Merge sort when n = {input_size}" )

    # Check random list of 2
    trial_number = 1000
    repeats_per_list = 100
    input_size = 2

    input_2_test = time_test(trial_number, repeats_per_list, input_size)
    print(f"Insertion provided a {input_2_test}% improvement compared to Merge sort when n = {input_size}" )

    # Check random list of 5
    trial_number = 1000
    repeats_per_list = 100
    input_size = 5

    input_5_test = time_test(trial_number, repeats_per_list, input_size)
    print(f"Insertion provided a {input_5_test}% improvement compared to Merge sort when n = {input_size}" )


    # Check random list of 10 
    trial_number = 1000
    repeats_per_list = 100
    input_size = 10

    input_10_test = time_test(trial_number, repeats_per_list, input_size)
    print(f"Insertion provided a {input_10_test}% improvement compared to Merge sort when n = {input_size}" )


    # Check random list of 100 
    trial_number = 1000
    repeats_per_list = 100
    input_size = 100

    input_100_test = time_test(trial_number, repeats_per_list, input_size)
    print(f"Insertion provided a {input_100_test}% improvement compared to Merge sort when n = {input_size}" )


    # Check random list of 50 
    trial_number = 1000
    repeats_per_list = 100
    input_size = 50

    input_50_test = time_test(trial_number, repeats_per_list, input_size)
    print(f"Insertion provided a {input_50_test}% improvement compared to Merge sort when n = {input_size}" )

    
    # Check random list of 60 
    trial_number = 1000
    repeats_per_list = 100
    input_size = 60

    input_60_test = time_test(trial_number, repeats_per_list, input_size)
    print(f"Insertion provided a {input_60_test}% improvement compared to Merge sort when n = {input_size}" )

    # Check random list of 55 
    trial_number = 1000
    repeats_per_list = 100
    input_size = 55

    input_55_test = time_test(trial_number, repeats_per_list, input_size)
    print(f"Insertion provided a {input_55_test}% improvement compared to Merge sort when n = {input_size}" )

    # Check random list of 58 
    trial_number = 10000
    repeats_per_list = 100
    input_size = 58

    input_58_test = time_test(trial_number, repeats_per_list, input_size)
    print(f"Insertion provided a {input_58_test}% improvement compared to Merge sort when n = {input_size}" )

    # Check random list of 1000 (for fun)
    trial_number = 100
    repeats_per_list = 10
    input_size = 1000

    input_1000_test = time_test(trial_number, repeats_per_list, input_size)
    print(f"Insertion provided a {input_1000_test}% improvement compared to Merge sort when n = {input_size}" )

    



