
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(self, root: TreeNode) -> List[List[int]]:
    final_result=[]
    if not root:
        return final_result
    q = []
    q.append(root)

    while q:
        node = q.pop(0)
        final_result.append(node.val)

        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    return final_result


root = [3,9,20,null,null,15,7]
print(levelOrder(root))
