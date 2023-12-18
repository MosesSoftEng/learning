# Modules.
Re-usable block of code that encapsulates related functions, classes or variables used to organize code into separate files.

## Types of modules.
1. Core modules - built-in modules that are included with Node.js.
2. Third-party modules - modules that are created by other developers and published to the Node Package Manager.
3. User-defined modules - modules defined by developer.


1. CommonJs Modules.
2. ECMAScript Modules.

## Node.js Core Modules.
Built-in modules that come bundled with Node.js runtime environment.

### [Child Process Core Module.](./core-modules/child-process-core-module/)
A core Node.js module that provides functionality to create and manage child processes.

### child_process.exec() method.
A method in child_process that runs commands in a console and buffers the output.

#### [Example: Execute python code using python -c command in terminal and show result](./core-modules/child-process-core-module/child-process-exec-method.js)
```javascript
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
```

### [Events Core Module.](./core-modules/events-core-module/)

#### EventEmimitter Class.
A built-in class in Node.js event core module that provides a way for objects to emit events.

##### Components of EventEmiiter Class.
1. Event Emitters: Instances of the EventEmitter class or objects which have extend the class. They have the ability to emit events and event handling.
2. Event Listeners or Handlers: Callbacks (functions) that are registered to handle specific events emitted by Event Emitter and listen for emitted events and execute associated functions when event occurs. Attached to Event Emitters using methods as: on, addListener, once.
3. Event Handlers: Callbacks (functions) associated with event Listeners and define logic to be per-formed when an event is emitted/ triggered.
4. Event Names: Unique identifier representing specific occurrence or actions. Can be predefined/ built-in or custom-defined.
5. Event Data or Arguments: Optional info associated with an event, accessible to Event Listeners and Handlers.

##### [Example: Create a custom called greet that print out Hello Doe](./core-modules/events-core-module/custom-event-using-event-emitter-class.js)
```bash
# Run script.
node ./core-modules/events-core-module/custom-event-using-event-emitter-class.js
```

##### EventEmitter Built-in Event Names.
Include: error, newListener, removeListener, listening and unlistening.

### [Buffer Core Module.](./core-modules/buffer-core-module/)
Node.js core module that provides API for handling binary data: Reading, writing, and manipulating binary data/ raw bytes.

##### [Example: Write string to buffer](./core-modules/buffer-core-module/buffer-write-method.js)
```bash
node ./core-modules/buffer-core-module/buffer-alloc-method.js

node ./core-modules/buffer-core-module/buffer-allocUnsafe-method.js
```



