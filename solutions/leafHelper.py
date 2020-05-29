# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        return self.helper(root)
    
    def helper(self, root):
        boundary = [root.val]
        self.leftSubtreeHelper(root.left, boundary)
        self.rightSubtreeHelper(root.right, boundary)
        return boundary
        
    def leftSubtreeHelper(self, root, boundary):
        if not root:
            return
        boundary.append(root.val)
        boundary_node, leaf_node = (root.left, root.right) if root.left else (root.right, None)
        self.leftSubtreeHelper(boundary_node, boundary)
        self.leafHelper(leaf_node, boundary)
        
    def rightSubtreeHelper(self, root, boundary):
        if not root:
            return
        boundary_node, leaf_node = (root.right, root.left) if root.right else (root.left, None)
        self.leafHelper(leaf_node, boundary)
        self.rightSubtreeHelper(boundary_node, boundary)
        boundary.append(root.val)
        
    def leafHelper(self, root, boundary):
        if not root:
            return
        elif not (root.left or root.right):
            boundary.append(root.val)        
        else:
            self.leafHelper(root.left, boundary)
            self.leafHelper(root.right, boundary)

# O(n) time, space

