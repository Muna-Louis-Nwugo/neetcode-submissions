class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        seen = set()

        pointer1 = 0
        pointer2  = 1
        max_len = 1
        curr_len = 1

        seen.add(s[pointer1])
        while pointer2 < len(s) and pointer1 < pointer2:
            while s[pointer2] in seen:
               seen.remove(s[pointer1])
               pointer1 += 1
            
            else:
                seen.add(s[pointer2])
                pointer2 += 1
        
            curr_len = pointer2 - pointer1

            if curr_len > max_len:
                max_len = curr_len
        
        return max_len