# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

# 示例 1:

# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]
# 示例 2:

# 输入: temperatures = [30,40,50,60]
# 输出: [1,1,1,0]
# 示例 3:

# 输入: temperatures = [30,60,90]
# 输出: [1,1,0]

def dailyTemperatures(temperatures):
    n = len(temperatures)
    res = [0] * n  # 初始化结果数组
    stack = []  # 单调递减栈，存储索引

    for i, temp in enumerate(temperatures):
        # 当前温度大于栈顶温度时，更新结果
        while stack and temp > temperatures[stack[-1]]:
            index = stack.pop()
            res[index] = i - index  # 天数差
        stack.append(i)  # 当前索引入栈

    return res

# 示例
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures))  # 输出: [1, 1, 4, 2, 1, 1, 0, 0]
