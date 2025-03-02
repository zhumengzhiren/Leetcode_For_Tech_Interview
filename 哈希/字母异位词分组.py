# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

 

# 示例 1:

# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 示例 2:

# 输入: strs = [""]
# 输出: [[""]]
# 示例 3:

# 输入: strs = ["a"]
# 输出: [["a"]]

import collections

# 第一种写法
def groupAnagrams(strs):
        # 首先建立mp,以列表作为key，记住是collections.defaultdict(list)
        # collections是python中的集合类，defaultdict则表示使用[]作为key不存在时的默认填充值
        mp = collections.defaultdict(list)
        # 开始遍历字符串列表
        for st in strs:
            # 由于最多有26个字母，可以把它变成一个tuple，这样加入的时候就可以加入到同一个集合中
            counts = [0] * 26
            # 开始遍历字符串中的每一个单字
            for ch in st:
                # 根据他们的差异加上对应的位置
                counts[ord(ch) - ord("a")] += 1
            # 元祖化，并且加入对应的字符串以确保同一性
            mp[tuple(counts)].append(st)
            # 利用values()函数将mp转换为一个值
        return list(mp.values())

# 第二种方法，利用字母异位词排序后相同的特性，更为简单的解决问题
def groupAnagrams(self, strs):
        # 首先建立mp,以列表作为key，记住是collections.defaultdict(list)
        mp = collections.defaultdict(list)
        # 开始遍历字符串列表
        for st in strs:
            # 这里是不能直接使用sorted，因为sorted函数的返回值是一个list，而list是无法被hash的
            key = "".join(sorted(st))
            mp[key].append(st)

            # 当然你也可以像上面那样使用tuple化
            # key = sorted(st)
            # mp[tuple(key)].append(st)

        return list(mp.values())