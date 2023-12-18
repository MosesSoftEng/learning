from typing import Union

class Node:
    """
    A class that represents a node in a linked list.

    Attributes:
        data: The data stored in the node.
        next: A reference to the next node in the linked list.
    """

    def __init__(self, data: Union[int, None]) -> None:
        """
        Constructs a new node with the given data.

        Args:
            data: The data to be stored in the node.
        """
        self.next: Union[Node, None] = None
        self.data = data

    def __str__(self) -> str:
        """
        Returns a string representation of the node.

        Returns:
            A string representation of the node.
        """
        return str(self.data)


class LinkedList:
    """
    A class that represents a singly linked list.

    Attributes:
        head: The head node of the linked list.
    """

    def __init__(self) -> None:
        """
        Constructs an empty linked list.
        """
        self.head = Node(None)

    def __str__(self) -> str:
        """
        Returns a string representation of the linked list.

        Returns:
            A string representation of the linked list.
        """
        return str(self.head)

    def insert_at_tail(self, data: int) -> None:
        """
        Inserts a new node with the given data at the tail of the linked list.

        Args:
            data: The data to be stored in the new node.
        """
        current_node = self.head

        # Traverse to the end of the list.
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data)

    def delete_at_tail(self) -> None:
        """
        Deletes the node at the tail of the linked list.
        """
        current_node: Node = self.head

        # Traverse to the second last node in the list.
        while current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    def size(self) -> int:
        """
        Returns the size of the linked list.

        Returns:
            The size of the linked list.
        """
        size: int = 0
        current_node: Node = self.head

        while current_node:
            size += 1
            current_node = current_node.next

        return size

    def reverse(self) -> None:
        """
        Reverses the linked list in-place.
        """
        current_node: Node = self.head
        previous_node: Union[Node, None] = None

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def __str__(self) -> str:
        """
        Returns a string representation of the linked list.

        Returns:
            A string representation of the linked list.
        """
        str_rep_list: list[str] = []
        current_node = self.head

        while current_node:
            str_rep_list.append(str(current_node))
            current_node = current_node.next

        return ' -> '.join(str_rep_list)


linkedList: LinkedList = LinkedList()
linkedList.insert_at_tail(0)
linkedList.insert_at_tail(1)
linkedList.insert_at_tail(2)
linkedList.insert_at_tail(3)
linkedList.insert_at_tail(4)
linkedList.delete_at_tail()

print(linkedList)

linkedList.reverse()

print()
print('Reversed linked list')
print(linkedList)

print('Size:', linkedList.size())
