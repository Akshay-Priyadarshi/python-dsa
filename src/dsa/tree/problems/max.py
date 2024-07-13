from typing import Optional
import sys
from src.helpers.custom_typevars import NumberType
from src.dsa.tree.implementation import TreeNode


def get_max(node: Optional[TreeNode[NumberType]] = None) -> NumberType:
    if node is None:
        return -sys.maxsize
    m: NumberType = max(get_max(node.left), get_max(node.right), node.data)
    return m
