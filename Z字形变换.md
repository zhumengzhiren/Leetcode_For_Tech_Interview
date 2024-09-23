将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
 

示例 1：

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
示例 3：

输入：s = "A", numRows = 1
输出："A"

思路及算法

非常有意思的一道题，分别有矩阵数组字符串三种解法，随着数据结构越来越简单，解法所需要的思路也越来越复杂。与之相对应的，解法所需求的时间也越来越短。

```
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        base = 2 * numRows - 2
        sep = base
        new = ''
        for i in range(numRows):
            if i < len(s):
                new += s[i]
            sep = base - 2 * i
            if sep == 0:
                sep = base
            k = i + sep
            while k < len(s):
                new += s[k]
                if sep < base:
                    sep = base - sep
                k += sep
        return new
```

