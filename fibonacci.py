def fibonacci(n):
    """
    Computes the nth Fibonacci number using recursion.

    Args:
    n (int): The position in the Fibonacci sequence to compute. Must be a non-negative integer.

    Returns:
    int: The nth Fibonacci number.

    Note:
    This function has an exponential time complexity of O(2^n) due to its recursive nature.
    """

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
print(fibonacci(5))  # Output: 832040
# print(fibonacci(40))  # Output: 102334155
endtime = time.time()
print("Time taken:", endtime - starttime)
