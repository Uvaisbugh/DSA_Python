def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#time complexity: O(2^n)
import time
starttime = time.time()
# Example
# print(fibonacci(10))  # Output: 55
# print(fibonacci(20))  # Output: 6765
print(fibonacci(30))  # Output: 832040
# print(fibonacci(40))  # Output: 102334155
endtime = time.time()
print("Time taken:", endtime - starttime)
