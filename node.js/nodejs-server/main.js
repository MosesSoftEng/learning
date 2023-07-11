// Import http module using node.js require built-in function.
const httpModule = require('http');

// Creates a new HTTP server instance.
const server = httpModule.createServer(
    // Callback function as parameter which itself has two parameters; request and response.
    (request, response) => {
        // Send HTTP response header with HTTP status 200, content type text/plain
        response.writeHead(
            200,
            {
                'Content-Type': 'text/plain'
            }
        );

        // Send response body
        response.end('Hello World\n');
    }
);

server.listen(
    // port
    3000,
    // Hostname default 0.0.0.0 or ::
    'localhost',
    // Callback function executed when the server has started listening for incoming connections.
    () => {
        console.log('Server running at http://localhost:3000/');
    }
);
