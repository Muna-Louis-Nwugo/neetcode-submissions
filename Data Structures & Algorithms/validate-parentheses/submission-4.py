class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        terminating = [")", "]", "}"]

        for c in s:
            if c in terminating:
                corresponding = ""

                match c:
                    case ")":
                        corresponding = "("
                    case "]":
                        corresponding = "["
                    case "}":
                        corresponding = "{"
                
                
                if len(stack) < 1 or stack[-1] != corresponding:
                    return False
                else:
                    stack.pop()
            
            else:
                stack.append(c)
        
        return len(stack) == 0