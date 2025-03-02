# 215. 数组中的第K个最大元素
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

# 示例 1:

# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
# 示例 2:

# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4

import random

def findKthLargest(nums, k):
    # 随机选择一个数字
    pivot = random.choice(nums)
    # 创建三个数组，分别代表小，中，大
    small, equal, big = [], [], []
    # 对于列表中的数组，根据小中大的情况分别加入小中大的列表
    for num in nums:
        if num < pivot:
            small.append(num)
        elif num > pivot:
            big.append(num)
        else:
            equal.append(num)

    # 如果大于pivot的长度大于k代表目标在大于中，继而对大于pivot的数组继续进行检索
    if len(big) >= k:
        return findKthLargest(big, k)
    # 如果nums的长度减去小于pivot的长度小于k代表目标在小于中，继而对小于pivot的数组继续进行检索
    elif len(nums) - len(small) < k:
        return findKthLargest(small, k-len(nums)+len(small))
    return pivot
    




print(findKthLargest([3,2,1,5,6,4],2))
print(findKthLargest([3,2,3,1,2,4,5,5,6],4))