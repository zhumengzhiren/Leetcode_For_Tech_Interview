# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

 

# 示例 1：

# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 示例 2：

# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
# 示例 3：

# 输入：nums = [1,0,1,2]
# 输出：3

def longestConsecutive(nums) -> int:
    # 最长连胜，初始化为0
    longest_streak = 0
    # 建立一个set表示num_set
    num_set = set(nums)

    # 开始遍历数组
    for num in num_set:
        # 如果他的上一位不在数组中，则说明他是头，这个时候我们可以开始对他进行连胜计算
        if num - 1 not in num_set:

            current_num = num
            # 默认的连胜数从1开始，因为我们已经计算了头
            current_streak = 1

            # 如果头的下一位也在列表中，则增添连胜和更新头
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            # 在连胜中断后，试图寻找当前连胜和最长连胜的最大值以更新最长连胜
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

