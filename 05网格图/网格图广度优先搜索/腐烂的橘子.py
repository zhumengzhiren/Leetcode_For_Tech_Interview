# 994. 腐烂的橘子
# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

# 示例 1：
# 输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
# 示例 2：
# 输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
# 示例 3：
# 输入：grid = [[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。

def orangesRotting(grid):
    # 初始化行列,队列，新鲜橘子
    r, c = len(grid), len(grid[0])
    q = []
    fresh = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                fresh += 1
            elif grid[i][j] == 2:
                q.append((i,j))
    ans = 0
    # 开始遍历
    while q and fresh:
        # 每分钟
        ans += 1
        # 预保存队列长度
        for index in range(len(q)):
            # 弹出队列
            x, y = q.pop(0)
            # 遍历四个方向
            for i, j in ((x+1,y), (x-1,y),(x,y+1),(x,y-1)):
                # 判断是否越界
                if i < 0 or i >= r or j < 0 or j >= c:
                    continue
                # 判断是否是新鲜橘子
                if grid[i][j] == 1:
                    # 消除新鲜橘子
                    fresh -= 1
                    # 加入队列
                    q.append((i,j))
                    # 更改状态
                    grid[i][j] = 2
    # 返回-1或者分钟数
    return -1 if fresh else ans

print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]])) # -1
print(orangesRotting([[0,2]])) # 0
        

