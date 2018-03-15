class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if stack:
                    poped = stack.pop()
                    if poped == '(' and c != ')':
                        return False
                    elif poped == '[' and c != ']':
                        return False
                    elif poped == '{' and c != '}':
                        return False
                else:
                    return False
        if stack:
            return False  # should be empty at last
        else:
            return True