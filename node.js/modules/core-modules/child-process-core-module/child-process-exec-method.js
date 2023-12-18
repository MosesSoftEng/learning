/*
 * Execute python command in a child process using exec method.
 */

// Import child process and assign exec method to a variable.
const exec = require('child_process').exec;

const pythonCode = 'print("Hello, Python!")';

exec(`python3 -c '${pythonCode}'`, (error, stdout, stderr) =>{
	if(error) {
		console.error('Error:', error.message);
		return;
	}
	
	if(stderr) {
		console.error('Python Error:', stderr);
		return;
	} 

	console.log(stdout);
});
