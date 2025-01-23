#Palindrome Pairs
from typing import List

class Solution1:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        '''
        Finds all the pairs of palindromic strings that can be formed from
        the given list of words.
        
        Args:
            words (List[str]): A list of strings.
        
        Returns:
            List[List[int]]: A list of pairs of indices of words that form
            a palindromic pair.
            
        '''
        d = {w: i for i, w in enumerate(words)}
        ans = []
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                a, b = w[:j], w[j:]
                ra, rb = a[::-1], b[::-1]
                if ra in d and d[ra] != i and b == rb:
                    ans.append([i, d[ra]])
                if j and rb in d and d[rb] != i and a == ra:
                    ans.append([d[rb], i])
        return ans
    
    
    