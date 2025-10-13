# DOM (Document Object Model) - Complete Guide from Zero

## What is DOM?

The **Document Object Model (DOM)** is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as nodes and objects; that way, programming languages can interact with the page.

### Key Concepts:
- **Document**: The entire HTML document
- **Element**: HTML tags like `<div>`, `<p>`, `<h1>`, etc.
- **Node**: Every part of the document (elements, text, attributes)
- **Tree Structure**: DOM represents HTML as a tree of nodes

## DOM Tree Structure

```
Document
    └── html
        ├── head
        │   ├── title
        │   └── meta
        └── body
            ├── h1
            ├── p
            └── div
                ├── span
                └── button
```

## DOM Selection Methods

### 1. getElementById()
Selects an element by its `id` attribute.

```javascript
// HTML: <div id="myDiv">Hello World</div>
const element = document.getElementById('myDiv');
console.log(element.textContent); // "Hello World"
```

### 2. getElementsByClassName()
Selects elements by their `class` attribute (returns HTMLCollection).

```javascript
// HTML: <p class="highlight">Text 1</p> <p class="highlight">Text 2</p>
const elements = document.getElementsByClassName('highlight');
console.log(elements.length); // 2
console.log(elements[0].textContent); // "Text 1"
```

### 3. getElementsByTagName()
Selects elements by tag name (returns HTMLCollection).

```javascript
// Selects all <p> elements
const paragraphs = document.getElementsByTagName('p');
console.log(paragraphs.length);
```

### 4. querySelector()
Selects the **first** element that matches a CSS selector.

```javascript
// By ID
const byId = document.querySelector('#myDiv');

// By Class
const byClass = document.querySelector('.highlight');

// By Tag
const byTag = document.querySelector('p');

// By Attribute
const byAttr = document.querySelector('[data-id="123"]');

// Complex selector
const complex = document.querySelector('div.container > p.text');
```

### 5. querySelectorAll()
Selects **all** elements that match a CSS selector (returns NodeList).

```javascript
const allHighlights = document.querySelectorAll('.highlight');
const allParagraphs = document.querySelectorAll('p');

// Convert NodeList to Array for more methods
const paragraphsArray = Array.from(allParagraphs);
```

## DOM Manipulation

### 1. Changing Content

#### textContent vs innerHTML
```javascript
const element = document.getElementById('myDiv');

// textContent - sets/gets text only (safe from XSS)
element.textContent = 'New text content';

// innerHTML - sets/gets HTML content (can be dangerous)
element.innerHTML = '<strong>Bold text</strong>';

// innerText - similar to textContent but respects styling
element.innerText = 'Visible text only';
```

### 2. Changing Attributes

```javascript
const img = document.querySelector('img');

// Get attribute
const src = img.getAttribute('src');

// Set attribute
img.setAttribute('src', 'new-image.jpg');
img.setAttribute('alt', 'New description');

// Remove attribute
img.removeAttribute('title');

// Direct property access (for common attributes)
img.src = 'another-image.jpg';
img.id = 'newId';
```

### 3. Changing Styles

```javascript
const element = document.getElementById('myDiv');

// Individual style properties
element.style.color = 'red';
element.style.backgroundColor = 'yellow';
element.style.fontSize = '20px';

// CSS property names with hyphens become camelCase
element.style.borderRadius = '10px';
element.style.marginTop = '15px';

// Using cssText to set multiple styles
element.style.cssText = 'color: blue; background: white; padding: 10px;';
```

### 4. Working with Classes

```javascript
const element = document.getElementById('myDiv');

// Add class
element.classList.add('newClass');
element.classList.add('class1', 'class2', 'class3');

// Remove class
element.classList.remove('oldClass');

// Toggle class (add if not present, remove if present)
element.classList.toggle('active');

// Check if class exists
if (element.classList.contains('highlight')) {
    console.log('Element has highlight class');
}

// Replace class
element.classList.replace('oldClass', 'newClass');
```

## Creating and Removing Elements

### Creating Elements

```javascript
// Create new element
const newDiv = document.createElement('div');
newDiv.textContent = 'I am a new div';
newDiv.className = 'dynamic-element';
newDiv.id = 'newDiv';

// Create text node
const textNode = document.createTextNode('Just text');

// Add to DOM
document.body.appendChild(newDiv);

// Insert at specific position
const container = document.getElementById('container');
const firstChild = container.firstElementChild;
container.insertBefore(newDiv, firstChild);
```

### Removing Elements

```javascript
const element = document.getElementById('toRemove');

// Modern way (preferred)
element.remove();

// Older way
element.parentNode.removeChild(element);

// Remove all children
const container = document.getElementById('container');
container.innerHTML = ''; // Quick way
// OR
while (container.firstChild) {
    container.removeChild(container.firstChild);
}
```

## Event Handling

### Adding Event Listeners

```javascript
const button = document.getElementById('myButton');

// Method 1: addEventListener (recommended)
button.addEventListener('click', function() {
    console.log('Button clicked!');
});

// Method 2: Arrow function
button.addEventListener('click', () => {
    console.log('Button clicked with arrow function!');
});

// Method 3: Named function
function handleClick(event) {
    console.log('Button clicked!', event);
}
button.addEventListener('click', handleClick);

// Method 4: Inline (not recommended)
// <button onclick="handleClick()">Click me</button>
```

### Common Events

```javascript
const input = document.getElementById('myInput');
const form = document.getElementById('myForm');

// Input events
input.addEventListener('input', (e) => {
    console.log('Input value:', e.target.value);
});

input.addEventListener('focus', () => {
    console.log('Input focused');
});

input.addEventListener('blur', () => {
    console.log('Input lost focus');
});

// Form events
form.addEventListener('submit', (e) => {
    e.preventDefault(); // Prevent form submission
    console.log('Form submitted');
});

// Mouse events
button.addEventListener('mouseenter', () => {
    console.log('Mouse entered button');
});

button.addEventListener('mouseleave', () => {
    console.log('Mouse left button');
});

// Keyboard events
document.addEventListener('keydown', (e) => {
    console.log('Key pressed:', e.key);
});
```

### Event Object Properties

```javascript
button.addEventListener('click', (event) => {
    console.log('Event type:', event.type);
    console.log('Target element:', event.target);
    console.log('Current target:', event.currentTarget);
    console.log('Mouse coordinates:', event.clientX, event.clientY);
    
    // Prevent default behavior
    event.preventDefault();
    
    // Stop event bubbling
    event.stopPropagation();
});
```

## DOM Traversal

### Parent, Child, and Sibling Navigation

```javascript
const element = document.getElementById('myElement');

// Parent navigation
const parent = element.parentNode;
const parentElement = element.parentElement;

// Child navigation
const children = element.children; // HTMLCollection of child elements
const firstChild = element.firstElementChild;
const lastChild = element.lastElementChild;
const childNodes = element.childNodes; // All nodes (including text)

// Sibling navigation
const nextSibling = element.nextElementSibling;
const prevSibling = element.previousElementSibling;

// Check if element has children
if (element.hasChildNodes()) {
    console.log('Element has children');
}
```

## Practical Examples

### Example 1: Dynamic List Management

```javascript
// HTML needed:
// <ul id="todoList"></ul>
// <input id="todoInput" type="text" placeholder="Enter todo">
// <button id="addTodo">Add Todo</button>

const todoList = document.getElementById('todoList');
const todoInput = document.getElementById('todoInput');
const addButton = document.getElementById('addTodo');

function addTodo() {
    const todoText = todoInput.value.trim();
    
    if (todoText === '') {
        alert('Please enter a todo item');
        return;
    }
    
    // Create list item
    const li = document.createElement('li');
    li.textContent = todoText;
    
    // Create delete button
    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete';
    deleteBtn.style.marginLeft = '10px';
    
    // Add delete functionality
    deleteBtn.addEventListener('click', () => {
        todoList.removeChild(li);
    });
    
    // Add elements to DOM
    li.appendChild(deleteBtn);
    todoList.appendChild(li);
    
    // Clear input
    todoInput.value = '';
}

// Event listeners
addButton.addEventListener('click', addTodo);

todoInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        addTodo();
    }
});
```

### Example 2: Image Gallery with Modal

```javascript
// HTML needed:
// <div id="gallery"></div>
// <div id="modal" style="display: none;">
//     <span id="closeModal">&times;</span>
//     <img id="modalImage" src="" alt="">
// </div>

const gallery = document.getElementById('gallery');
const modal = document.getElementById('modal');
const modalImage = document.getElementById('modalImage');
const closeModal = document.getElementById('closeModal');

const images = [
    'image1.jpg',
    'image2.jpg',
    'image3.jpg'
];

// Create gallery
images.forEach(imageSrc => {
    const img = document.createElement('img');
    img.src = imageSrc;
    img.style.width = '200px';
    img.style.margin = '10px';
    img.style.cursor = 'pointer';
    
    // Add click event to open modal
    img.addEventListener('click', () => {
        modalImage.src = imageSrc;
        modal.style.display = 'block';
    });
    
    gallery.appendChild(img);
});

// Close modal functionality
closeModal.addEventListener('click', () => {
    modal.style.display = 'none';
});

// Close modal when clicking outside image
modal.addEventListener('click', (e) => {
    if (e.target === modal) {
        modal.style.display = 'none';
    }
});
```

### Example 3: Form Validation

```javascript
// HTML needed:
// <form id="userForm">
//     <input id="username" type="text" placeholder="Username">
//     <input id="email" type="email" placeholder="Email">
//     <input id="password" type="password" placeholder="Password">
//     <button type="submit">Submit</button>
// </form>
// <div id="errors"></div>

const form = document.getElementById('userForm');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const errorsDiv = document.getElementById('errors');

function validateForm(e) {
    e.preventDefault();
    
    const errors = [];
    
    // Clear previous errors
    errorsDiv.innerHTML = '';
    
    // Username validation
    if (username.value.trim().length < 3) {
        errors.push('Username must be at least 3 characters');
    }
    
    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.value)) {
        errors.push('Please enter a valid email');
    }
    
    // Password validation
    if (password.value.length < 6) {
        errors.push('Password must be at least 6 characters');
    }
    
    // Display errors or success
    if (errors.length > 0) {
        const errorList = document.createElement('ul');
        errorList.style.color = 'red';
        
        errors.forEach(error => {
            const li = document.createElement('li');
            li.textContent = error;
            errorList.appendChild(li);
        });
        
        errorsDiv.appendChild(errorList);
    } else {
        errorsDiv.innerHTML = '<p style="color: green;">Form submitted successfully!</p>';
        form.reset();
    }
}

form.addEventListener('submit', validateForm);
```

## Best Practices

### 1. Performance Tips

```javascript
// ❌ Bad: Multiple DOM queries
document.getElementById('myDiv').style.color = 'red';
document.getElementById('myDiv').style.background = 'blue';
document.getElementById('myDiv').textContent = 'Hello';

// ✅ Good: Store reference
const myDiv = document.getElementById('myDiv');
myDiv.style.color = 'red';
myDiv.style.background = 'blue';
myDiv.textContent = 'Hello';

// ❌ Bad: Multiple reflows
element.style.width = '100px';
element.style.height = '100px';
element.style.background = 'red';

// ✅ Good: Batch style changes
element.style.cssText = 'width: 100px; height: 100px; background: red;';
```

### 2. Event Delegation

```javascript
// ❌ Bad: Adding event to each item
const buttons = document.querySelectorAll('.button');
buttons.forEach(button => {
    button.addEventListener('click', handleClick);
});

// ✅ Good: Event delegation
document.getElementById('container').addEventListener('click', (e) => {
    if (e.target.classList.contains('button')) {
        handleClick(e);
    }
});
```

### 3. Wait for DOM to Load

```javascript
// Method 1: DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
    // DOM is fully loaded
    console.log('DOM ready');
});

// Method 2: Check if already loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeApp);
} else {
    initializeApp();
}

function initializeApp() {
    // Your initialization code here
}
```

## Common Mistakes to Avoid

1. **Not checking if element exists**
```javascript
// ❌ Bad
const element = document.getElementById('mayNotExist');
element.style.color = 'red'; // Error if element is null

// ✅ Good
const element = document.getElementById('mayNotExist');
if (element) {
    element.style.color = 'red';
}
```

2. **Using innerHTML with user input**
```javascript
// ❌ Dangerous (XSS vulnerability)
element.innerHTML = userInput;

// ✅ Safe
element.textContent = userInput;
```

3. **Forgetting to remove event listeners**
```javascript
// ❌ Memory leak potential
function addTempListener() {
    button.addEventListener('click', handleClick);
}

// ✅ Clean up when needed
function addTempListener() {
    button.addEventListener('click', handleClick);
    // Later...
    button.removeEventListener('click', handleClick);
}
```

## Conclusion

The DOM is a powerful interface that allows JavaScript to interact with HTML documents. Master these concepts and practice with real projects to become proficient in DOM manipulation. Remember to:

- Always check if elements exist before manipulating them
- Use appropriate selection methods
- Be mindful of performance with large DOM operations
- Handle events properly
- Keep your code clean and readable

Practice these examples and experiment with your own ideas to solidify your understanding!