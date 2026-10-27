class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
            "E": 0,
            "F": 0,
            "G": 0,
            "H": 0,
            "I": 0,
            "J": 0,
            "K": 0,
            "L": 0,
            "M": 0,
            "N": 0,
            "O": 0,
            "P": 0,
            "Q": 0,
            "R": 0,
            "S": 0,
            "T": 0,
            "U": 0,
            "V": 0,
            "W": 0,
            "X": 0,
            "Y": 0,
            "Z": 0
        } 

        max_len = 0
        curr_len = 0

        left = 0
        right = 0

        for right in range(len(s)):
            right_val = s[right]
            char_map[right_val] += 1

            curr_len = (right - left) + 1

            if curr_len - max(char_map.values()) <= k:
                if max_len < curr_len:
                    max_len = curr_len
            else:
                while curr_len - max(char_map.values()) > k:
                    char_map[s[left]] -= 1
                    left += 1
                    curr_len = (right - left) + 1

        return max_len