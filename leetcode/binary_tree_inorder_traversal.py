class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recursive(self, root, output):
        if root is not None:
            self.recursive(root.left, output)
            output.append(root.val)
            self.recursive(root.right, output)

    def iterative(self, root):
        output = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            if stack and root is None:
                root = stack.pop()
                output.append(root.val)
                root = root.right
        return output

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # output = []
        # self.recursive(root, output)
        output = self.iterative(root)
        return output
