import express from 'express';

const app  =express();
const PORT = 3000;

app.get('/', (req, res) => {
    res.send('<h1>Hello,Welcome to my Express server!</h1>');
});

app.get('/about', (req, res) => {
    res.send('<h1>This is the about page of my Express server.</h1>');
}); 

app.get('/api/user', (req, res) => {
const user = {
    username : "john_doe",
    role : "admin",
    framework : "Express"
};
res.json(user);
});


app.use((req, res) => {
    res.status(404).send('<h1>404 Not Found</h1><p>The page you are looking for does not exist.</p>');
    })

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
