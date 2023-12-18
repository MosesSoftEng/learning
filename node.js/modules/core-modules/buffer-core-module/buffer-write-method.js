// Import buffer module.
const bufferModule = require('buffer');

// Create a buffer using the Buffer class,  size 10 bytes
const buffer = new bufferModule.Buffer(10);

const string = 'Hello';

// Write the string to the buffer.
buffer.write(string, 0, string.length, 'utf8');

// Output buffer in string format.
console.log(buffer.toString());
