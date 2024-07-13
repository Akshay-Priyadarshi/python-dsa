from typing import Generic
import json

from src.helpers.custom_typevars import ComparableType


class Queue(Generic[ComparableType]):
    def __init__(self, items: list[ComparableType] | None = None) -> None:
        self.items: list[ComparableType] = [] if items is None else items

    def __str__(self) -> str:
        return json.dumps({"items": self.items})

    def enque(self, new_data: ComparableType) -> None:
        self.items.append(new_data)

    def dequeue(self) -> ComparableType:
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)

    def get_front(self) -> ComparableType:
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]

    def get_rear(self) -> ComparableType:
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return len(self.items) == 0
