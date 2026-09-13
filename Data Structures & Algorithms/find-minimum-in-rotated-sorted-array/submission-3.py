class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = float('inf')

        while right >= left:
            if nums[right] >= nums[left]:
                if nums[left] <= result:
                    result = nums[left]
                
                break
            else:
                middle = math.floor((right + left) / 2)

                if nums[middle] < result:
                    result = nums[middle]

                if nums[middle] >= nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1

        
        return result