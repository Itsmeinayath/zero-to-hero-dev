# Query Selector - Complete Guide

## 📚 Table of Contents

- [What is Query Selector?](#what-is-query-selector)
- [Syntax](#syntax)
- [Selector Types](#selector-types)
- [querySelector vs querySelectorAll](#queryselector-vs-queryselectorall)
- [Practical Examples](#practical-examples)
- [Common Use Cases](#common-use-cases)
- [Parent, Child & Sibling Traversal](#parent-child--sibling-traversal)
- [Best Practices](#best-practices)
- [Practice Exercises](#practice-exercises)

---

## What is Query Selector?

**`querySelector()`** is a powerful JavaScript method that allows you to select HTML elements using **CSS selectors**. It returns the **first element** that matches the specified selector.

### 💡 Analogy

Think of `querySelector` as a **search function** for your webpage:
- You give it a description (CSS selector)
- It finds and returns the first matching element
- Just like searching for "red shirt" in your closet - you get the first one you find!

### 🎯 Key Benefits

✅ **Use CSS selectors** - Same syntax you already know from CSS  
✅ **Flexible** - Select by tag, class, ID, or complex selectors  
✅ **Modern** - Preferred over older methods like `getElementById`  
✅ **Powerful** - Can use any valid CSS selector  

---

## Syntax

```javascript
// Basic syntax
document.querySelector("selector");

// Store in a variable
const element = document.querySelector("selector");
```

### Return Value

- **Found:** Returns the first matching element
- **Not found:** Returns `null`

```javascript
const element = document.querySelector(".myClass");

if (element) {
    console.log("Element found!");
} else {
    console.log("Element not found!");
}
```

---

## Selector Types

### 1. Tag Selector

Select elements by their HTML tag name.

```html
<p>First paragraph</p>
<p>Second paragraph</p>
<div>A div element</div>
```

```javascript
// Selects the FIRST <p> element
const paragraph = document.querySelector("p");
console.log(paragraph.textContent); // Output: First paragraph

// Selects the <div> element
const div = document.querySelector("div");
```

### 2. ID Selector (#)

Select an element by its unique ID. Use `#` before the ID name.

```html
<h1 id="title">Welcome!</h1>
<p id="description">This is a description.</p>
```

```javascript
// Select by ID using #
const title = document.querySelector("#title");
title.textContent = "Hello World!";

const description = document.querySelector("#description");
description.style.color = "blue";
```

### 3. Class Selector (.)

Select elements by their class name. Use `.` before the class name.

```html
<p class="highlight">Important text</p>
<p class="highlight">Another important text</p>
<p class="normal">Regular text</p>
```

```javascript
// Selects only the FIRST element with class "highlight"
const highlighted = document.querySelector(".highlight");
highlighted.style.backgroundColor = "yellow";

// The second .highlight element is NOT selected!
```

### 4. Attribute Selector

Select elements by their attributes.

```html
<input type="text" name="username">
<input type="email" name="email">
<button disabled>Submit</button>
```

```javascript
// Select by attribute
const emailInput = document.querySelector('input[type="email"]');
const usernameInput = document.querySelector('input[name="username"]');
const disabledBtn = document.querySelector("button[disabled]");
```

### 5. Descendant Selector

Select nested elements using space between selectors.

```html
<div class="container">
    <p>Paragraph inside div</p>
</div>
<p>Paragraph outside div</p>
```

```javascript
// Select <p> that is INSIDE .container
const nestedParagraph = document.querySelector(".container p");
nestedParagraph.style.fontWeight = "bold";
```

### 6. Multiple Selectors (Complex)

Combine selectors for precise selection.

```html
<nav class="navbar">
    <ul>
        <li class="active">Home</li>
        <li>About</li>
    </ul>
</nav>
```

```javascript
// Select .active that is inside nav ul
const activeItem = document.querySelector("nav ul li.active");
console.log(activeItem.textContent); // Output: Home
```

---

## querySelector vs querySelectorAll

| Feature | `querySelector()` | `querySelectorAll()` |
|---------|------------------|---------------------|
| **Returns** | First matching element | All matching elements |
| **Return type** | Single element or `null` | NodeList (array-like) |
| **Use when** | Need one specific element | Need multiple elements |

### querySelector - Single Element

```javascript
// Returns ONLY the first match
const firstItem = document.querySelector(".item");
```

### querySelectorAll - Multiple Elements

```javascript
// Returns ALL matches as a NodeList
const allItems = document.querySelectorAll(".item");

// Loop through all items
allItems.forEach(item => {
    item.style.color = "red";
});

// Access by index
console.log(allItems[0]); // First item
console.log(allItems[1]); // Second item
console.log(allItems.length); // Total count
```

### Example Comparison

```html
<ul>
    <li class="fruit">Apple</li>
    <li class="fruit">Banana</li>
    <li class="fruit">Orange</li>
</ul>
```

```javascript
// querySelector - Gets only Apple
const oneFruit = document.querySelector(".fruit");
console.log(oneFruit.textContent); // Output: Apple

// querySelectorAll - Gets all three
const allFruits = document.querySelectorAll(".fruit");
console.log(allFruits.length); // Output: 3

allFruits.forEach(fruit => {
    console.log(fruit.textContent);
});
// Output: Apple, Banana, Orange
```

---

## Practical Examples

### Example 1: Changing Text Content

```html
<h1 id="greeting">Hello!</h1>
```

```javascript
const greeting = document.querySelector("#greeting");
greeting.textContent = "Welcome to my website!";
```

### Example 2: Changing Styles

```html
<div class="box">Styled Box</div>
```

```javascript
const box = document.querySelector(".box");
box.style.backgroundColor = "lightblue";
box.style.padding = "20px";
box.style.borderRadius = "10px";
box.style.textAlign = "center";
```

### Example 3: Changing HTML Content

```html
<div id="content">Original content</div>
```

```javascript
const content = document.querySelector("#content");
content.innerHTML = "<h2>New Title</h2><p>New paragraph</p>";
```

### Example 4: Form Input Values

```html
<input type="text" id="username" value="John">
<button id="greetBtn">Greet</button>
```

```javascript
const input = document.querySelector("#username");
const button = document.querySelector("#greetBtn");

button.addEventListener("click", () => {
    const name = input.value;
    alert(`Hello, ${name}!`);
});
```

### Example 5: Toggle Classes

```html
<div class="card">Click to toggle</div>
```

```javascript
const card = document.querySelector(".card");

card.addEventListener("click", () => {
    card.classList.toggle("active");
});
```

### Example 6: Nested Selection

```html
<nav class="main-nav">
    <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About</a></li>
    </ul>
</nav>
```

```javascript
// Select first link inside nav
const firstLink = document.querySelector(".main-nav a");
firstLink.style.color = "red";

// Select all links inside nav
const allLinks = document.querySelectorAll(".main-nav a");
allLinks.forEach(link => {
    link.style.textDecoration = "none";
});
```

---

## Common Use Cases

### 1. Selecting by ID (Most Common)

```javascript
const header = document.querySelector("#header");
const footer = document.querySelector("#footer");
const mainContent = document.querySelector("#main");
```

### 2. Selecting Form Elements

```javascript
const form = document.querySelector("form");
const submitBtn = document.querySelector('button[type="submit"]');
const emailField = document.querySelector('input[type="email"]');
```

### 3. Selecting Navigation Items

```javascript
const navbar = document.querySelector(".navbar");
const navLinks = document.querySelectorAll(".navbar a");
const activeLink = document.querySelector(".navbar a.active");
```

### 4. Selecting Data Attributes

```html
<div data-user-id="123">User Card</div>
```

```javascript
const userCard = document.querySelector('[data-user-id="123"]');
console.log(userCard.dataset.userId); // Output: 123
```

### 5. First/Last Child Selection

```javascript
const firstItem = document.querySelector("ul li:first-child");
const lastItem = document.querySelector("ul li:last-child");
const thirdItem = document.querySelector("ul li:nth-child(3)");
```

---

## Parent, Child & Sibling Traversal

Once you select an element, you can navigate to its relatives (parent, children, siblings).

### 🌳 DOM Tree Visualization

```
        <div class="container">     ← PARENT
            │
    ┌───────┼───────┐
    │       │       │
  <p>     <span>   <a>              ← CHILDREN (siblings to each other)
```

### Getting Child Elements

```html
<ul id="menu">
    <li>Home</li>
    <li>About</li>
    <li>Contact</li>
</ul>
```

```javascript
const menu = document.querySelector("#menu");

// Get ALL children (returns HTMLCollection)
const allChildren = menu.children;
console.log(allChildren); 
// Output: HTMLCollection(3) [li, li, li]

console.log(allChildren.length); 
// Output: 3

// Get FIRST child element
const firstChild = menu.firstElementChild;
console.log(firstChild.textContent); 
// Output: Home

// Get LAST child element
const lastChild = menu.lastElementChild;
console.log(lastChild.textContent); 
// Output: Contact

// Access child by index
console.log(menu.children[1].textContent); 
// Output: About
```

**Visual: What we're selecting:**
```
<ul id="menu">          ← menu (selected element)
    │
    ├── <li>Home</li>      ← menu.firstElementChild OR menu.children[0]
    │
    ├── <li>About</li>     ← menu.children[1]
    │
    └── <li>Contact</li>   ← menu.lastElementChild OR menu.children[2]
```

### Getting Parent Element

```html
<body>
    <div class="container">
        <p id="paragraph">Hello World</p>
    </div>
</body>
```

```javascript
const paragraph = document.querySelector("#paragraph");

// Get direct parent
const parent = paragraph.parentElement;
console.log(parent.className); 
// Output: container

// Get parent of parent (grandparent)
const grandparent = paragraph.parentElement.parentElement;
console.log(grandparent.tagName); 
// Output: BODY
```

**Visual: Going UP the tree:**
```
<body>                          ← paragraph.parentElement.parentElement (grandparent)
    │
    └── <div class="container"> ← paragraph.parentElement (parent)
            │
            └── <p id="paragraph">  ← paragraph (we start here)
                    │
                    "Hello World"
```

### Using closest() - Find Ancestor

```html
<div class="card">
    <div class="card-body">
        <button class="delete-btn">Delete</button>
    </div>
</div>
```

```javascript
const button = document.querySelector(".delete-btn");

// Find the nearest ancestor with class "card"
const card = button.closest(".card");
console.log(card.className); 
// Output: card

// Common use: Delete the entire card when button clicked
button.addEventListener("click", () => {
    button.closest(".card").remove();
});
```

**Visual: closest() searches UP:**
```
<div class="card">          ← button.closest(".card") ✅ FOUND!
    │
    └── <div class="card-body">  ← button.closest(".card-body") ✅ FOUND!
            │
            └── <button>  ← We start here, search goes UP ⬆️
```

### Getting Sibling Elements

```html
<ul>
    <li id="first">Apple</li>
    <li id="second">Banana</li>
    <li id="third">Orange</li>
</ul>
```

```javascript
const second = document.querySelector("#second");

// Get NEXT sibling
const next = second.nextElementSibling;
console.log(next.textContent); 
// Output: Orange

// Get PREVIOUS sibling
const prev = second.previousElementSibling;
console.log(prev.textContent); 
// Output: Apple
```

**Visual: Sibling Navigation:**
```
<ul>
    │
    ├── <li>Apple</li>   ← second.previousElementSibling
    │         ⬇️
    ├── <li>Banana</li>  ← second (we start here)
    │         ⬇️
    └── <li>Orange</li>  ← second.nextElementSibling
```

### Practical Example: Accordion

```html
<!-- BEFORE click -->
<div class="accordion">
    <button class="accordion-btn">Section 1</button>
    <div class="accordion-content">Hidden Content</div>
</div>
```

```javascript
const button = document.querySelector(".accordion-btn");

button.addEventListener("click", () => {
    // Get the next sibling (the content div)
    const content = button.nextElementSibling;
    content.classList.toggle("open");
});
```

**Visual: Before & After Click:**
```
BEFORE CLICK:                      AFTER CLICK:
┌─────────────────────┐           ┌─────────────────────┐
│ [Section 1]         │    →      │ [Section 1]         │
└─────────────────────┘           ├─────────────────────┤
  (content hidden)                │ Hidden Content      │
                                  │ (now visible!)      │
                                  └─────────────────────┘
```

### Practical Example: Delete Item from List

```html
<!-- BEFORE delete -->
<ul id="todoList">
    <li>Task 1 <button class="delete">X</button></li>
    <li>Task 2 <button class="delete">X</button></li>
    <li>Task 3 <button class="delete">X</button></li>
</ul>
```

```javascript
const deleteButtons = document.querySelectorAll(".delete");

deleteButtons.forEach(btn => {
    btn.addEventListener("click", () => {
        // Get parent (the <li>) and remove it
        const listItem = btn.parentElement;
        listItem.remove();
    });
});
```

**Visual: Before & After Clicking X on Task 2:**
```
BEFORE:                           AFTER:
┌─────────────────────┐          ┌─────────────────────┐
│ • Task 1  [X]       │          │ • Task 1  [X]       │
│ • Task 2  [X] ← Click          │ • Task 3  [X]       │
│ • Task 3  [X]       │          └─────────────────────┘
└─────────────────────┘           Task 2 is GONE!
```

**How it works:**
```
<li>                    ← btn.parentElement (this gets removed)
    │
    ├── "Task 2 "       
    │
    └── <button class="delete">X</button>  ← btn (clicked)
```

### Practical Example: Highlight Parent on Hover

```html
<div class="card">
    <h3>Product Title</h3>
    <p>Product description here</p>
    <button class="buy-btn">Buy Now</button>
</div>
```

```javascript
const buyBtn = document.querySelector(".buy-btn");

buyBtn.addEventListener("mouseenter", () => {
    // Highlight the entire card when hovering button
    buyBtn.parentElement.style.backgroundColor = "#ffffcc";
});

buyBtn.addEventListener("mouseleave", () => {
    buyBtn.parentElement.style.backgroundColor = "";
});
```

**Visual: Hover Effect:**
```
NORMAL:                           ON HOVER (button):
┌─────────────────────┐          ┌─────────────────────┐
│ Product Title       │          │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
│                     │    →     │▓ Product Title     ▓│
│ Product description │          │▓                   ▓│
│                     │          │▓ Product description│
│ [Buy Now]           │          │▓                   ▓│
└─────────────────────┘          │▓ [Buy Now] ← hover ▓│
                                 └─────────────────────┘
                                  (card highlighted!)
```

### Quick Reference: Traversal Properties

| Property | Description | Returns |
|----------|-------------|---------|
| `parentElement` | Direct parent | Single element |
| `children` | All child elements | HTMLCollection |
| `firstElementChild` | First child | Single element |
| `lastElementChild` | Last child | Single element |
| `nextElementSibling` | Next sibling | Single element |
| `previousElementSibling` | Previous sibling | Single element |
| `closest("selector")` | Nearest ancestor matching selector | Single element |

### Loop Through All Children

```javascript
const container = document.querySelector(".container");

// Method 1: for...of loop
for (const child of container.children) {
    console.log(child.tagName);
}

// Method 2: Convert to array and use forEach
Array.from(container.children).forEach(child => {
    child.style.color = "blue";
});
```

**Visual: Looping through children:**
```html
<div class="container">
    <p>Paragraph 1</p>    ← Loop iteration 1: color = blue
    <p>Paragraph 2</p>    ← Loop iteration 2: color = blue
    <p>Paragraph 3</p>    ← Loop iteration 3: color = blue
</div>
```

---

## Best Practices

### ✅ Do's

**1. Use IDs for Unique Elements**

```javascript
// ✅ Good - ID is unique
const header = document.querySelector("#header");
```

**2. Store Elements in Variables**

```javascript
// ✅ Good - Reuse the variable
const button = document.querySelector("#submitBtn");
button.style.color = "white";
button.style.backgroundColor = "blue";
button.addEventListener("click", handleSubmit);
```

**3. Check if Element Exists**

```javascript
// ✅ Good - Prevent errors
const element = document.querySelector(".maybe-exists");

if (element) {
    element.style.display = "block";
}
```

**4. Use Specific Selectors**

```javascript
// ✅ Good - Specific and clear
const submitBtn = document.querySelector("form#login button.submit");
```

### ❌ Don'ts

**1. Don't Query Repeatedly**

```javascript
// ❌ Bad - Queries DOM 3 times
document.querySelector("#box").style.color = "red";
document.querySelector("#box").style.fontSize = "20px";
document.querySelector("#box").textContent = "Hello";

// ✅ Good - Query once, use variable
const box = document.querySelector("#box");
box.style.color = "red";
box.style.fontSize = "20px";
box.textContent = "Hello";
```

**2. Don't Use Too Generic Selectors**

```javascript
// ❌ Bad - Too generic, might select wrong element
const div = document.querySelector("div");

// ✅ Good - Specific
const contentDiv = document.querySelector(".content-wrapper");
```

---

## Practice Exercises

### Exercise 1: Basic Selection

```html
<div id="container">
    <h1 class="title">Hello World</h1>
    <p class="description">This is a paragraph.</p>
    <button id="btn">Click Me</button>
</div>
```

```javascript
// 1. Select the h1 element and change its text to "Welcome!"
// Your code here

// 2. Select the button and change its background color
// Your code here

// 3. Select the paragraph and make the text bold
// Your code here
```

### Exercise 2: Nested Selection

```html
<nav class="navbar">
    <ul class="nav-list">
        <li class="nav-item">Home</li>
        <li class="nav-item">About</li>
        <li class="nav-item">Contact</li>
    </ul>
</nav>
```

```javascript
// 1. Select the first nav-item and change its color
// Your code here

// 2. Select all nav-items and add padding to each
// Your code here
```

### Exercise 3: Form Handling

```html
<form id="signup">
    <input type="text" id="name" placeholder="Your name">
    <input type="email" id="email" placeholder="Your email">
    <button type="submit">Sign Up</button>
</form>
```

```javascript
// 1. Select the form element
// Your code here

// 2. Select both input fields
// Your code here

// 3. Add a submit event listener that logs the input values
// Your code here
```

### Exercise 4: Dynamic Styling

```html
<div class="cards">
    <div class="card">Card 1</div>
    <div class="card">Card 2</div>
    <div class="card">Card 3</div>
</div>
```

```javascript
// 1. Select all cards and give each a different background color
// Your code here

// 2. Add a click event to each card that toggles a "selected" class
// Your code here
```

---

## 🎯 Quick Reference

```javascript
// BY TAG
document.querySelector("div");
document.querySelector("p");
document.querySelector("button");

// BY ID (use #)
document.querySelector("#myId");
document.querySelector("#header");

// BY CLASS (use .)
document.querySelector(".myClass");
document.querySelector(".container");

// BY ATTRIBUTE
document.querySelector('[name="email"]');
document.querySelector('[type="submit"]');
document.querySelector('[data-id="123"]');

// NESTED / DESCENDANT
document.querySelector(".parent .child");
document.querySelector("nav ul li");
document.querySelector("#form input");

// PSEUDO-SELECTORS
document.querySelector("li:first-child");
document.querySelector("li:last-child");
document.querySelector("li:nth-child(2)");

// MULTIPLE ELEMENTS (querySelectorAll)
document.querySelectorAll(".item");
document.querySelectorAll("p");
```

---

## 📚 Summary

### Key Takeaways

✅ `querySelector` selects the **first** matching element  
✅ `querySelectorAll` selects **all** matching elements  
✅ Use `#` for IDs and `.` for classes  
✅ Returns `null` if no element is found  
✅ Can use any valid CSS selector  
✅ Store elements in variables for reuse  
✅ Always check if element exists before using  

### Comparison with Old Methods

| Old Method | querySelector Equivalent |
|------------|-------------------------|
| `getElementById("id")` | `querySelector("#id")` |
| `getElementsByClassName("class")[0]` | `querySelector(".class")` |
| `getElementsByTagName("tag")[0]` | `querySelector("tag")` |

---

🎉 **Congratulations!** You now understand Query Selector! Practice with the exercises to master DOM selection.

**Pro Tip:** `querySelector` is the Swiss Army knife of DOM selection - learn it well and you can select anything! 🚀
