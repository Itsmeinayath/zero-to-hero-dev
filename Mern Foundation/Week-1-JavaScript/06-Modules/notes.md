Topic 6 — JavaScript Modules

## 1 — What are modules?

Modules let you split code into separate files for better organization and reusability. Each module can export functions, objects, or variables that other files can import.

## 2 — Why use modules?

- **Organization**: Keep code organized in separate files
- **Reusability**: Use the same code in multiple places
- **Maintainability**: Easier to update and debug
- **Namespace**: Avoid variable name conflicts

## 3 — Export (sending code out)

### Named exports

```javascript
// math.js
export function add(a, b) {
  return a + b;
}

export function subtract(a, b) {
  return a - b;
}

export const PI = 3.14159;
```

### Default export

```javascript
// calculator.js
export default class Calculator {
  add(a, b) {
    return a + b;
  }
  
  multiply(a, b) {
    return a * b;
  }
}
```

## 4 — Import (bringing code in)

### Named imports

```javascript
// app.js
import { add, subtract, PI } from './math.js';

console.log(add(5, 3));      // 8
console.log(subtract(10, 4)); // 6
console.log(PI);              // 3.14159
```

### Default import

```javascript
// app.js
import Calculator from './calculator.js';

const calc = new Calculator();
console.log(calc.add(2, 3)); // 5
```

### Import all

```javascript
// app.js
import * as MathUtils from './math.js';

console.log(MathUtils.add(1, 2));  // 3
console.log(MathUtils.PI);         // 3.14159
```

## 5 — Using modules in HTML

Add `type="module"` to your script tag:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Modules Example</title>
</head>
<body>
  <h1>JavaScript Modules</h1>
  
  <!-- Note: type="module" is required -->
  <script type="module" src="app.js"></script>
</body>
</html>
```

## 6 — Common module patterns

### DOM utilities module

```javascript
// dom.js
export function createElement(tag, className, text) {
  const element = document.createElement(tag);
  if (className) element.className = className;
  if (text) element.textContent = text;
  return element;
}

export function getById(id) {
  return document.getElementById(id);
}
```

### API utilities module

```javascript
// api.js
const BASE_URL = 'https://jsonplaceholder.typicode.com';

export async function fetchPosts() {
  const response = await fetch(`${BASE_URL}/posts`);
  return response.json();
}

export async function createPost(data) {
  const response = await fetch(`${BASE_URL}/posts`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  return response.json();
}
```

### Using both modules

```javascript
// app.js
import { createElement, getById } from './dom.js';
import { fetchPosts } from './api.js';

async function displayPosts() {
  const posts = await fetchPosts();
  const container = getById('posts-container');
  
  posts.slice(0, 5).forEach(post => {
    const postDiv = createElement('div', 'post');
    postDiv.innerHTML = `<h3>${post.title}</h3><p>${post.body}</p>`;
    container.appendChild(postDiv);
  });
}

displayPosts();
```

## 7 — Module best practices

- One module per file
- Use clear, descriptive names
- Export only what's needed
- Keep modules focused (single responsibility)
- Use default export for main functionality
- Use named exports for utilities

## Day 6 Task (from 90-Day Plan)

Split your webpage code into modules:
- `dom.js` — DOM manipulation utilities
- `api.js` — API fetch utilities
- `app.js` — Main application logic

Debug module imports and push to GitHub!

See `practice.js` and example files for hands-on exercises.
