class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sort = sorted([(num, index) for (index, num) in enumerate(nums)])
        p1 = 0
        p2 = len(nums) - 1

        while p1 <= p2:
            val = sort[p1][0] + sort[p2][0]
            print(val)

            if val == target:
                return [min(sort[p1][1], sort[p2][1]), max(sort[p1][1], sort[p2][1])]
            elif val < target:
                p1 += 1
            else: 
                p2 -= 1