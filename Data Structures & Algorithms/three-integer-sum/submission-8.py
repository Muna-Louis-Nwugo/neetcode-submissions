class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                p1 = i + 1
                p2 = len(nums) - 1
                target = 0 - nums[i]

                while p1 < p2:
                    val = nums[p1] + nums[p2]

                    if val == target:
                        result.append([nums[i], nums[p1], nums[p2]])
                        p1 += 1
                        p2 -= 1

                        # do this to make sure that we're skipping duplicates in the final result
                        while nums[p2] == nums[p2 + 1] and p1 < p2:
                            p2 -= 1

                        while nums[p1] == nums[p1-1] and p1 < p2:
                            p1 += 1
                    elif val < target:
                        p1 += 1
                    else: 
                        p2 -= 1
                
        
        return result