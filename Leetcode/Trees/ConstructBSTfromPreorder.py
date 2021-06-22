
def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

    def helper(arr, root):
        if len(arr)==1:
            return

        i=0
        while i<len(arr):
            if arr[i]>root.val:
                break
            i+=1

        left_arr = arr[1:i]
        right_arr = arr[i:]

        if left_arr:
            node1 = TreeNode(val=left_arr[0])
            root.left = node1
            helper(left_arr, node1)
        if right_arr:
            node2 = TreeNode(val=right_arr[0])
            root.right = node2
            helper(right_arr, node2)

    root = TreeNode(val = preorder[0])
    helper(preorder, root)

    return root
