from typing import TypeVar, Generic
import json

DataType = TypeVar("DataType", int, float, str, bool)


class Stack(Generic[DataType]):
    def __init__(self, size: int, items: list[DataType] | None = None) -> None:
        self.size = size
        self.items: list[DataType] = [] if items is None else items

    def __str__(self) -> str:
        s = json.dumps({"size": self.size, "items": self.items})
        return s

    def push(self, data: DataType) -> None:
        if len(self.items) >= self.size:
            raise Exception("Stack overflow!")
        self.items.append(data)

    def pop(self) -> DataType:
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self.items.pop()

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def peek(self) -> DataType:
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self.items[-1]
