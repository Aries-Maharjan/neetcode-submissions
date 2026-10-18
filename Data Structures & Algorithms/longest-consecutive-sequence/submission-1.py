class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        longest = 0
        for n in num:
            if n - 1 not in num:
                curr = n
                length = 1
                while curr+1 in num:
                    curr+=1
                    length+=1
                longest =max(longest,length)
        return longest



        