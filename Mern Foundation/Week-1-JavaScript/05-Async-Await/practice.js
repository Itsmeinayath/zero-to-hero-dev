// Topic 5 — Async/Await & Fetch API Practice

// === Exercise 1: Basic Fetch ===
// Fetch and display all posts from JSONPlaceholder
async function getAllPosts() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts');
    const posts = await response.json();
    console.log('All posts:', posts);
  } catch (error) {
    console.error('Error:', error);
  }
}

// Uncomment to run:
// getAllPosts();


// === Exercise 2: Fetch with Error Handling ===
// Fetch a single post by ID, handle invalid IDs
async function getPostById(id) {
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`);
    
    if (!response.ok) {
      throw new Error(`Post ${id} not found`);
    }
    
    const post = await response.json();
    console.log('Post:', post);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Test with valid and invalid IDs:
// getPostById(1);   // Should work
// getPostById(999); // Should show error


// === Exercise 3: Display Posts on Webpage ===
// This function will be used with an HTML page
async function displayPostsOnPage() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=5');
    const posts = await response.json();
    
    const container = document.getElementById('posts-container');
    container.innerHTML = '<h2>Loading...</h2>';
    
    // Simulate loading delay
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    container.innerHTML = '';
    
    posts.forEach(post => {
      const postElement = document.createElement('div');
      postElement.className = 'post';
      postElement.innerHTML = `
        <h3>${post.title}</h3>
        <p>${post.body}</p>
      `;
      container.appendChild(postElement);
    });
  } catch (error) {
    console.error('Error loading posts:', error);
    document.getElementById('posts-container').innerHTML = 
      '<p style="color: red;">Error loading posts. Please try again.</p>';
  }
}

// To use this, create an HTML file with:
// <div id="posts-container"></div>
// <button onclick="displayPostsOnPage()">Load Posts</button>


// === Exercise 4: POST Request ===
// Create a new post
async function createNewPost(title, body) {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        title: title,
        body: body,
        userId: 1
      })
    });
    
    const newPost = await response.json();
    console.log('Created post:', newPost);
  } catch (error) {
    console.error('Error creating post:', error);
  }
}

// Test:
// createNewPost('My First Post', 'This is the content of my post!');


// === Challenge: Fetch Multiple Resources ===
// Fetch user and their posts simultaneously
async function getUserWithPosts(userId) {
  try {
    // Fetch both in parallel using Promise.all
    const [userResponse, postsResponse] = await Promise.all([
      fetch(`https://jsonplaceholder.typicode.com/users/${userId}`),
      fetch(`https://jsonplaceholder.typicode.com/posts?userId=${userId}`)
    ]);
    
    const user = await userResponse.json();
    const posts = await postsResponse.json();
    
    console.log('User:', user);
    console.log('Posts by user:', posts);
  } catch (error) {
    console.error('Error:', error);
  }
}

// Test:
// getUserWithPosts(1);


// === Day 4 Task ===
// TODO: Create a webpage that:
// 1. Has a button to fetch posts
// 2. Shows "Loading..." while fetching
// 3. Displays posts in a nice format
// 4. Handles errors gracefully
// 5. Validates that data is not empty before displaying

console.log('Async/Await exercises loaded. Uncomment functions to test!');
