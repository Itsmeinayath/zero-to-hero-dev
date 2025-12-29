import http from 'http';

// This is a basic web server using Node.js's built-in 'http' module
//this is api 
const server = http.createServer((req, res) => {
    
    // 1. Log the URL so we can see what the browser is asking for
    console.log("User requested:", req.url);

    // 2. ROUTING LOGIC (Traffic Cop)
    if (req.url === '/') {
        // --- HOME PAGE (HTML) ---
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end('<h1>Welcome to the Home Page! 🏠</h1><p>This is served by Node.js</p>');
    
    } else if (req.url === '/about') {
        // --- ABOUT PAGE (HTML) ---
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end('<h1>About Us 👥</h1><p>We are learning Backend Development.</p>');
    
    } else if (req.url === '/api/user') {
        // --- API DATA (JSON) ---
        // This is exactly what you fetched in Day 4! Now YOU are the server sending it.
        const userData = {
            username: "Inayath",
            role: "Developer",
            level: "Junior Backend Engineer"
        };
        
        res.writeHead(200, { 'Content-Type': 'application/json' });
        // We must convert the JS Object to a String before sending
        res.end(JSON.stringify(userData));
    
    } else {
        // --- 404 NOT FOUND ---
        res.writeHead(404, { 'Content-Type': 'text/html' });
        res.end('<h1>404 Error ❌</h1><p>Page not found.</p>');
    }
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});