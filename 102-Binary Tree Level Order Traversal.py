# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, nodes: List[TreeNode]) -> List[TreeNode]:
        next_level_nodes = []
        for node in nodes:
            if node.left is not None:
                next_level_nodes.append(node.left)
            if node.right is not None:
                next_level_nodes.append(node.right)
        return next_level_nodes

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result_ints = [[root.val]]
        next_level_nodes = self.bfs([root])
        while next_level_nodes:
            _result = []
            for node in next_level_nodes:
                _result.append(node.val)
            result_ints.append(_result)
            next_level_nodes = self.bfs(next_level_nodes)
        
        return result_ints
