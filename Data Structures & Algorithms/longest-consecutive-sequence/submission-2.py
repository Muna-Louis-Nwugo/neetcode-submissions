class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_sorted = sorted(nums)
        print(nums_sorted)
        counter = 1
        max_counter = 1
        last_num = nums_sorted[0]

        for num in nums_sorted:
            if last_num + 1 == num:
                counter += 1
            elif last_num == num:
                continue
            else:
                counter = 1

            if counter > max_counter:
                max_counter = counter

            last_num = num
        
        return max_counter