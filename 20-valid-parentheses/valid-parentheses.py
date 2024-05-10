class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif len(stack) != 0 and i == ')':
                if (stack.pop() != '('):
                    return False
            elif len(stack) != 0 and i == '}':
                if (stack.pop() != '{'):
                    return False
            elif len(stack) != 0 and i == ']':
                if (stack.pop() != '['):
                    return False
            else:
                return False
        if (stack):
            return False
        return True

                