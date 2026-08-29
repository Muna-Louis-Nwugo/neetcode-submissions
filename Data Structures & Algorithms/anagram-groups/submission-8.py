class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # HASH CHARACTER COUNT TO STRS DIRECT
        result = {}

        for s in strs:
            charcount = {}
            
            for c in s:
                if c in charcount.keys():
                    charcount[c] += 1
                else:
                    charcount[c] = 1
            
            key = frozenset(charcount.items())

            if key in result.keys():
                result[key].append(s)
            else:
                result[key] = [s]

        values = result.values()
        return list(result.values())
