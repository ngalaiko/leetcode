from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self) -> List[int]:
        list = []
        head = self
        while head is not None:
            list.append(head.val)
            head = head.next
        return list


def list_to_list_node(list: List[int]) -> Optional[ListNode]:
    if len(list) == 0:
        return None
    else:
        return ListNode(list[0], list_to_list_node(list[1:]))


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for j in range(0, n)] for i in range(0, m)]

        i, j = 0, 0
        di, dj = 0, 1
        k = 0
        while head is not None and k != m*n:
            if di == 0 and dj == 1:  # walking right
                matrix[i][j] = head.val
                head = head.next

                if j == n-1 or matrix[i][j+1] != -1:  # go down
                    di, dj = 1, 0

            elif di == 1 and dj == 0:  # walking down
                matrix[i][j] = head.val
                head = head.next

                if i == m - 1 or matrix[i+1][j] != -1:  # go left
                    di, dj = 0, -1

            elif di == 0 and dj == -1:  # walking left
                matrix[i][j] = head.val
                head = head.next

                if j == 0 or matrix[i][j-1] != -1:  # go up
                    di, dj = -1, 0

            elif di == -1 and dj == 0:  # waling up
                matrix[i][j] = head.val
                head = head.next

                if i == 0 or matrix[i-1][j] != -1:  # go right
                    di, dj = 0, 1

            i += di
            j += dj
            k += 1

        return matrix


if __name__ == '__main__':
    assert Solution().spiralMatrix(3, 5, list_to_list_node([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])) == [
        [3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]]

    assert Solution().spiralMatrix(
        1, 4, list_to_list_node([0, 1, 2])) == [[0, 1, 2, -1]]

    assert Solution().spiralMatrix(
        1, 4, list_to_list_node([0, 1, 2, 3, 4])) == [[0, 1, 2, 3]]
