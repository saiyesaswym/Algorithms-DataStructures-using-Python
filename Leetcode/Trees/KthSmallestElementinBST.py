"""
InOrder Traversal of BST -> Sorted Array
Time complexity: O(n)
Space complexity: O(h)
"""
def kthSmallest(self, root: TreeNode, k: int) -> int:

    def bst_to_array(node, slate):
        if not node:
            return

        if node.left:
            bst_to_array(node.left, slate)

        slate.append(node.val)

        if node.right:
            bst_to_array(node.right, slate)

    arr = []
    bst_to_array(root, arr)

    return arr[k-1]


"""
O(H) to reach the smallest node in the BST.
O(k) to find the kth smallest from there doing an inorder search.
Time complexity: O(h+k)
Space complexity: O(h)
"""
def kthSmallest(self, root: TreeNode, k: int) -> int:
    s=[]
    curr=root

    while s or curr:
        if curr:
            s.append(curr)
            curr = curr.left
        else:
            curr = s.pop()
            k-=1
            if not k:
                return curr.val
            curr = curr.right
