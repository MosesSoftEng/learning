/*
 * Code to demostrate event module in node.js
 */

// Import the events module.
const events = require('events');

// Create an eventEmitter object.
const eventEmitter = new events.EventEmitter();

// Create an event handler function.
const connectEventHandler = function() {
    console.log('connection succesful.');
};

// Bind event with handler
eventEmitter.on('connection', connectEventHandler);

// Fire event.
eventEmitter.emit('connection');