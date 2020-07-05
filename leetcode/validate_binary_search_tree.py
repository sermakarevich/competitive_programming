class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recursive(self, root, low=float(-inf), high=float(inf)):
        if root is None:
            return True
        if root.val >= high or root.val <= low:
            return False
        if root.left is not None:
            print('left', low, root.val)
            if not self.recursive(root.left, low, root.val):
                return False
        if root.right is not None:
            print('right', root.val, high)
            if not self.recursive(root.right, root.val, high):
                return False
        return True

    def iterative(self, root):
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True

    def isValidBST(self, root: TreeNode) -> bool:
        return self.iterative(root)
