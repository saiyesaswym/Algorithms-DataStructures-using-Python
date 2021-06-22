
def postorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    result=[]
    pre = None
    s=[]
    curr = root

    while curr or s:
        if curr:
            s.append(curr)
            curr = curr.left
        else:
            curr = s[-1]
            if curr.right is None or curr.right==pre:
                result.append(curr.val)
                s.pop()
                pre=curr
                curr=None
            else:
                curr=curr.right

    return result





def postorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
        return []

    result = []
    s = []
    s.append(root)

    while s:
        node = s.pop()
        result.append(node.val)

        if node.left:
            s.append(node.left)

        if node.right:
            s.append(node.right)

    return result[::-1]
