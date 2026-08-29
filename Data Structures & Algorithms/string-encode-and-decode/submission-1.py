class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += s;
            res += "😛";
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        current = ""
        for c in s:
            if c == "😛":
                res.append(current)
                current = ""
            else:
                current += c

        return res
