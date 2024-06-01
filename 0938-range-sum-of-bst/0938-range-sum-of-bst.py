class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []

        def traversal(node):
            if node is None:
                return

            if low <= node.val <= high:
                res.append(node.val)
            if low < node.val:
                traversal(node.left)
            if node.val < high:
                traversal(node.right)

        traversal(root)

        return sum(res)
