from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self):
        if self.next:
            return [self.val] + self.next.to_list()
        else:
            return [self.val]


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return solution(l1, l2, 0)


def solution(l1: Optional[ListNode], l2: Optional[ListNode], rem: int) -> Optional[ListNode]:
    sum = (0 if l1 is None else l1.val) + (0 if l2 is None else l2.val) + rem
    sum, rem = sum % 10, sum // 10

    if l1 is None and l2 is None and sum == 0:
        return None
    else:
        return ListNode(
            val=sum,
            next=solution(None if l1 is None else l1.next,
                          None if l2 is None else l2.next, rem)
        )


if __name__ == '__main__':
    l1 = ListNode(9, ListNode(9, ListNode(
        9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    sol = Solution()
    print(sol.addTwoNumbers(l1, l2).to_list())
