const fibonacciNumberIndex = Number.parseInt(process.argv[2]);
// console.log(fibonacciNumberIndex);

/* TODO: Add checks for correct values of fibonacciNumberIndex
    - Check for null.
    - Check for valid number. Number and positve.
    - Provide feedback if invalid number provided.
    - Write tests.
*/

/*
 * Making use of JavaScript Objects (Hash Maps) to store and retrieve computed
 *  fibonacci numbers.
 */ 

const getFbonacciNumberAtIndex = (index, memo = {}) => {
    // return index;

    // Handle default Fibonnacci numbers.
    if (index === 1 || index === 2) {
        return index - 1;
    }

    // Check if already saved in memo.
    if (memo[index]) {
        return memo[index];
    }

    // Recurrsive calls.
    const fibonacciNumber = getFbonacciNumberAtIndex(index - 1, memo) + getFbonacciNumberAtIndex(index - 2, memo);
    memo[index] = fibonacciNumber;

    return fibonacciNumber;
}

console.log(getFbonacciNumberAtIndex(fibonacciNumberIndex));
