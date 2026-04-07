# 示例 1：
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 示例 2：
#
# 输入：l1 = [], l2 = []
# 输出：[]
# 示例 3：
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode(None)
        node = res
        while list1 and list2:
            if list1.val < list2.val:
                node.next, list1 = list1, list1.next
            else:
                node.next, list2 = list2, list2.next
            node = node.next
        if list1:
            node.next = list1
        else:
            node.next = list2
        return res.next
