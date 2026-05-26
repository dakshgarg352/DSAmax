class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        x = ''
        if s[0] in ')}]' or len(s)%2 == 1:
            return False
        for i in range(len(s)):
            m = s[i]
            if m in '[{(':
                stack.append(m)
                continue
            if not stack:
                return False
            n = stack[-1]
            if m == ']' and n != '[':
                return False
            elif m == '}' and n != '{':
                return False
            elif m == ')' and n != '(':
                return False
            stack.pop()
            
        if not stack:
            return True
        return False