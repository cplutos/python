"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。



示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。


提示：

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 如果非空，则仅由小写英文字母组成
"""

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        # min和max本身比较的是字符ascll码
        s1 = min(strs)
        s2 = max(strs)

        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

s = Solution()
result = s.longestCommonPrefix(["flower","flow","flight"])
print(result)