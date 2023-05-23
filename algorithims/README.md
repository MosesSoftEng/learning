# Algorithms.
A step-by-step procedure/ instructions/ rules to solve a specific problem or perform a specific task. It takes some input, process it and produces desired output.

# Sorting Algorithms.
An algorithm designed to rearrange elements in a list or array in a specific order, typically in ascending or descending order.

## Selection Sort Ascending.
<div align="center">
  <img src="simple-selection-sort-algorithm.png" alt="Image Description" />
  <p><em>Selection Sort Ascending Illustration.</em></p>
</div>

A sorting algorithm that works by ensuring the left side of list (sorted portion) is sorted as we loop through the list, it then finds the smallest element from unsorted portion and swaps with element in the end of the sorted portion.

### Algorithm approach.
Uses the "in-place comparison" approach to sorting. 

### Pseudocode for selection sort.
```commandline
procedure selectionSort(array)
    n = length of array
    for i from 0 to n-1 do
        minIndex = i
        for j from i+1 to n do
            if element at index j is smaller than element at index minIndex then
                minIndex = j
            end if
        end for
        swap element at index i with element at index minIndex
    end for
end procedure
```

### Time Complexity:
 - Best case: O(n^2)
 - Average case: O(n^2)
 - Worst case: O(n^2)

In selection sort, there are two nested loops.

### Space Complexity:
 - Selection sort has a space complexity of O(1) (constant space).
 - It performs the sorting in-place, meaning it does not require additional space proportional to the input size.
 - The only extra space used is for temporary variables during swapping, which remains constant regardless of the input size.

[👉 See Code](sorting-algorithims/simple-selection-sort-algorithm.py) | 
[▶️ Run Code](https://onecompiler.com/python/3z9enay29)
