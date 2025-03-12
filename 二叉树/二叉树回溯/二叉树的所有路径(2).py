# 257. 二叉树的所有路径
# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

# 叶子节点 是指没有子节点的节点。

# 示例 1：

# 输入：root = [1,2,3,null,5]
# 输出：["1->2->5","1->3"]
# 示例 2：

# 输入：root = [1]
# 输出：["1"]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    result = []
    def dfs(node,path):
        if not node:
            return
        path += str(node.val)
        if node.left is node.right:
            result.append(path)
        path += "->"
        dfs(node.left,path)
        dfs(node.right,path)
    dfs(root,"")
    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
print(binaryTreePaths(root)) # ["1->2->5","1->3"]

root = TreeNode(1)
print(binaryTreePaths(root)) # ["1"]