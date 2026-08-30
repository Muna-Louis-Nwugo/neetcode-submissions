class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s));
            res += "#"
            res += s
        
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        print(s)

        current_length = ""
        length_converted = 1
        current_string = ""
        stringing = False


        for c in s:
            if stringing:
                length_converted -= 1
                current_string += c

                if length_converted == 0:
                    res.append(current_string)
                    current_length = ""
                    current_string = ""
                    stringing = False
            elif c == "#":
                length_converted = int(current_length)

                if length_converted == 0:
                    res.append("")
                else:
                    stringing = True
            else:
                current_length += c


        return res
