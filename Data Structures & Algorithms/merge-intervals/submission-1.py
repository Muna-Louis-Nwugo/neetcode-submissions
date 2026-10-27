class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = []

        result.insert(0, intervals[0])

        result_index = 0

        for i in intervals:
            r = result[result_index]
            if r[0] <= i[0] <= r[1] or r[0]<=i[1]<=r[1]:
                result[result_index] = [min(i[0], r[0]), max(i[1], r[1])]
            
            else:
                result_index += 1
                result.insert(result_index, i)

        return result
