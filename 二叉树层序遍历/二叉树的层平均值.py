# 637. 二叉树的层平均值
# 给定一个非空二叉树的根节点 root , 以数组的形式返回每一层节点的平均值。
# 示例 1：

# 输入：root = [3,9,20,null,null,15,7]
# 输出：[3.00000,14.50000,11.00000]
# 解释：第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
# 因此返回 [3, 14.5, 11] 。
# 示例 2:

# 输入：root = [3,9,20,15,7]
# 输出：[3.00000,14.50000,11.00000]

# 层序遍历五部曲
def averageOfLevels(self, root):
    # 创建结果集
    results = []
    if not root:
        results
    # 创建队列
    q = [root]
    while q:
        # 进行预保存队列长度和返回总和
        size = len(q)
        sum = 0
        for _ in range(size):
            # 在队列中加入子树
            node = q.pop(0)
            sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        # 加入结果
        results.append(sum/size)
    # 返回结果
    return results