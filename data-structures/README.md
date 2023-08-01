# Data Structures

# [Linked List](composite-data-structures/linked-list/)
## [Simple Singly Linked List](composite-data-structures/linked-list/simple-singly-linked-list.py)
<div align="center">
  <img src="composite/linked-list/simple-singly-linked-list.png" alt="Image Description" />
  <p><em>Simple Singly Linked List Illustration.</em></p>
</div>

The code implements a singly linked list using the Node class, initializing nodes with data and connections. It traverses the list and prints data, showcasing linked list implementation in Python.

### Reverse singly linked list function.
Pseudocode for reversing singly linked list.

```commandline
Start at the beginning of the list (head).
Keep track of the previous node (previous_node) initially as None.
While there are still nodes in the list:
    Save the next node (next_node) of the current node (current_node) before modifying any pointers.
    Update the next pointer of the current node to point to the previous node. This reverses the link.
    Move the previous_node to the current node and the current node to the next node to continue to the next pair of nodes.
After the loop ends, the last node processed becomes the new head of the reversed list, so update head to be the previous_node.
```
[👉 See Code](composite-data-structures/linked-list/simple-singly-linked-list.py) | 
[▶️ Run Code](https://onecompiler.com/python/3z8c8muhx)

## [Advanced Singly Linked List](composite-data-structures/linked-list/advanced-singly-linked-list.py)
The code implements a singly linked list data structure in Python, allowing insertion, deletion, size calculation, and reversal of the list, showcasing linked list implementation in Python.
