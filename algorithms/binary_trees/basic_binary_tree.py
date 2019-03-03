
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def depth_of_tree(tree: Node):
    """
    :param tree:
            A
          /  \
        B     C
      /  \     \
    D     E     F

    :return: 3
    Depth of tree is height of tree from root to down
       Complexity - log(n) regarding number of nodes
    """
    if tree is None:
        return 0
    else:
        depth_l_tree = depth_of_tree(tree.left)
        depth_r_tree = depth_of_tree(tree.right)
        if depth_l_tree > depth_r_tree:
            return 1 + depth_l_tree
        else:
            return 1 + depth_r_tree


def is_full_binary_tree(tree: Node) -> bool:
    """
    :param tree:
            A
          /  \
        B     C
      /  \     \
    D     E     F
    :return false
    Check if each leaf do not have one child
    """
    if tree is None:
        return True
    if (tree.left is None) and (tree.right is None):
        return True
    if (tree.left is not None) and (tree.right is not None):
        return (is_full_binary_tree(tree.left) and
                is_full_binary_tree(tree.right))
    else:
        return False


def build_binary_tree(preorder: list, inorder: list) -> Node:
    if len(preorder) == 0:
        return
    if len(preorder) == 1:
        return Node(preorder[0])

    tree = Node(preorder[0])
    root_index_in_order = inorder.index(preorder[0])
    tree.left = build_binary_tree(preorder[1:(root_index_in_order + 1)],
                                  inorder[0:root_index_in_order])
    tree.right = build_binary_tree(preorder[(root_index_in_order+1):],
                                   inorder[root_index_in_order + 1:])
    return tree


def pre_order(tree: Node, result=None) -> list:
    """
    :param tree:
            A
          /  \
        B     C
      /  \     \
    D     E     F

    :return: A B D E C F
    - first is always root (truth regarding each subtree)
    - |root|-|left subtree|-|right subtree|
    """
    if result is None:
        result = list()
    if tree is None:
        return result

    result.append(tree.data)
    if tree.left is not None:
        pre_order(tree.left, result)
    if tree.right is not None:
        pre_order(tree.right, result)
    return result


def in_order(tree: Node, result=None) -> list:
    """
            A
          /  \
        B     C
      /  \     \
    D     E     F
    :param tree:
    :return: D B E A F C
    - left leaf is always first,
    - root is inside unless right subtree is empty,
    - all nodes before root is left subtree,
    - all nodes after root is right subtree
    - |left subtree|-|root|-|right subtree|
    """
    if result is None:
        result = list()
    if tree is None:
        return result

    if tree.left is not None:
        in_order(tree.left, result)
    result.append(tree.data)
    if tree.right is not None:
        in_order(tree.right, result)
    return result


def post_order(tree: Node, result=None) -> list:
    """
            A
          /  \
        B     C
      /  \     \
    D     E     F
    :param tree:
    :return: D E B F C A
    - left leaf is always first,
    - root is always last
    - |left subtree|-|right subtree|-|root|
    """
    if result is None:
        result = list()
    if tree is None:
        return result

    if tree.left is not None:
        post_order(tree.left, result)
    if tree.right is not None:
        post_order(tree.right, result)
    result.append(tree.data)
    return result

