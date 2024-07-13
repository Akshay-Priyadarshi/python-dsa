from typing import Optional

from src.helpers.custom_typevars import ComparableType
from src.dsa.tree.implementation import TreeNode


def get_height(node: Optional[TreeNode[ComparableType]]) -> int:
    if node is None:
        return 0
    return max(get_height(node.left), get_height(node.right)) + 1
