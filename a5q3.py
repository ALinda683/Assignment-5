# Name: Alinda Kumar Mazumder
# NSID: ugj683
# Student Number: 11342454

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def ordered(tnode):
    def is_ordered(node, lower_bound, upper_bound):
        if node is None:
            return True

        if lower_bound is not None and node.data <= lower_bound:
            return False

        if upper_bound is not None and node.data >= upper_bound:
            return False

        left_ordered = is_ordered(node.left, lower_bound, node.data)
        right_ordered = is_ordered(node.right, node.data, upper_bound)

        return left_ordered and right_ordered
