# 912. 排序数组
# 给你一个整数数组 nums，请你将该数组升序排列。

# 你必须在 不使用任何内置函数 的情况下解决问题，时间复杂度为 O(nlog(n))，并且空间复杂度尽可能小。

 

# 示例 1：

# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 示例 2：

# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]

import random
def sortArray(nums):
        def quick(nums):
            if len(nums) == 1 or not nums:
                return nums
            pivot = random.choice(nums)

            small, equal, big = [], [], []
            for num in nums:
                if num < pivot:
                    small.append(num)
                elif num > pivot:
                    big.append(num)
                else:
                    equal.append(num)
            print(pivot,small,equal,big)
            return quick(small) + equal +quick(big)
        return quick(nums)

print(sortArray([5,2,3,1]))
print(sortArray([5,1,1,2,0,0]))
        