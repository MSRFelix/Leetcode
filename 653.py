# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    seen = set()
    sol = False
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.seen.add(root.val)
        def traverser(rot):
            if rot == None:
                return
            if rot.left != None:
                self.seen.add(rot.left.val)
                traverser(rot.left)
            if rot.right != None:
                self.seen.add(rot.right.val)
                traverser(rot.right)
        traverser(root)
        for i in self.seen:
            if k - i in self.seen and k != 2*i:
                self.sol = True
        self.seen.clear()
        return self.sol

# BST traversal to find good pair
