class Solution(object):
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        values = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(values[mid])

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        inorder(root)
        return build(0, len(values) - 1)