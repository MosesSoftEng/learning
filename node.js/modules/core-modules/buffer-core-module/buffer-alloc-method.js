// Import buffer module.
const buffer = require('buffer');

// Create a buffer using the Buffer class,  size 10 bytes
const myBuffer = buffer.Buffer.alloc(10, 'a');

// Output buffer in hexadecimal format.
console.log(myBuffer);

const string = 'Hello';

// Write the string to the buffer.
myBuffer.write(string, 0, string.length, 'utf8');

// Output buffer in string format.
console.log(myBuffer.toString());
