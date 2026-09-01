class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        result = []
        zero_counter = 0

        for num in nums:
            if num == 0:
                zero_counter += 1
                if zero_counter >= 2:
                    print("entered")
                    result = [0] * len(nums)
                    return result
                continue
            product *= num
        
        for num in nums:
            if num == 0:
                result.append(product)
            elif zero_counter >= 1:
                result.append(0)
            else:
                result.append(int(product/num))
        
        return result