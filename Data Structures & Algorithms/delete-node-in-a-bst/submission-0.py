# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # An in order traversal of a BST is a sorted list
        # Do DFS and build the list representation.
        # If you encounter key, skip it
        # Then rebuild the tree from the sorted array

        arr = []

        if not root:
            return None

        def inOrderTraversal(node):
            if not node:
                return
            inOrderTraversal(node.left)
            if node.val != key:
                arr.append(node.val)
            inOrderTraversal(node.right)
    

        def buildBSTFromArr(start, end):
            
            if start < 0 or end > len(arr):
                return None
            if start >= end:
                return None
            
            mid = (start + end) // 2

            print(start, end)

            return TreeNode(arr[mid], buildBSTFromArr(start, mid), buildBSTFromArr(mid+1, end))

        inOrderTraversal(root)
        return buildBSTFromArr(0, len(arr))

            


        
            
        