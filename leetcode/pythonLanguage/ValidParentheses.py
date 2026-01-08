class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        for c in s:
            match c:
                case "(":
                    stack.append(c)
                case "[":
                    stack.append(c)
                case "{":
                    stack.append(c)
                case ")":
                    if len(stack)>0 and stack[-1]=='(':
                        stack.pop()
                    else:
                        return False
                case "]":
                    if len(stack)>0 and stack[-1]=='[':
                        stack.pop()
                    else:
                        return False
                case "}":
                    if len(stack)>0 and stack[-1]=='{':
                        stack.pop()
                    else:
                        return False
        return len(stack)==0
    
solution= Solution()

print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("([])"))
print(solution.isValid("([)]"))