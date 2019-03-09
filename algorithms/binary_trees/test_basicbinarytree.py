import pytest
import algorithms.binary_trees.basic_binary_tree as trees

in_order = ['D', 'B', 'E', 'A', 'F', 'C']
pre_order = ['A', 'B', 'D', 'E', 'C', 'F']
binary_tree = trees.build_binary_tree(
    preorder=pre_order,
    inorder=in_order
)


def test_pre_order():
    assert trees.pre_order(binary_tree) == pre_order


def test_in_order():
    assert trees.in_order(binary_tree) == in_order


def test_post_order():
    assert trees.post_order(binary_tree) == ['D', 'E', 'B', 'F', 'C', 'A']


in_order_2 = []
pre_order_2 = []
binary_tree_2 = trees.build_binary_tree(
    preorder=pre_order_2,
    inorder=in_order_2
)


def test_pre_order_empty():
    assert trees.pre_order(binary_tree_2) == pre_order_2


def test_in_order_empty():
    assert trees.in_order(binary_tree_2) == in_order_2


def test_post_order_empty():
    assert trees.post_order(binary_tree_2) == []


in_order_3 = ['A']
pre_order_3 = ['A']
binary_tree_3 = trees.build_binary_tree(
    preorder=pre_order_3,
    inorder=in_order_3
)


def test_pre_order_one_elem():
    assert trees.pre_order(binary_tree_3) == pre_order_3


def test_in_order_one_elem():
    assert trees.in_order(binary_tree_3) == in_order_3


def test_post_order_one_elem():
    assert trees.post_order(binary_tree_3) == ['A']


in_order_4 = ['A', 'B', 'C', 'D']
pre_order_4 = ['E', 'F', 'G', 'H']


def test_bad_data():
    with pytest.raises(ValueError) as excinfo:
        binary_tree_4 = trees.build_binary_tree(
            preorder=pre_order_4,
            inorder=in_order_4
        )
    assert 'is not in list' in str(excinfo.value)


pre_order_5 = ['A', 'B', 'D', 'E', 'C', 'F']
in_order_5 = ['D', 'B', 'E', 'A', 'F', 'C']
binary_tree_5 = trees.build_binary_tree(
            preorder=pre_order_5,
            inorder=in_order_5
        )


def test_is_full_binary_tree_negative():
    assert trees.is_full_binary_tree(binary_tree_5) == False


pre_order_6 = ['A']
in_order_6 = ['A']
binary_tree_6 = trees.build_binary_tree(
            preorder=pre_order_6,
            inorder=in_order_6
        )


def test_is_full_binary_tree_positive():
    assert trees.is_full_binary_tree(binary_tree_6)


def test_binary_tree_depth():
    assert trees.depth_of_tree(binary_tree_5) == 3
    assert trees.depth_of_tree(binary_tree_6) == 1




def test_binary_tree_diameter():
    assert trees.diameter(binary_tree_6) == 1
    assert trees.diameter(binary_tree_5) == 5
    assert trees.diameter(binary_tree_2) == 0

    binary_tree_7 = trees.Node("A")
    binary_tree_7.left = trees.Node("B")
    binary_tree_7.left.left = trees.Node("C")
    binary_tree_7.left.right = trees.Node("D")
    binary_tree_7.left.left.left = trees.Node("E")
    binary_tree_7.left.left.left.left = trees.Node("F")
    binary_tree_7.left.right.right = trees.Node("G")
    binary_tree_7.left.right.right.right = trees.Node("H")

    assert trees.diameter(binary_tree_7) == 7

