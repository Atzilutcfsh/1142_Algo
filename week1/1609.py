# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0

        while q:
            level_size = len(q)

            if level % 2 == 0:
                prev = float('-inf')   # 偶數層要遞增
            else:
                prev = float('inf')    # 奇數層要遞減

            for _ in range(level_size):
                node = q.popleft()
                val = node.val

                if level % 2 == 0:
                    if val % 2 == 0 or val <= prev:
                        return False
                else:
                    if val % 2 == 1 or val >= prev:
                        return False

                prev = val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return True