class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            # most we've got so far is either this + rob1 (the one before the one before) or just rob2 (the one before)
            temp = max(n + rob1, rob2)

            rob1 = rob2
            rob2 = temp
        
        return rob2