var http = require('http');

var requestHandler = (req, res) => {
    console.log("request received")
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end('Hello World');
};

http.createServer(requestHandler).listen(8080);

console.log("hello world")


// MERN 
// MongoDB

// MySQL

// Express
// React
// NodeJS
