class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not postorder:
            return None

        root_value = postorder[-1]
        root = TreeNode(root_value)

        root_index = inorder.index(root_value)

        root.left = self.buildTree(
            inorder[:root_index],
            postorder[:root_index]
        )

        root.right = self.buildTree(
            inorder[root_index + 1:],
            postorder[root_index:-1]
        )

        return root