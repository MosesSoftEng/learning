// Import buffer module using require global function.
const buffer = require('buffer');

// Create a new buffer object using allocUnsafe Buffer class method,
//	of size 10 bytes
const myBuffer = buffer.Buffer.allocUnsafe(10);
console.log(myBuffer);

// Initialize buffer with string hello.
myBuffer.write('hello');
console.log(myBuffer.toString());
