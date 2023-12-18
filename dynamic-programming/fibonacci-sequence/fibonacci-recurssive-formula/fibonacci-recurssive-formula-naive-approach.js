const fibonacciNumberIndex = Number.parseInt(process.argv[2]);
// console.log(fibonacciNumberIndex);

/* TODO: Add checks for correct values of fibonacciNumberIndex
    - Check for null.
    - Check for valid number. Number and positve.
    - Provide feedback if invalid number provided.
    - Write tests.
*/

const getFbonacciNumberAtIndex = (index) => {
    // return index;

    // Handle default Fibonnacci numbers.
    if (index === 1 || index === 2) {
        return index - 1;
    }

    // Recurrsive calls.
    return getFbonacciNumberAtIndex(index - 1 ) + getFbonacciNumberAtIndex(index - 2);
}

console.log(getFbonacciNumberAtIndex(fibonacciNumberIndex));
