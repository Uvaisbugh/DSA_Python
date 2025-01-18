# https://leetcode.com/problems/continuous-subarray-sum/

from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        Determines if the array contains a continuous subarray of at least size 2 
        whose elements sum up to a multiple of the given integer k.

        Args:
        nums (List[int]): A list of integers.
        k (int): An integer to check the multiple of.

        Returns:
        bool: True if such a subarray exists, False otherwise.
        """

        sumIndexDic = {0 : -1}    # nums = [14, 7]; k = 7
        curSum = 0
        
        for i in range(len(nums)):
            curSum += nums[i]
            curSum = curSum % k
            
            if curSum in sumIndexDic:
                if i - sumIndexDic[curSum] >= 2: 
                    return True
            else:
                sumIndexDic[curSum] = i
        
        return False