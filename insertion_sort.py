def inserton_sort(arr):
    '''insertion sort algorithm'''
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Worst Case: O(n²), when the array is sorted in reverse order.
# Best Case: O(n), when the array is already sorted.
# Average Case: O(n²), when the array is in a random order.

import random
import time
start_time = time.time()
unsorted_list = random.sample(range(1, 100), 10)
sorted_list = inserton_sort(unsorted_list)
print("Sorted list:", sorted_list)
end_time = time.time()
print("Time taken:", end_time - start_time, "seconds")