from typing import Generic, Optional
import json
from src.helpers.custom_typevars import ComparableType


class LinkedListNode(Generic[ComparableType]):
    def __init__(
        self, next: Optional["LinkedListNode[ComparableType]"], data: ComparableType
    ) -> None:
        self.data: ComparableType = data
        self.next: Optional["LinkedListNode[ComparableType]"] = next

    def __str__(self) -> str:
        return json.dumps({"data": self.data})


class SinglyLinkedList(Generic[ComparableType]):
    def __init__(self, head: LinkedListNode[ComparableType]) -> None:
        self.head: Optional[LinkedListNode[ComparableType]] = head

    def __str__(self) -> str:
        s = ""
        current = self.head
        while current is not None:
            s += f"{current.data} "
            current = current.next
        return s

    @property
    def length(self) -> int:
        current: Optional[LinkedListNode[ComparableType]] = self.head
        items_count: int = 0
        while current is not None:
            items_count += 1
            current = current.next
        return items_count

    @staticmethod
    def recursive_print(node: Optional[LinkedListNode]) -> None:
        if node is None:
            print()
            return
        print(node.data, end=" ")
        SinglyLinkedList.recursive_print(node.next)

    def insert_at_start(self, new_data: ComparableType) -> None:
        new_node = LinkedListNode[ComparableType](None, new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, new_data: ComparableType) -> None:
        new_node = LinkedListNode[ComparableType](None, new_data)
        current: Optional[LinkedListNode[ComparableType]] = self.head
        while current and current.next is not None:
            current = current.next
        if current is not None:
            current.next = new_node

    def insert_at_pos(self, pos: int, new_data: ComparableType) -> None:
        if pos > self.length - 1:
            raise Exception(
                "Cannot insert at pos greater than or equal to the length of linked list"
            )
        new_node = LinkedListNode(None, new_data)
        current = self.head
        i = 0
        while current is not None:
            if i == pos - 2:
                break
            current = current.next
            i += 1
        if current is not None:
            new_node.next = current.next
            current.next = new_node

    def delete_at_start(self) -> None:
        if self.head is not None:
            self.head = self.head.next

    def delete_at_end(self) -> None:
        current = self.head
        if current is not None:
            while current.next is not None and current.next.next is not None:
                current = current.next
            current.next = None

    def search(self, data: ComparableType) -> int:
        """
        Returns the position of the found data, if not found returns -1
        """
        current: Optional[LinkedListNode[ComparableType]] = self.head
        i = 0
        while current is not None:
            if current.data == data:
                return i + 1
            i += 1
            current = current.next
        return -1


class DoublyLinkedListNode(Generic[ComparableType]):
    def __init__(
        self,
        data: ComparableType,
        prev: Optional["DoublyLinkedListNode[ComparableType]"] = None,
        next: Optional["DoublyLinkedListNode[ComparableType]"] = None,
    ) -> None:
        self.data: ComparableType = data
        self.prev: Optional["DoublyLinkedListNode[ComparableType]"] = prev
        self.next: Optional["DoublyLinkedListNode[ComparableType]"] = next

    def __str__(self) -> str:
        return json.dumps(
            {
                "data": self.data,
                "prev": self.prev.data if self.prev is not None else self.prev,
                "next": self.next.data if self.next is not None else self.next,
            }
        )


class DoublyLinkedList(Generic[ComparableType]):
    def __init__(self, head: DoublyLinkedListNode) -> None:
        self.head = head
        self.tail = head

    def __str__(self) -> str:
        s = ""
        current: Optional[DoublyLinkedListNode[ComparableType]] = self.head
        while current is not None:
            s += f"{current.data} "
            current = current.next
        return s

    @property
    def length(self) -> int:
        current: Optional[DoublyLinkedListNode[ComparableType]] = self.head
        items_count = 0
        while current is not None:
            items_count += 1
            current = current.next
        return items_count

    def insert_at_end(self, new_data: ComparableType):
        new_node = DoublyLinkedListNode(new_data, None, None)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current
        self.tail = new_node

    def insert_at_start(self, new_data: ComparableType):
        new_node = DoublyLinkedListNode(new_data, None, None)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def reverse(self):
        current = self.head
        # Make sure to have a prev defined so that we can assign it to head
        first = current
        last = None
        while current is not None:
            current.next, current.prev = current.prev, current.next
            last = current
            current = current.prev
        self.head = last
        self.tail = first

    def delete_at_start(self):
        if self.head.next is None:
            raise Exception("Only one node in linked list!")
        node_to_del = self.head
        new_head = self.head.next
        new_head.prev = None
        self.head = new_head
        del node_to_del

    def delete_at_end(self):
        if self.head.next is None:
            raise Exception("Only one node in linked list!")
        current = self.head
        while current.next.next is not None:
            current = current.next
        node_to_del = current.next
        del node_to_del
        current.next = None
