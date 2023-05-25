// blocking code
function longTask(ms) {
    const start = Date.now();
    let num = 0;
    while (Date.now() - start < ms);
    console.log('Task complete');
}

longTask(3000);
console.log('Program ended');
