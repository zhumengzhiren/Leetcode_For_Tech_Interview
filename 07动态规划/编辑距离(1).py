# 72. 编辑距离
# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

# 你可以对一个单词进行如下三种操作：

# 插入一个字符
# 删除一个字符
# 替换一个字符
 
# 示例 1：

# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2：

# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')

from functools import cache

# 字节生活服务一面惨挂

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