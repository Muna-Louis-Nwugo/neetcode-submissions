class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_frequency_s = {}
        char_frequency_t = {}

        for c in s:
            if c in char_frequency_s:
                char_frequency_s[c] += 1
            else: 
                char_frequency_s[c] = 1
        
        for c in t:
            if c in char_frequency_t:
                char_frequency_t[c] += 1
            else: 
                char_frequency_t[c] = 1

        return char_frequency_s == char_frequency_t
            

        

        