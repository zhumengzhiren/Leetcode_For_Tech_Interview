def searchInsert(nums, target: int) -> int:
    # 我们采取左闭右开写法
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2
        if mid >= nums[target]:
            right = mid
        else:
            left = mid + 1
    return left

print(searchInsert([0,1,2,3,4,5,6,7,8],4))

