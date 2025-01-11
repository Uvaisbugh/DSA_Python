def bubble_sort(arr):
    '''
    Function to sort a list using bubble sort algorithm
    '''
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#time complexity: O(n^2)
# Example
import random
import time
start_time = time.time()
unsorted_list = random.sample(range(1, 100), 10)
sorted_list = bubble_sort(unsorted_list)
print("Sorted list:", sorted_list)
end_time = time.time()
print("Time taken:", end_time - start_time)