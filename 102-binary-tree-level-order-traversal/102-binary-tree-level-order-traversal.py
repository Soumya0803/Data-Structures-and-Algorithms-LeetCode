# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        output=[]
        queue=[]
        queue.append(root)
        while queue:
            level_val=[]
            for _ in range(len(queue)): 
                node=queue.pop(0)
                level_val.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(level_val)
        return output


        
            
        