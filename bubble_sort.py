def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Example usage:
unsorted_list = [5, 2, 9, 1, 5]
sorted_list = bubble_sort(unsorted_list)
print("Sorted list:", sorted_list)