setInterval(() => {}, 1000); // Keep the event loop busy every 1 second

// Handle process interruption using process global object events.
process.on('SIGINT', () => {
	console.log('Received SIGINT signal');
	// Perform cleanup or shutdown operations
});
