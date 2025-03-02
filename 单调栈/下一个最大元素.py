def nextGreaterElements(nums):
    n = len(nums)
    res = [-1] * n  # 初始化结果数组
    stack = []  # 存储索引的单调递减栈

    for i in range(n):
        # 当当前元素大于栈顶索引对应的元素时，弹出栈顶
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            res[index] = nums[i]  # 当前元素是栈顶的下一个更大元素
        stack.append(i)  # 将当前索引入栈

    return res

# 示例
nums = [2, 1, 2, 4, 3]
print(nextGreaterElements(nums))  # 输出: [4, 2, 4, -1, -1]