# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        _, _, total, count = self.helper(root)
        if not count:
            return 0
        
        return total / count
    
    def helper(self, root):
        if not root:
            return (0, 0, 0, 0)
        
        left_total, left_count, max_left_total, max_left_count = self.helper(root.left)
        right_total, right_count, max_right_total, max_right_count = self.helper(root.right)
        
        subtree_total = root.val + left_total + right_total
        subtree_count = 1 + left_count + right_count
        
        max_total, max_count = subtree_total, subtree_count
        if max_left_count and (max_left_total/max_left_count) > (max_total/max_count):
            max_total = max_left_total
            max_count = max_left_count
            
        if max_right_count and (max_right_total/max_right_count) > (max_total/max_count):
            max_total = max_right_total
            max_count = max_right_count
                    
        return (subtree_total, subtree_count, max_total, max_count)

# O(n) time, space (b/c recursion)

