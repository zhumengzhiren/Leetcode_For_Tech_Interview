# 560. 和为 K 的子数组
# 提示
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

# 子数组是数组中元素的连续非空序列。

 

# 示例 1：

# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：

# 输入：nums = [1,2,3], k = 3
# 输出：2
import collections

def subarraySum( nums, k):
    s = [0] * (len(nums)+1)
    for i, x in enumerate(nums):
        s[i+1] = s[i] + nums[i]
    print(s)

    cnt = collections.defaultdict(int)
    ans = 0
    for sj in s:
        ans += cnt[sj - k]
        cnt[sj] += 1

    return ans  

print(subarraySum([1,1,1],2))
print(subarraySum([1,2,3],3))