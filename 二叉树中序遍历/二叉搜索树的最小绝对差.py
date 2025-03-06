# 530. 二叉搜索树的最小绝对差
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

# 差值是一个正数，其数值等于两值之差的绝对值。

# 示例 1：


# 输入：root = [4,2,6,1,3]
# 输出：1
# 示例 2：


# 输入：root = [1,0,48,null,null,12,49]
# 输出：1

# Definition for a binary tree node.
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 如何思考中序遍历，先记住中序遍历的顺序左中右
# 二叉搜索树的特性，中序遍历后按从小到大的顺序排列，因此绝大多数二叉搜索树题目都可以用中序遍历来做

def getMinimumDifference(self, root) -> int:
    pre = -inf
    result = inf
    def dfs(root):
        if not root:
            return
        # 左子树需要做什么？答：传递

        # 中子树需要做什么？答：运行核心逻辑
        dfs(root.left)
        nonlocal result,pre

        result = min(result,abs(root.val-pre))
        pre = root.val
        # 右子树需要做什么？ 答：没什么用，其实绝大多数工作在左子树和中子树都已经被做完了
        dfs(root.right)
    dfs(root)
    return result