class Solution:
    def climbStairs(self, n: int) -> int:
        last = 1
        next_to_last = 1

        index = n-1

        while index > 0:
            current_val = next_to_last + last

            last = next_to_last
            next_to_last = current_val
            index -= 1

        return next_to_last