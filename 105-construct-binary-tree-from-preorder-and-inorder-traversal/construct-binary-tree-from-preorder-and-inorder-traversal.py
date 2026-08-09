class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None

        root_value = preorder[0]
        root = TreeNode(root_value)

        root_index = inorder.index(root_value)

        root.left = self.buildTree(
            preorder[1:root_index + 1],
            inorder[:root_index]
        )

        root.right = self.buildTree(
            preorder[root_index + 1:],
            inorder[root_index + 1:]
        )

        return root