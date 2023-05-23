"""
This module provides an implementation of the Selection Sort algorithm for sorting a list of integers in
    ascending order.
"""
from typing import List


def swap_list_values(lst_: List[int], i: int, smallest_index: int) -> List[int]:
    """
    Swaps the values between lst[i] and lst[smallest_index] in the given list.

    Args:
        lst_ (List[int]): The input list of integers.
        i (int): The index of the first element to swap.
        smallest_index (int): The index of the second element to swap.

    Returns:
        List[int]: The list with the swapped values.
    """
    temp_value = lst_[i]
    lst_[i] = lst_[smallest_index]
    lst_[smallest_index] = temp_value

    return lst_


def selection_sort(lst_: List[int]) -> List[int]:
    """
    Sorts the given list of integers in ascending order using the Selection Sort algorithm.

    Args:
        lst_ (List[int]): The input list of integers.

    Returns:
        List[int]: The sorted list in ascending order.
    """
    for i in range(len(lst_) - 2):
        smallest_index: int = i

        for j in range(i+1, len(lst_)):
            if lst_[j] < lst_[smallest_index]:
                smallest_index = j

        if smallest_index != i:
            lst_ = swap_list_values(lst_, i, smallest_index)

    return lst_


lst: List[int] = [8, 7, 6, 1, 10]
print(selection_sort(lst))
