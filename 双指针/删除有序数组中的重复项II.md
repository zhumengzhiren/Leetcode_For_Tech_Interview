给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

<!-- def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 1, 1
        n = len(nums)
        cur, count = nums[0], 1
        while i < n and j < n:
            if nums[j] == cur:
                count += 1
            else:
                cur = nums[j]
                count = 1
            if count <= 2:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i -->

对于两次及以上重复，我们可以用两个变量来判断，一个是当前的值，一个是当前值的重复次数。当重复次数小于等于 2 时，我们可以移动慢指针，依旧遵守快探慢移的原则。
