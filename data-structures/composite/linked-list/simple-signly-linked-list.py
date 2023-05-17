"""This module provides a simple implementation of a linked list using a class."""
from typing import Union


class Node:
    """
      A class that represents a node in a linked list.

      Attributes:
        data: The data stored in the node.
        next: A reference to the next node in the linked list.
    """

    def __init__(self, data: int) -> None:
        """
        Constructs a new node with the given data.

        Args:
          data: The data to be stored in the node.
        """
        self.next: Union[Node, None] = None
        self.data: int = data

    def __str__(self) -> str:
        """
        Returns a string representation of the node.

        Returns:
          A string representation of the node.
        """
        return str(self.data)


# Create head node.
head: Node = Node(1)

# Add next node.
node2: Node = Node(2)
head.next = node2

# Add next node (tail).
node2.next = Node(3)

# Traverse the linked list from head to tail.
current_node: Node = head
while current_node is not None:
    print(current_node)
    current_node = current_node.next
