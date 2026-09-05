class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.replace(" ", "")
        clean = [c for c in string if c.isalnum()]
        s = s.lower()

        pointer1 = 0
        pointer2 = len(clean) - 1
        s1 = ""
        s2 = ""

        while pointer1 < pointer2:
            s1 += clean[pointer1].lower()
            s2 += clean[pointer2].lower()

            pointer1 += 1
            pointer2 -= 1

        print(s1, s2)
        return s1 == s2