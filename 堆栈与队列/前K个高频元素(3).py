

from collections import defaultdict
import heapq


def topKFrequent(self, nums,k ):
    # 默认创建字典
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
    # 初始化堆
    heap = []
    # 倒排索引
    for key, val in count.items():
        heapq.heappush(heap, (val, key))
        # 因为是最小堆，所以里面包含的都是最大值
        if len(heap) > k:
            heapq.heappop(heap)
    # 重新倒排
    return [num[1] for num in heap]
        