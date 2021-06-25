"""
Time complexity: O(n)
Space complexity: O(logn) - Since it is a Balanced binary tree - Call stack takes height of the tree
"""
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    def helper(arr, root):
        if not arr or len(arr)==1:
            return

        n = len(arr)//2
        left_arr = arr[:n]
        right_arr = arr[n+1:]

        if left_arr:
            l1 = len(left_arr)//2
            node1 = TreeNode(val=left_arr[l1])
            root.left = node1
            helper(left_arr, node1)
        if right_arr:
            l2 = len(right_arr)//2
            node2 = TreeNode(val=right_arr[l2])
            root.right = node2
            helper(right_arr, node2)

    n = len(nums)//2
    root = TreeNode(val = nums[n])
    helper(nums, root)

    return root



def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
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
