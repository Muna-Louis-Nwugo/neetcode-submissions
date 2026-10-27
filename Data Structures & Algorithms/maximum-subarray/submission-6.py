class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        best = float('-inf')

        for num in nums:
            if total < 0:
                total = num
            else: 
                total += num

            if total > best:
                best = total 
                


        return best