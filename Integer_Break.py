# https://leetcode.com/problems/integer-break/


# Method 1 ------  Memoization  -------
# https://youtu.be/in6QbUPMJ3I
class Solution:
    def integerBreak(self, n):
        """
        Breaks an integer n into the sum of at least two positive integers, aiming to 
        maximize the product of those integers. Uses a memoization approach to store 
        intermediate results and avoid redundant computations.

        Args:
        n (int): The integer to be broken into a sum of at least two positive integers.

        Returns:
        int: The maximum product achievable by breaking the integer n.
        """

        dp = {1 : 1}
        
        def dfs(num):
            if num in dp:
                return dp[num]
            
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num], val)
            return dp[num]
        
        return dfs(n)

# Method 2 -------  Dynamic Programming -------
class Solution(object):
    def integerBreak(self, n):
        dp = [None, 1]
        for m in range (2, n + 1):
            j = m - 1
            i = 1
            max_product = 0
            while i <= j:
                max_product = max(max_product, max(i, dp[i]) * max(j, dp[j]))
                j -= 1
                i += 1
            dp.append(max_product)
        return dp[n]
# Time: O(n^2)
# Space: O(n)