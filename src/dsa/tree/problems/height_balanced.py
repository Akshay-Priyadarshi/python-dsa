from typing import Optional
from tree.implementation import TreeNode
from src.helpers.custom_typevars import ComparableType
from tree.problems.height import get_height


def is_height_balanced_naive(node: Optional[TreeNode[ComparableType]]) -> bool:
    if node is None:
        return True
    return (
        abs(get_height(node.left) - get_height(node.right)) <= 1
        and is_height_balanced_naive(node.left)
        and is_height_balanced_naive(node.right)
    )


def is_height_balanced(node: Optional[TreeNode[ComparableType]]):
    def _get_height(node: Optional[TreeNode[ComparableType]]) -> int:
        if node is None:
            return 0
        lh = _get_height(node.left)
        rh = _get_height(node.right)
        if abs(lh - rh) > 1:
            return -1
        ch = max(lh, rh) + 1
        return ch

    if _get_height(node) == -1:
        return False
    return True
