# 📘 DOM (Document Object Model) - The Master Guide

## 📚 Table of Contents

- [What is the DOM?](#1-what-is-the-dom)
- [Selection Methods](#2-selection-methods-the-hook-)
- [Manipulation](#3-manipulation-the-change-)
- [Creating & Moving Elements](#4-creating--moving-elements-)
- [Event Handling](#5-event-handling-the-ear-)
- [Traversal (Parent, Child, Sibling)](#6-dom-traversal-)
- [Senior Design Patterns](#7-senior-design-patterns-)
- [Common Mistakes to Avoid](#8-common-mistakes-to-avoid-)

---

## 1. What is the DOM?

The **Document Object Model (DOM)** is a programming interface for web documents. It represents the page structure as a "Tree" of objects that JavaScript can read, change, and listen to.

### Visualizing the Tree

```
                    document
                       │
                      html
                    /      \
                head        body
               /    \      /    \
            title  meta   nav    div
                          │       │
                          p      h1
```

> 💡 Think of the DOM as an upside-down tree. The "Root" is the Document, and every HTML tag is a "Branch" or "Leaf" (Node).

### Key Concepts

| Term | Description |
|------|-------------|
| **Document** | The entry point (global `document` object) |
| **Element** | HTML tags like `<div>`, `<p>`, `<h1>` |
| **Node** | Every part of the tree (elements, text, comments) |

---

## 2. Selection Methods (The "Hook") 🪝

Before you can change an element, you must find it.

### Single Element Selectors

*Returns the **first** matching element or `null` if not found.*

| Method | Selector Type | Speed | Example |
|--------|--------------|-------|---------|
| `getElementById('id')` | ID only | ⚡ Fastest | `getElementById('app')` |
| `querySelector('.class')` | Any CSS | ⚡ Fast | `querySelector('.box')` |

```javascript
// By ID
const header = document.getElementById('header');

// By CSS Selector (Recommended - more flexible)
const header = document.querySelector('#header');      // ID
const box = document.querySelector('.box');            // Class
const firstP = document.querySelector('p');            // Tag
const activeItem = document.querySelector('li.active'); // Combined
```

### Multi-Element Selectors

*Returns a **collection** of all matching elements.*

| Method | Returns | Live? | forEach? |
|--------|---------|-------|----------|
| `querySelectorAll('.item')` | NodeList | ❌ Static | ✅ Yes |
| `getElementsByClassName('item')` | HTMLCollection | ✅ Live | ❌ No |
| `getElementsByTagName('p')` | HTMLCollection | ✅ Live | ❌ No |

```javascript
// ✅ Recommended - Static NodeList (safer)
const items = document.querySelectorAll('.item');
items.forEach(item => item.style.color = 'red');

// ⚠️ Live HTMLCollection (auto-updates, can cause bugs)
const items = document.getElementsByClassName('item');
for (let i = 0; i < items.length; i++) {
    items[i].style.color = 'red';
}
```

### ⚠️ Live vs Static - Key Difference!

```javascript
// LIVE Collection - Auto-updates!
const live = document.getElementsByClassName('item');
console.log(live.length);  // 3

// Add new element with class "item"...
console.log(live.length);  // 4 (auto-updated!)

// STATIC Collection - Snapshot in time
const static = document.querySelectorAll('.item');
console.log(static.length);  // 3

// Add new element...
console.log(static.length);  // Still 3! (doesn't update)
```

**Visual:**
```
LIVE Collection:              STATIC Collection:
┌─────────────┐              ┌─────────────┐
│ Item 1      │              │ Item 1      │
│ Item 2      │              │ Item 2      │
│ Item 3      │              │ Item 3      │
│ Item 4 NEW! │ ← Included   └─────────────┘ ← Item 4 NOT included
└─────────────┘
```

---

## 3. Manipulation (The "Change") 🎨

### Changing Text Content

| Property | Parses HTML? | Reads Hidden? | Security |
|----------|-------------|---------------|----------|
| `textContent` | ❌ No | ✅ Yes | ✅ Safe |
| `innerText` | ❌ No | ❌ No | ✅ Safe |
| `innerHTML` | ✅ Yes | ✅ Yes | ⚠️ XSS Risk |

```javascript
const message = document.querySelector('#msg');

// ✅ textContent (Best Practice) - Safe & Fast
message.textContent = 'Hello <script>';
// Output: Hello <script>  (shows as text, script won't run)

// ⚠️ innerHTML - Parses HTML (XSS risk with user input!)
message.innerHTML = '<strong>Bold</strong>';
// Output: Bold  (actually bold)

// 😐 innerText - Ignores hidden elements, slower
message.innerText = 'Visible text only';
```

**Visual: textContent vs innerHTML**
```
Code: element.textContent = '<b>Hello</b>'
Output: <b>Hello</b>  (plain text, tags visible)

Code: element.innerHTML = '<b>Hello</b>'
Output: Hello  (bold text, tags parsed)
```

### Changing Attributes

```javascript
const img = document.querySelector('img');

// ✅ Direct property access (Modern)
img.src = 'avatar.png';
img.alt = 'User Avatar';
img.id = 'profile-pic';

// getAttribute/setAttribute (older, but works for any attribute)
img.getAttribute('src');
img.setAttribute('src', 'new-image.png');
```

### Data Attributes (dataset API)

```html
<div id="user" data-id="55" data-role="admin" data-is-active="true"></div>
```

```javascript
const user = document.querySelector('#user');

// ✅ Access via dataset
console.log(user.dataset.id);       // "55"
console.log(user.dataset.role);     // "admin"
console.log(user.dataset.isActive); // "true" (camelCase!)

// Set data attributes
user.dataset.score = "100";
// HTML becomes: data-score="100"
```

### Working with Classes (classList API)

```javascript
const btn = document.querySelector('.btn');

// ADD classes
btn.classList.add('active');
btn.classList.add('active', 'shadow');  // Multiple

// REMOVE classes
btn.classList.remove('disabled');

// TOGGLE (add if missing, remove if present)
btn.classList.toggle('dark-mode');

// CHECK if class exists
if (btn.classList.contains('active')) {
    console.log('Button is active!');
}

// REPLACE class
btn.classList.replace('old-class', 'new-class');
```

**Visual: classList.toggle()**
```
FIRST CLICK:                  SECOND CLICK:
┌──────────┐                 ┌──────────┐
│ ☀️ Light │  → toggle →    │ 🌙 Dark  │  → toggle →  ☀️ Light
└──────────┘                 └──────────┘
(adds 'dark-mode')           (removes 'dark-mode')
```

### Changing Styles

```javascript
const box = document.querySelector('.box');

// Single styles
box.style.color = 'red';
box.style.backgroundColor = 'yellow';  // camelCase!
box.style.fontSize = '20px';

// Multiple styles at once
box.style.cssText = 'color: red; background: yellow; padding: 10px;';

// Remove inline style
box.style.color = '';  // Removes the color style
```

---

## 4. Creating & Moving Elements 🏗️

### Creating Elements

```javascript
// 1. Create element (in memory)
const newDiv = document.createElement('div');

// 2. Add content & attributes
newDiv.textContent = 'I am brand new!';
newDiv.classList.add('alert-box');
newDiv.id = 'notification';

// 3. Add to DOM
const parent = document.querySelector('body');
```

### Adding Elements - Old vs Modern

| Old Method | Modern Method | Difference |
|-----------|--------------|------------|
| `appendChild(node)` | `append(node)` | append() can add text too |
| `insertBefore(new, ref)` | `before(node)` | Cleaner syntax |
| N/A | `after(node)` | Insert after element |
| N/A | `prepend(node)` | Insert as first child |

```javascript
const parent = document.querySelector('.container');
const newEl = document.createElement('div');
newEl.textContent = 'New Element';

// ✅ Modern Methods
parent.append(newEl);           // Add as last child
parent.prepend(newEl);          // Add as first child
existingEl.before(newEl);       // Add before existing element
existingEl.after(newEl);        // Add after existing element

// Can add multiple items AND text
parent.append(newEl, ' Some text', anotherEl);
```

**Visual: Insert Positions**
```
parent.prepend(new)  →  NEW | Child 1 | Child 2 | Child 3
parent.append(new)   →  Child 1 | Child 2 | Child 3 | NEW
child2.before(new)   →  Child 1 | NEW | Child 2 | Child 3
child2.after(new)    →  Child 1 | Child 2 | NEW | Child 3
```

### Removing Elements

```javascript
const trash = document.querySelector('.trash');

// ✅ Modern Way
trash.remove();

// ❌ Old Way
trash.parentNode.removeChild(trash);
```

### Cloning Elements

```javascript
const original = document.querySelector('.card');

// Clone without children
const shallowClone = original.cloneNode(false);

// Clone with all children
const deepClone = original.cloneNode(true);

document.body.append(deepClone);
```

---

## 5. Event Handling (The "Ear") 👂

### Adding Event Listeners

```javascript
const btn = document.querySelector('#save-btn');

btn.addEventListener('click', function(event) {
    console.log('Clicked!');
});

// Arrow function
btn.addEventListener('click', (e) => {
    console.log('Clicked!');
});
```

### Common Events

| Event | Triggers When |
|-------|--------------|
| `click` | Element is clicked |
| `dblclick` | Element is double-clicked |
| `mouseenter` | Mouse enters element |
| `mouseleave` | Mouse leaves element |
| `keydown` | Key is pressed |
| `keyup` | Key is released |
| `submit` | Form is submitted |
| `input` | Input value changes |
| `change` | Input loses focus after change |
| `load` | Page/image finishes loading |
| `DOMContentLoaded` | HTML is fully parsed |

### The Event Object

```javascript
btn.addEventListener('click', (event) => {
    // Prevent default behavior (form submit, link navigation)
    event.preventDefault();

    // Stop event from bubbling up
    event.stopPropagation();

    // Get information
    console.log(event.target);        // Element that was clicked
    console.log(event.currentTarget); // Element with the listener
    console.log(event.type);          // "click"
});
```

### event.target vs event.currentTarget

```html
<div class="parent">
    <button class="child">Click Me</button>
</div>
```

```javascript
parent.addEventListener('click', (e) => {
    console.log(e.target);        // <button> (what you clicked)
    console.log(e.currentTarget); // <div> (where listener is)
});
```

**Visual:**
```
Click on button:
┌─────────────────────────────┐
│  div.parent ← currentTarget │
│    ┌─────────────────┐      │
│    │ button ← target │      │
│    └─────────────────┘      │
└─────────────────────────────┘
```

### Event Bubbling

When you click a button inside a div, the click "bubbles" up:

```
Click happens → button → div → body → html → document
                  ↑
            (bubbles UP)
```

```javascript
// Stop bubbling
btn.addEventListener('click', (e) => {
    e.stopPropagation();  // Event stops here, won't reach parent
});
```

### Keyboard Events

```javascript
document.addEventListener('keydown', (e) => {
    console.log(e.key);   // "Enter", "a", "Escape"
    console.log(e.code);  // "Enter", "KeyA", "Escape"
    
    if (e.key === 'Escape') {
        closeModal();
    }
    
    // Check modifier keys
    if (e.ctrlKey && e.key === 's') {
        e.preventDefault();  // Prevent browser save
        saveDocument();
    }
});
```

---

## 6. DOM Traversal 🧭

### Moving Through the Tree

```html
<ul id="menu">
    <li>Home</li>
    <li id="about">About</li>
    <li>Contact</li>
</ul>
```

```javascript
const about = document.querySelector('#about');

// PARENT
about.parentElement;           // <ul>

// SIBLINGS
about.previousElementSibling;  // <li>Home</li>
about.nextElementSibling;      // <li>Contact</li>

// From parent - CHILDREN
const menu = document.querySelector('#menu');
menu.children;                 // All <li> elements
menu.firstElementChild;        // <li>Home</li>
menu.lastElementChild;         // <li>Contact</li>
menu.children[1];              // <li>About</li>
```

**Visual: Traversal Map**
```
                    parentElement
                         ↑
previousElementSibling ← ELEMENT → nextElementSibling
                         ↓
         ┌───────────────┼───────────────┐
         ↓               ↓               ↓
   firstElementChild  children[1]  lastElementChild
```

### closest() - Find Ancestor

```javascript
// Find nearest ancestor matching selector (searches UP)
const card = button.closest('.card');
const form = input.closest('form');
```

**Visual:**
```
<div class="card">        ← button.closest('.card') finds this!
    <div class="body">
        <button>Click</button>  ← Start here, search UP
    </div>
</div>
```

---

## 7. Senior Design Patterns 🧠

### Pattern A: Event Delegation

Instead of adding 100 listeners to 100 items (slow), add ONE listener to the parent (fast).

```javascript
// ❌ Bad - 100 listeners
document.querySelectorAll('.delete-btn').forEach(btn => {
    btn.addEventListener('click', handleDelete);
});

// ✅ Good - 1 listener (Event Delegation)
document.querySelector('ul').addEventListener('click', (e) => {
    const deleteBtn = e.target.closest('.delete-btn');
    
    if (deleteBtn) {
        deleteBtn.closest('li').remove();
    }
});
```

**Why it's better:**
- Works for dynamically added elements
- Uses less memory
- Faster initialization

### Pattern B: Document Fragments

Build many elements in memory first, then add to DOM once.

```javascript
// ❌ Bad - 1000 DOM updates
for (let i = 0; i < 1000; i++) {
    const li = document.createElement('li');
    li.textContent = `Item ${i}`;
    document.querySelector('ul').append(li);  // Repaints 1000x!
}

// ✅ Good - 1 DOM update
const fragment = document.createDocumentFragment();

for (let i = 0; i < 1000; i++) {
    const li = document.createElement('li');
    li.textContent = `Item ${i}`;
    fragment.append(li);  // In memory only
}

document.querySelector('ul').append(fragment);  // ONE repaint!
```

---

## 8. Common Mistakes to Avoid 🚫

### 1. Null Crashes

```javascript
const el = document.querySelector('.missing');

// ❌ Crashes if element doesn't exist
el.style.color = 'red';  // TypeError: Cannot read properties of null

// ✅ Safe - Check first
if (el) {
    el.style.color = 'red';
}

// ✅ Also safe - Optional chaining
el?.style.color = 'red';
```

### 2. XSS Vulnerabilities

```javascript
const userInput = '<script>stealCookies()</script>';

// ❌ DANGEROUS - Script will run!
element.innerHTML = userInput;

// ✅ SAFE - Renders as plain text
element.textContent = userInput;
```

### 3. Querying Inside Loops

```javascript
// ❌ Bad - Queries DOM every iteration
for (let i = 0; i < 100; i++) {
    document.querySelector('.box').style.opacity = i / 100;
}

// ✅ Good - Query once, reuse
const box = document.querySelector('.box');
for (let i = 0; i < 100; i++) {
    box.style.opacity = i / 100;
}
```

---

## 📊 Quick Reference Table

| Task | Code |
|------|------|
| Select by ID | `document.getElementById('id')` |
| Select by CSS | `document.querySelector('.class')` |
| Select all | `document.querySelectorAll('.class')` |
| Change text | `el.textContent = 'text'` |
| Change HTML | `el.innerHTML = '<b>bold</b>'` |
| Add class | `el.classList.add('class')` |
| Remove class | `el.classList.remove('class')` |
| Toggle class | `el.classList.toggle('class')` |
| Set style | `el.style.color = 'red'` |
| Set attribute | `el.setAttribute('src', 'img.png')` |
| Get data attr | `el.dataset.id` |
| Create element | `document.createElement('div')` |
| Add to DOM | `parent.append(child)` |
| Remove | `el.remove()` |
| Add event | `el.addEventListener('click', fn)` |
| Get parent | `el.parentElement` |
| Get children | `el.children` |
| Get sibling | `el.nextElementSibling` |
| Find ancestor | `el.closest('.class')` |

---

🎉 **You now have a complete DOM reference!** Bookmark this and use it as your go-to guide.
