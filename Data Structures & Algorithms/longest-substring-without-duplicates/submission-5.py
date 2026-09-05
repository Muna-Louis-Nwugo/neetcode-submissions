class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        substring = ''
        p1 = 0
        p2 = 1

        substring += s[p1]
        max_length = 1

        while p2 < len(s) and p1 < p2:
            if s[p2] in substring:
                p1 += 1

                if p1 == p2:
                    p2 += 1
                    
                substring = s[p1:p2]
            else:
                substring += s[p2]
                if len(substring) > max_length:
                    max_length = len(substring)
                p2 += 1
        
        return max_length
                