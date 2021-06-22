
from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        q = deque()
        q.append(root)
        q.append(root)

        while q:
            result=[]
            count = len(q)
            for i in range(count):
                node = q.popleft()
                result.append(node.val)

                if node.left is not None:
                    q.append(node.left)
                else:
                    if node.val!=-101:
                        new_node = TreeNode(-101)
                        q.append(new_node)
                if node.right is not None:
                    q.append(node.right)
                else:
                    if node.val!=-101:
                        new_node = TreeNode(-101)
                        q.append(new_node)
            print(result)
            l = len(result)//2
            if result[:l]!=result[l:][::-1]:
                return False
        return True
