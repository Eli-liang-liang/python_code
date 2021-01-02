# class BinaryTreeNode(object):
#     """二叉树的结点"""

#     def __init__(self, item):
#         # val
#         self.val = item
#         # left是左节点的指针
#         self.left = None
#         # right是左节点的指针
#         self.right = None

# Node3 = BinaryTreeNode(3)
# Node5 = BinaryTreeNode(5)
# Node6 = BinaryTreeNode(6)
# Node8 = BinaryTreeNode(8)
# Node9 = BinaryTreeNode(9)
# Node10 = BinaryTreeNode(10)
# Node11 = BinaryTreeNode(11)

# # 补充代码，将树连起来

# Node8.left = Node5
# Node8.right = Node10
# Node5.left = Node3
# Node5.right = Node6
# Node10.left = Node9
# Node10.right = Node11

# # 执行下面代码进行监测

# def print_tree(tree_root):
#     if tree_root is None:
#         return
#     print_tree(tree_root.left)
#     print(tree_root.val, end='')
#     print("-",end='')
#     print_tree(tree_root.right)

# print_tree(Node3)
# print("\n")
# print_tree(Node5)
# print("\n")
# print_tree(Node8)