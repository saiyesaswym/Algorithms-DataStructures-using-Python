
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: TreeNode):
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
