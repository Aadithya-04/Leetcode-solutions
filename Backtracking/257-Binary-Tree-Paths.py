
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        result = []

        # Helper function to perform DFS traversal
        def dfs(node, current_path):
            if not node:
                return
            
            # Append current node value to path
            current_path += str(node.val)
            
            # If it's a leaf, add the path to the result
            if not node.left and not node.right:
                result.append(current_path)
            else:
                # Otherwise, continue the DFS traversal on both left and right children
                current_path += "->"
                dfs(node.left, current_path)
                dfs(node.right, current_path)
        
        # Start DFS from the root
        dfs(root, "")
        
        return result
