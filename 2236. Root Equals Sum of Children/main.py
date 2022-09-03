from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left + root.right
    
def main():
    root = TreeNode(5, 3, 1)
    solu = Solution()
    print(solu.checkTree(root))
    root = TreeNode(10, 6, 4)
    solu = Solution()
    print(solu.checkTree(root))

if __name__ == "__main__":
    main()