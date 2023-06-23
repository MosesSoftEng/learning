// Import events module.
const events = require('events');

// Create EventEmitter object.
const eventEmitter = new events.EventEmitter();

// Create an Event Handler.
const helloHander = function hello(data = 'no name') {
	console.log(`Hello ${data}`);
};

// Register a Build in Event Name using addListener method.
eventEmitter.addListener('newListener', function(data){
	console.log(`New Event registered: ${data}`);
});

// Bind Event Name 'greet' to Event Handler 'helloHander'
eventEmitter.on('greet', helloHander);

// Fire the connection event passing Event Data optional 'Doe'
eventEmitter.emit('greet', 'Doe');