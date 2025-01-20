const http = require('http');

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Welcome to the prod version of chatza defang. You will need to use dev for now\n');
});

server.listen(3000, '0.0.0.0', () => {
    console.log('Server running at http://127.0.0.1:3000/');
});
