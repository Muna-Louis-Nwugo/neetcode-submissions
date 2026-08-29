import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        nums.sort()

        current_num = nums[0]
        count = 0
        for num in nums:
            if num == current_num:
                count += 1
            else:
                heapq.heappush(heap, (count, current_num))
                count = 1
                current_num = num
        
        heapq.heappush(heap, (count, current_num))

        # IN PYTHON, .nlargest IS HOW YOU EXTRACT THE LARGEST VALUES FROM A HEAP
        # REMEMBER: Heaps are a binary tree where the left side is smaller and the right side is larger (or vice versa)
        final = [x for (a, x) in heapq.nlargest(k, heap)]
        
        return final
        