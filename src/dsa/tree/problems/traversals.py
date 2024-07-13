from typing import List, Optional

from src.helpers.custom_typevars import ComparableType
from src.dsa.tree.implementation import TreeNode


def print_preorder_traversal(node: Optional[TreeNode[ComparableType]]) -> None:
    if node is None:
        return
    print(node.data)
    print_preorder_traversal(node.left)
    print_preorder_traversal(node.right)


def print_inorder_traversal(node: Optional[TreeNode[ComparableType]]) -> None:
    if node is None:
        return
    print_inorder_traversal(node.left)
    print(node.data)
    print_inorder_traversal(node.right)


def print_postorder_traversal(node: Optional[TreeNode[ComparableType]]) -> None:
    if node is None:
        return
    print_postorder_traversal(node.left)
    print_postorder_traversal(node.right)
    print(node.data)


def print_level_order_traversal(node: Optional[TreeNode[ComparableType]]) -> None:
    queue: List[TreeNode[ComparableType]] = []
    if node is not None:
        queue.append(node)
    while len(queue) != 0:
        current_node = queue.pop(0)
        print(current_node.data)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
