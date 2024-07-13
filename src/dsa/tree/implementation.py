from typing import Generic
from src.helpers.custom_typevars import ComparableType


class TreeNode(Generic[ComparableType]):
    def __init__(
        self,
        data: ComparableType,
        left: "TreeNode[ComparableType]" | None = None,
        right: "TreeNode[ComparableType]" | None = None,
    ) -> None:
        self.data: ComparableType = data
        self.left: TreeNode[ComparableType] | None = left
        self.right: TreeNode[ComparableType] | None = right
