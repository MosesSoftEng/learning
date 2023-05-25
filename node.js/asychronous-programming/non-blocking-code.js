/*
 * Non-blocking code.
 */
function longTask(ms, callbackFunction) {
    const start = Date.now();
    let num = 0;
    function incrementNum() {
        num++;
        if (Date.now() - start < ms) {
            // 
            setImmediate(incrementNum);
        } else {
            callbackFunction(num);
        }
    }
    setImmediate(incrementNum);
}

longTask(3000, function(num) {
    console.log('Task complete, num: ', num);
});

console.log('Program ended');
