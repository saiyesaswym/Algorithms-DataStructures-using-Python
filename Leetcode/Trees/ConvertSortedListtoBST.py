
def sortedListToBST(self, head: ListNode) -> TreeNode:  
    nums=[]
    curr=head
    while curr is not None:
        nums.append(curr.val)
        curr = curr.next

    def helper(left, right):
        if left > right:
            return None

        # always choose right middle node as a root
        p = (left + right) // 2
        if (left + right) % 2:
            p += 1

        # preorder traversal: node -> left -> right
        root = TreeNode(nums[p])
        root.left = helper(left, p - 1)
        root.right = helper(p + 1, right)
        return root

    return helper(0, len(nums) - 1)
