// Topic 6 — JavaScript Modules Practice
// This is the main app file that imports from other modules

// NOTE: To run this example, you need:
// 1. Create dom.js and api.js files (see below)
// 2. Create an index.html with type="module"
// 3. Run with a local server (not just opening the file)

// === Example: Import from modules ===

// Uncomment when you create the modules:
// import { createElement, getById, toggleVisibility } from './dom.js';
// import { fetchPosts, fetchUserById } from './api.js';


// === Module Examples to Create ===

// CREATE FILE: dom.js
// ==================
/*
export function createElement(tag, className, text) {
  const element = document.createElement(tag);
  if (className) element.className = className;
  if (text) element.textContent = text;
  return element;
}

export function getById(id) {
  return document.getElementById(id);
}

export function toggleVisibility(elementId) {
  const element = getById(elementId);
  element.style.display = element.style.display === 'none' ? 'block' : 'none';
}

export function clearChildren(element) {
  while (element.firstChild) {
    element.removeChild(element.firstChild);
  }
}
*/


// CREATE FILE: api.js
// ==================
/*
const BASE_URL = 'https://jsonplaceholder.typicode.com';

export async function fetchPosts(limit = 10) {
  try {
    const response = await fetch(`${BASE_URL}/posts?_limit=${limit}`);
    if (!response.ok) throw new Error('Failed to fetch posts');
    return await response.json();
  } catch (error) {
    console.error('Error fetching posts:', error);
    throw error;
  }
}

export async function fetchUserById(userId) {
  try {
    const response = await fetch(`${BASE_URL}/users/${userId}`);
    if (!response.ok) throw new Error('User not found');
    return await response.json();
  } catch (error) {
    console.error('Error fetching user:', error);
    throw error;
  }
}

export async function createPost(title, body, userId = 1) {
  try {
    const response = await fetch(`${BASE_URL}/posts`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, body, userId })
    });
    return await response.json();
  } catch (error) {
    console.error('Error creating post:', error);
    throw error;
  }
}
*/


// === Example app.js (main file) ===
/*
import { createElement, getById, clearChildren } from './dom.js';
import { fetchPosts } from './api.js';

async function displayPosts() {
  const container = getById('posts-container');
  clearChildren(container);
  
  // Show loading
  container.appendChild(createElement('p', 'loading', 'Loading posts...'));
  
  try {
    const posts = await fetchPosts(5);
    clearChildren(container);
    
    posts.forEach(post => {
      const postDiv = createElement('div', 'post');
      const title = createElement('h3', '', post.title);
      const body = createElement('p', '', post.body);
      
      postDiv.appendChild(title);
      postDiv.appendChild(body);
      container.appendChild(postDiv);
    });
  } catch (error) {
    clearChildren(container);
    container.appendChild(createElement('p', 'error', 'Error loading posts!'));
  }
}

// Load posts when page loads
displayPosts();
*/


// === HTML File Example ===
/*
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Modules Example</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }
    .post {
      border: 1px solid #ddd;
      padding: 15px;
      margin: 10px 0;
      border-radius: 5px;
    }
    .loading {
      color: #666;
      font-style: italic;
    }
    .error {
      color: red;
    }
  </style>
</head>
<body>
  <h1>JavaScript Modules Demo</h1>
  <div id="posts-container"></div>
  
  <!-- IMPORTANT: type="module" is required! -->
  <script type="module" src="app.js"></script>
</body>
</html>
*/


// === How to run locally ===
// You need a local server because modules use CORS
// Option 1: VS Code Live Server extension
// Option 2: Python: python -m http.server 8000
// Option 3: Node.js: npx http-server

console.log('Modules practice loaded!');
console.log('Create dom.js, api.js, and index.html to test modules.');
