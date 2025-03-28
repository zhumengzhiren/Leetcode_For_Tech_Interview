# 347. 前 K 个高频元素
# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

# 示例 1:

# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:

# 输入: nums = [1], k = 1
# 输出: [1]
import collections

# 直接看api理解意思
def topKFrequent(self, nums, k):
        count = collections.Counter(nums)
        return [item[0] for item in count.most_common(k)]