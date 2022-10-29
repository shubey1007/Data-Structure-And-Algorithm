class SolutSolutionion(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        if not root.left and not root.right and targetSum == root.val:
            return [[root.val]]
        l_path = self.pathSum(root.left, sum-root.val)
        r_path = self.pathSum(root.right, sum-root.val)
        left = [[root.val]+l for l in l_path]
        right = [[root.val]+r for r in r_path]
        return left+right
