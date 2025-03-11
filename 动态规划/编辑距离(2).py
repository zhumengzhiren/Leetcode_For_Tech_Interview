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

# 二维数组初始化做法
def minDistance(word1, word2):
    m , n = len(word1), len(word2)
    # 注意这里dp的顺序很重要，先被初始化的反而是内侧的元素，要牢记这一点，不然就会出错
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)] 
    dp[0] = list(range(n+1))
    # for i in range(m+1):
    #     dp[i][0] = i
    for i in range(m+1):
        dp[i][0] = i
        for j in range(n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) +1 
    return dp[-1][-1]

print(minDistance("horse", "ros"))
print(minDistance("intention","execution"))