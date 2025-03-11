from functools import cache

# 递归做法
def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # cache很重要，不然会超时
        @cache
        def dfs(i, j):
            # base case
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            # 如果两个字符相等，不需要操作
            if word1[i] == word2[j]:
                return dfs(i-1,j-1)
            # 如果不相等，三种操作方式
            return min(dfs(i-1,j), dfs(i,j-1),dfs(i-1,j-1)) + 1
        # 从后往前递归
        return dfs(m-1,n-1)