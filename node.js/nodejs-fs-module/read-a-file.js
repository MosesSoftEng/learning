// Import fs module using node.js global require function.
const fs = require('fs');

const fileName = 'data.txt';

/*
 * Read file data using fs readFile() function.
 */
// Asynchronous file read.
fs.readFile(fileName, 'utf-8', (error, fileData) => {
	if (error) {
		console.log('error: ', error.message);
	} else {
		console.log('Asychronous file data: ', fileData);
	}
});

// Synchronous file read.
const data = fs.readFileSync(fileName, 'utf-8');
console.log('Synchronous File data', data);
