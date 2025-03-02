def largestRectangleArea(heights):
    stack = []  # 单调递增栈，存储索引
    max_area = 0
    heights.append(0)  # 添加一个高度为0的柱子，便于清空栈

    for i, h in enumerate(heights):
        # 当前柱子高度小于栈顶柱子时，计算面积
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]  # 栈顶柱子的高度
            width = i if not stack else i - stack[-1] - 1  # 宽度
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area

# 示例
heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))  # 输出: 10
