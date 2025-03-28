# 108. 将有序数组转换为二叉搜索树
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。

# 示例 1：
# 输入：nums = [-10,-3,0,5,9]
# 输出：[0,-3,9,-10,null,5]
# 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

# 示例 2：
# 输入：nums = [1,3]
# 输出：[3,1]
# 解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(self, nums) :
        def recur(arr):
            if not arr:
                return
            mid = len(arr) // 2
            node = TreeNode(arr[mid])
            node.left = recur(arr[:mid])
            node.right = recur(arr[mid+1:])
            return node
        return recur(nums)