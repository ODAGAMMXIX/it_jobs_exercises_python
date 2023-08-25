class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def search_in_binary_tree(root, target):
    if root is None or root.val == target:
        return root

    if root.val < target:
        return search_in_binary_tree(root.right, target)

    return search_in_binary_tree(root.left, target)

# Driver code
if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    target_value = 200
    result_node = search_in_binary_tree(root, target_value)

    if result_node:
        print(f"Element {target_value} found in the binary tree.")
    else:
        print(f"Element {target_value} not found in the binary tree.")
