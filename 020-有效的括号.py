# 给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # 入栈
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif stack == [] or stack[-1] != item:
                return False
            # 出栈
            else:
                stack.pop()

        return True if stack == [] else False