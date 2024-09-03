class Solution(object):
    def calculate(s):
        """
        :type s: str
        :rtype: int
        """
        digit, res, num, prev = 1, 0, 0, 0
        op = 1
        stack = []
        for c in s:
            if c.isdigit():
                if digit != 1:
                    res = op * (int(c) + digit * num) + prev
                    num = 10 * num + int(c) 
                else:
                    prev = res
                    res = op * int(c) + res
                    num = int(c)
                digit = 10
            elif c == "(":
                stack.append(res)
                stack.append(op)
                res = 0
                op = 1
            elif c == ")":
                op = stack.pop()
                res = stack.pop() + op * res
            else:
                if c == "+":
                    op = 1
                    
                if c == "-":
                    op = -1
                digit = 1
        return res

