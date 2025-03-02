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

import heapq

def findKthLargest(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap) 
    return min_heap[0] if min_heap else None

print(findKthLargest([3,2,1,5,6,4],2))

print(findKthLargest([3,2,3,1,2,4,5,5,6],4))


