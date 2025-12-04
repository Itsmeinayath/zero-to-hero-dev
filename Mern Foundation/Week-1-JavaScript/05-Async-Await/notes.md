Topic 5 — Async/Await & Fetch API

## 1 — What is asynchronous JavaScript?

JavaScript is single-threaded, but async operations (like API calls, file reading) don't block code execution. Instead, they run in the background.

## 2 — Promises

A Promise represents a future value (like data from an API).

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('Success!');
  }, 1000);
});

promise.then(result => console.log(result)); // 'Success!' after 1 second
```

## 3 — Async/Await

`async/await` makes asynchronous code look synchronous and easier to read.

```javascript
// Old way with .then()
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data));

// New way with async/await
async function fetchData() {
  const response = await fetch('https://api.example.com/data');
  const data = await response.json();
  console.log(data);
}
```

## 4 — Fetch API

Fetch is used to make HTTP requests (GET, POST, etc.).

```javascript
// GET request
async function getPosts() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts');
    const posts = await response.json();
    console.log(posts);
  } catch (error) {
    console.error('Error fetching posts:', error);
  }
}

getPosts();
```

## 5 — Error handling with try/catch

Always handle errors in async operations.

```javascript
async function fetchUser(id) {
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
    
    if (!response.ok) {
      throw new Error('User not found');
    }
    
    const user = await response.json();
    console.log(user);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

fetchUser(1);
```

## 6 — POST requests

```javascript
async function createPost(postData) {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(postData)
    });
    
    const data = await response.json();
    console.log('Created:', data);
  } catch (error) {
    console.error('Error creating post:', error);
  }
}

createPost({ title: 'My Post', body: 'Hello world', userId: 1 });
```

## Day 4 Task (from 90-Day Plan)

Build a webpage that:
1. Fetches posts from JSONPlaceholder API
2. Displays them dynamically on the page
3. Handles errors with try/catch
4. Shows loading state while fetching

See `practice.js` for hands-on exercises!
