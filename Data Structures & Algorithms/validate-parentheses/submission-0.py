class Solution:
    def isValid(self, s: str) -> bool:
        op = {'(','{','['}
        cl = {')','}',']'}
        stack = []
        for ch in s:
            if ch in op:
                stack.append(ch)
            elif ch in cl:
                if len(stack) == 0:
                    return False
                left = stack.pop()
                if left == '(' and ch != ')':
                    return False
                if left == '{' and ch != '}':
                    return False
                if left == '[' and ch != ']':
                    return False
        return len(stack) == 0
                    

        