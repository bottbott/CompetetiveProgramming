class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        open_brackets = '({['
        close_brackets = ')}]'
        for c in s:
            # add all opening brackets to stack
            if c in open_brackets:
                bracket_stack.append(c)
            # remove from the stack if the bracket matches
            if c in close_brackets:
                index = close_brackets.index(c)
                try:
                    if open_brackets[index] == bracket_stack[-1]:
                        bracket_stack.pop()
                    else:
                        return False
                except:
                    return False
        if len(bracket_stack) == 0:
            return True
        return False



sol = Solution()

print(sol.isValid('()'))
print(sol.isValid('(hello)[my]{name}'))
print(sol.isValid('(()'))
print(sol.isValid(']'))
print(sol.isValid('(])'))
