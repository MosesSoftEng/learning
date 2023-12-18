# Fibonacci Sequence.

## Definition of Fibonacci Sequence.

A sequence of numbers starting from 0, then 1 and the following numbers is a sum of the preceding two.

## Example of first 6 Fibonacci numbers.

> 0, 1, 1, 2, 3, 5

|                                  |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | --- |
| index (n)                        | 1   | 2   | 3   | 4   | 5   | 6   |
| Fibonacci number F<sub>(n)</sub> | 0   | 1   | 1   | 2   | 3   | 5   |

5 is the 6<sup>th</sup> Fibonnacci number denoted F<sub>(6)</sub> obtained by summing the preceding two fibonacci number i.e. 3 and 2, the 5<sup>th</sup> and 4<sup>th</sup> Fibonnacci numbers respectively.

**NOTE!** 0 and 1 are **default Fibonnacci number** and are not obtained by any formula!

## Algorithms to find the n<sub>th</sub> Fibonnacci number i.e. F<sub>(n)</sub>.

## Method 1: Recurssive formula.

![fibonacci recurssive formula illutration to find 6th fibonacci number](fibonacci-recurssive-fromula/fibonacci-recurssive-formula-naive-approach.drawio.png)

To find n<sub>th</sub> Fibonnacci number, find and sum the preceding two numbers F<sub>(n-1)</sub> and F<sub>(n-2)</sub>

> F<sub>(n)</sub> = F<sub>(n-1)</sub> + F<sub>(n-2)</sub>

**NOTE!** Above formula does not apply to the two first default Fibonnacci numbers.

### Pseudocode for Recurssive formula using naive approach.

```
function fibonacci(n)
    # Handle default Fibonnacci numbers.
    if n is 0, return 0
    if n is 1, return 1

    # Recurrsive calls.
    return fibonnacci(n-1) + fibonacci(n-2)
```

[Open code implemetation in javascript](./fibonacci-recurssive-fromula/fibonacci-recurssive-formula.js)


### Example run.
```bash
# Get 6th fibonacci number.
node fibonacci-recurssive-formula/fibonacci-recurssive-formula-naive-approach.js 6

5
```

### Time complexity O(2<sup>n</sup>) - Exponential complexity.

Each call, makes two calls (exponential), thus total number of calls is 2<sup>n</sup>. The number of calls increases exponetially with increase in n.

### Space complexity O(n) - Linear complexity.
The number of function calls added to stack is the same for root node to leaf node.


## Method 2: Recurssive formula optimized using memoization.

Store results of already computed Fibonacci numbers and quickly reference instead of recomputing. 


### Pseudocode for Recurssive formula optimized using memoization.

```
function fibonacci(n, memo)
    # Handle default Fibonnacci numbers.
    if n is 0, return 0
    if n is 1, return 1

    if n is saved in memo
        return corresponding fib value

    # Recurrsive calls.
    fib = fibonnacci(n-1) + fibonacci(n-2)

    save n and fib to memo

    return fib.
```


### Example run.
```bash
# Get 6th fibonacci number.
node fibonacci-recurssive-formula/fibonacci-recurssive-formula-optimized-with-memoization.js 6

5
```





