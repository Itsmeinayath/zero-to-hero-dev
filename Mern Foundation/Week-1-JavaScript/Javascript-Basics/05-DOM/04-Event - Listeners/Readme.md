# 🎯 Event Listeners - Complete Guide

> **Master DOM Events** - Make your webpage respond to user actions!

---

## 📚 Table of Contents

1. [What Are Events?](#1-what-are-events)
2. [addEventListener Syntax](#2-addeventlistener-syntax)
3. [Common Event Types](#3-common-event-types)
4. [The Event Object](#4-the-event-object)
5. [Event Bubbling & Capturing](#5-event-bubbling--capturing)
6. [Event Delegation](#6-event-delegation)
7. [Removing Event Listeners](#7-removing-event-listeners)
8. [Keyboard Events](#8-keyboard-events)
9. [Form Events](#9-form-events)
10. [Best Practices](#10-best-practices)
11. [Dynamic DOM Manipulation](#11-dynamic-dom-manipulation)

---

## 1. What Are Events?

Events are **actions that happen** on your webpage that JavaScript can respond to.

```
User Action          →    Event Fires    →    Your Code Runs
─────────────────────────────────────────────────────────────
Click button         →    "click"        →    Show message
Type in input        →    "input"        →    Validate field
Hover over element   →    "mouseover"    →    Change color
Press keyboard key   →    "keydown"      →    Shortcut action
Submit form          →    "submit"       →    Send data
Page loads           →    "load"         →    Initialize app
```

---

## 2. addEventListener Syntax

### Basic Syntax

```javascript
element.addEventListener("eventType", callbackFunction);
```

### Three Ways to Write It

```javascript
const btn = document.querySelector("#myBtn");

// ✅ Way 1: Named Function (RECOMMENDED)
function handleClick() {
    console.log("Button clicked!");
}
btn.addEventListener("click", handleClick);

// ✅ Way 2: Anonymous Function
btn.addEventListener("click", function() {
    console.log("Button clicked!");
});

// ✅ Way 3: Arrow Function
btn.addEventListener("click", () => {
    console.log("Button clicked!");
});
```

### Visual Output

```
HTML:  <button id="myBtn">Click Me</button>

User clicks button...

Console Output:
┌─────────────────────────┐
│ Button clicked!         │
└─────────────────────────┘
```

---

## 3. Common Event Types

### 🖱️ Mouse Events

| Event         | When It Fires                    |
|---------------|----------------------------------|
| `click`       | Single click                     |
| `dblclick`    | Double click                     |
| `mouseenter`  | Mouse enters element             |
| `mouseleave`  | Mouse leaves element             |
| `mouseover`   | Mouse over (bubbles)             |
| `mouseout`    | Mouse out (bubbles)              |
| `mousedown`   | Mouse button pressed             |
| `mouseup`     | Mouse button released            |
| `mousemove`   | Mouse moves over element         |

```javascript
const box = document.querySelector(".box");

box.addEventListener("mouseenter", () => {
    box.style.backgroundColor = "lightblue";
});

box.addEventListener("mouseleave", () => {
    box.style.backgroundColor = "white";
});
```

**Visual:**
```
BEFORE (mouse outside):          AFTER (mouse inside):
┌──────────────┐                 ┌──────────────┐
│              │    ──────►      │▓▓▓▓▓▓▓▓▓▓▓▓▓▓│ (lightblue)
│    .box      │   mouseenter    │    .box      │
│              │                 │              │
└──────────────┘                 └──────────────┘
```

### ⌨️ Keyboard Events

| Event      | When It Fires                        |
|------------|--------------------------------------|
| `keydown`  | Key is pressed down                  |
| `keyup`    | Key is released                      |
| `keypress` | ⚠️ DEPRECATED - Don't use!           |

### 📝 Form Events

| Event    | When It Fires                          |
|----------|----------------------------------------|
| `submit` | Form is submitted                      |
| `input`  | Value changes (real-time)              |
| `change` | Value changes (after losing focus)     |
| `focus`  | Element gains focus                    |
| `blur`   | Element loses focus                    |

### 🌐 Window Events

| Event    | When It Fires                          |
|----------|----------------------------------------|
| `load`   | Page fully loaded                      |
| `scroll` | User scrolls                           |
| `resize` | Window is resized                      |

---

## 4. The Event Object

When an event fires, JavaScript automatically passes an **event object** with useful info.

```javascript
btn.addEventListener("click", function(event) {
    // "event" (or "e") contains info about what happened
    console.log(event);
});
```

### Key Properties

```javascript
element.addEventListener("click", (e) => {
    
    e.target        // Element that was clicked (actual target)
    e.currentTarget // Element listener is attached to
    e.type          // Event type ("click", "keydown", etc.)
    
    // Mouse position
    e.clientX       // X position in viewport
    e.clientY       // Y position in viewport
    e.pageX         // X position in page
    e.pageY         // Y position in page
    
    // Keyboard info (for keyboard events)
    e.key           // Key pressed ("Enter", "a", "Escape")
    e.code          // Physical key ("KeyA", "Enter")
    
    // Modifier keys
    e.shiftKey      // true if Shift was held
    e.ctrlKey       // true if Ctrl was held
    e.altKey        // true if Alt was held
    
    // Methods
    e.preventDefault()   // Stop default behavior
    e.stopPropagation() // Stop event bubbling
});
```

### Practical Example

```javascript
document.addEventListener("click", (e) => {
    console.log(`Clicked at position: (${e.clientX}, ${e.clientY})`);
    console.log(`You clicked on: ${e.target.tagName}`);
});
```

**Visual Output:**
```
User clicks on a button at coordinates (150, 200)...

Console:
┌───────────────────────────────────────┐
│ Clicked at position: (150, 200)       │
│ You clicked on: BUTTON                │
└───────────────────────────────────────┘
```

---

## 5. Event Bubbling & Capturing

### What is Bubbling?

Events "bubble up" from the target element to its ancestors.

```html
<div id="grandparent">
    <div id="parent">
        <button id="child">Click Me</button>
    </div>
</div>
```

```javascript
document.querySelector("#grandparent").addEventListener("click", () => {
    console.log("Grandparent clicked!");
});

document.querySelector("#parent").addEventListener("click", () => {
    console.log("Parent clicked!");
});

document.querySelector("#child").addEventListener("click", () => {
    console.log("Child clicked!");
});
```

**When you click the button:**
```
Event Flow (Bubbling - Default):
                                    
         ┌─────────────────────┐   3️⃣ Grandparent hears click
         │    #grandparent     │◄──────
         │  ┌───────────────┐  │       │
         │  │    #parent    │◄─┼───────┤ 2️⃣ Parent hears click
         │  │  ┌─────────┐  │  │       │
         │  │  │ #child  │──┼──┼───────┘ 1️⃣ Child clicked (START)
         │  │  │ (button)│  │  │
         │  │  └─────────┘  │  │
         │  └───────────────┘  │
         └─────────────────────┘

Console Output:
┌─────────────────────────┐
│ Child clicked!          │  ← First
│ Parent clicked!         │  ← Second
│ Grandparent clicked!    │  ← Third
└─────────────────────────┘
```

### Stop Bubbling

```javascript
document.querySelector("#child").addEventListener("click", (e) => {
    e.stopPropagation(); // 🛑 Stop! Don't tell parent
    console.log("Only child clicked!");
});
```

### Capturing (Opposite Direction)

```javascript
// Third parameter: true = capture phase
element.addEventListener("click", handler, true);

// Or with options object:
element.addEventListener("click", handler, { capture: true });
```

```
Capturing vs Bubbling:

         CAPTURING (down)          BUBBLING (up)
              │                         ▲
              ▼                         │
         ┌─────────┐              ┌─────────┐
         │ grandpa │  1️⃣          │ grandpa │  3️⃣
         │ ┌─────┐ │              │ ┌─────┐ │
         │ │parent│ │  2️⃣          │ │parent│ │  2️⃣
         │ │┌───┐│ │              │ │┌───┐│ │
         │ ││btn││ │  3️⃣ TARGET    │ ││btn││ │  1️⃣ START
         │ │└───┘│ │              │ │└───┘│ │
         │ └─────┘ │              │ └─────┘ │
         └─────────┘              └─────────┘
```

---

## 6. Event Delegation

Instead of adding listeners to many elements, add **ONE listener to the parent**.

### ❌ Without Delegation (Inefficient)

```javascript
// Adding listener to EACH button - BAD!
const buttons = document.querySelectorAll(".btn");
buttons.forEach(btn => {
    btn.addEventListener("click", () => {
        console.log("Button clicked");
    });
});

// Problem: New buttons won't have listeners!
```

### ✅ With Delegation (Efficient)

```javascript
// ONE listener on parent - GOOD!
document.querySelector("#button-container").addEventListener("click", (e) => {
    if (e.target.classList.contains("btn")) {
        console.log("Button clicked:", e.target.textContent);
    }
});

// New buttons automatically work!
```

### Visual Comparison

```
WITHOUT DELEGATION:                  WITH DELEGATION:
┌─────────────────────┐              ┌─────────────────────┐
│   #container        │              │   #container 👂     │ ← ONE listener
│  ┌─────┐ ┌─────┐   │              │  ┌─────┐ ┌─────┐   │
│  │btn👂│ │btn👂│   │              │  │ btn │ │ btn │   │
│  └─────┘ └─────┘   │              │  └─────┘ └─────┘   │
│  ┌─────┐ ┌─────┐   │              │  ┌─────┐ ┌─────┐   │
│  │btn👂│ │btn👂│   │              │  │ btn │ │ btn │   │
│  └─────┘ └─────┘   │              │  └─────┘ └─────┘   │
└─────────────────────┘              └─────────────────────┘
      4 listeners                         1 listener
      
❌ Doesn't work for new buttons       ✅ Works for new buttons
❌ More memory usage                  ✅ Better performance
```

### Real-World Example: Todo List

```html
<ul id="todo-list">
    <li>Task 1 <button class="delete">❌</button></li>
    <li>Task 2 <button class="delete">❌</button></li>
    <li>Task 3 <button class="delete">❌</button></li>
</ul>
```

```javascript
// One listener handles ALL delete buttons (even future ones!)
document.querySelector("#todo-list").addEventListener("click", (e) => {
    if (e.target.classList.contains("delete")) {
        e.target.closest("li").remove();
    }
});
```

---

## 7. Removing Event Listeners

### Why Remove Listeners?

- Prevent memory leaks
- Stop unwanted behavior
- One-time actions

### Syntax

```javascript
element.removeEventListener("eventType", functionName);
```

### ⚠️ Important: Must Use Named Function

```javascript
// ❌ WRONG - Can't remove anonymous functions
btn.addEventListener("click", function() {
    console.log("Clicked!");
});
btn.removeEventListener("click", function() {  // This won't work!
    console.log("Clicked!");
});

// ✅ CORRECT - Use named function
function handleClick() {
    console.log("Clicked!");
}
btn.addEventListener("click", handleClick);
btn.removeEventListener("click", handleClick);  // ✅ Works!
```

### One-Time Event (Modern Way)

```javascript
// Event fires only ONCE, then auto-removes itself
btn.addEventListener("click", () => {
    console.log("This only runs once!");
}, { once: true });
```

---

## 8. Keyboard Events

### Basic Keyboard Listening

```javascript
document.addEventListener("keydown", (e) => {
    console.log(`Key pressed: ${e.key}`);
    console.log(`Key code: ${e.code}`);
});
```

### Common Key Values

| Key            | e.key         | e.code        |
|----------------|---------------|---------------|
| Enter          | "Enter"       | "Enter"       |
| Space          | " "           | "Space"       |
| Escape         | "Escape"      | "Escape"      |
| Arrow Up       | "ArrowUp"     | "ArrowUp"     |
| Arrow Down     | "ArrowDown"   | "ArrowDown"   |
| Letter A       | "a" or "A"    | "KeyA"        |
| Number 1       | "1"           | "Digit1"      |
| Shift          | "Shift"       | "ShiftLeft"   |

### Keyboard Shortcuts

```javascript
document.addEventListener("keydown", (e) => {
    // Ctrl + S = Save
    if (e.ctrlKey && e.key === "s") {
        e.preventDefault(); // Stop browser's save dialog
        console.log("Custom save action!");
    }
    
    // Escape = Close modal
    if (e.key === "Escape") {
        closeModal();
    }
    
    // Enter = Submit
    if (e.key === "Enter") {
        submitForm();
    }
});
```

### Visual: Modifier Keys

```
┌─────────────────────────────────────────────────────────┐
│                    MODIFIER KEYS                        │
├─────────────────────────────────────────────────────────┤
│  e.ctrlKey   →  Ctrl is pressed?   (true/false)        │
│  e.shiftKey  →  Shift is pressed?  (true/false)        │
│  e.altKey    →  Alt is pressed?    (true/false)        │
│  e.metaKey   →  Cmd/Win is pressed? (true/false)       │
├─────────────────────────────────────────────────────────┤
│  Example: Ctrl + Shift + S                              │
│  e.ctrlKey = true, e.shiftKey = true, e.key = "s"      │
└─────────────────────────────────────────────────────────┘
```

---

## 9. Form Events

### Prevent Form Submission (Common Use)

```html
<form id="myForm">
    <input type="text" id="username" required>
    <button type="submit">Submit</button>
</form>
```

```javascript
document.querySelector("#myForm").addEventListener("submit", (e) => {
    e.preventDefault(); // 🛑 Stop page refresh!
    
    const username = document.querySelector("#username").value;
    console.log("Form submitted with:", username);
    
    // Now send data with fetch() instead
});
```

### Input vs Change Events

```javascript
const input = document.querySelector("#search");

// "input" - fires on EVERY keystroke
input.addEventListener("input", (e) => {
    console.log("Typing:", e.target.value);
});

// "change" - fires when you LEAVE the field
input.addEventListener("change", (e) => {
    console.log("Final value:", e.target.value);
});
```

**Visual Comparison:**
```
User types "hello" in input field:

┌──────────────────────────────────────────────────────────┐
│ INPUT EVENT (fires on every keystroke):                  │
│ ────────────────────────────────────────                 │
│ Type "h" → Console: "Typing: h"                          │
│ Type "e" → Console: "Typing: he"                         │
│ Type "l" → Console: "Typing: hel"                        │
│ Type "l" → Console: "Typing: hell"                       │
│ Type "o" → Console: "Typing: hello"                      │
│ Click outside → (nothing)                                │
├──────────────────────────────────────────────────────────┤
│ CHANGE EVENT (fires when leaving field):                 │
│ ────────────────────────────────────────                 │
│ Type "h" → (nothing)                                     │
│ Type "e" → (nothing)                                     │
│ Type "l" → (nothing)                                     │
│ Type "l" → (nothing)                                     │
│ Type "o" → (nothing)                                     │
│ Click outside → Console: "Final value: hello"            │
└──────────────────────────────────────────────────────────┘
```

### Focus & Blur

```javascript
const input = document.querySelector("#email");

input.addEventListener("focus", () => {
    input.style.borderColor = "blue";
    console.log("Input focused");
});

input.addEventListener("blur", () => {
    input.style.borderColor = "gray";
    console.log("Input lost focus");
});
```

---

## 10. Best Practices

### ✅ Do's

```javascript
// ✅ Use named functions for reusability
function handleClick(e) {
    console.log("Clicked!", e.target);
}
btn.addEventListener("click", handleClick);

// ✅ Use event delegation for dynamic content
container.addEventListener("click", (e) => {
    if (e.target.matches(".dynamic-btn")) {
        // handle click
    }
});

// ✅ Remove listeners when not needed
btn.removeEventListener("click", handleClick);

// ✅ Use { once: true } for one-time events
btn.addEventListener("click", handler, { once: true });

// ✅ Always prevent default for forms
form.addEventListener("submit", (e) => {
    e.preventDefault();
});
```

### ❌ Don'ts

```javascript
// ❌ Don't use inline event handlers in HTML
<button onclick="handleClick()">  // OLD WAY - Avoid!

// ❌ Don't add listeners in loops when delegation works
items.forEach(item => {
    item.addEventListener("click", handler);  // Inefficient!
});

// ❌ Don't forget to remove listeners (memory leaks!)
// ❌ Don't use anonymous functions if you need to remove later
```

---

## 11. Dynamic DOM Manipulation

### Creating Elements

```javascript
// Step 1: Create the element
const newDiv = document.createElement("div");

// Step 2: Add content & attributes
newDiv.textContent = "I'm a new element!";
newDiv.className = "card";
newDiv.id = "card-1";
newDiv.setAttribute("data-id", "123");

// Step 3: Add to the DOM
document.body.appendChild(newDiv);
```

**Visual:**
```
BEFORE:                          AFTER appendChild():
┌──────────────────┐             ┌──────────────────┐
│      <body>      │             │      <body>      │
│                  │   ──────►   │  ┌────────────┐  │
│                  │             │  │  new div   │  │
│                  │             │  └────────────┘  │
└──────────────────┘             └──────────────────┘
```

### Insert Positions

```javascript
const container = document.querySelector("#container");
const newElement = document.createElement("div");

// Different ways to insert
container.appendChild(newElement);        // Add as LAST child
container.prepend(newElement);            // Add as FIRST child
container.before(newElement);             // Add BEFORE container
container.after(newElement);              // Add AFTER container

// Insert at specific position
container.insertBefore(newElement, referenceElement);
```

**Visual Map:**
```
                    .before(new)
                         │
                         ▼
              ┌──────────────────────┐
              │     #container       │
              │ ┌──────────────────┐ │ ◄── .prepend(new) [FIRST]
              │ │  existing child  │ │
              │ └──────────────────┘ │
              │ ┌──────────────────┐ │ ◄── .appendChild(new) [LAST]
              │ └──────────────────┘ │
              └──────────────────────┘
                         │
                         ▼
                    .after(new)
```

### insertAdjacentHTML (Quick Way)

```javascript
const container = document.querySelector("#container");

// Insert HTML string at different positions
container.insertAdjacentHTML("beforebegin", "<p>Before</p>");
container.insertAdjacentHTML("afterbegin", "<p>First child</p>");
container.insertAdjacentHTML("beforeend", "<p>Last child</p>");
container.insertAdjacentHTML("afterend", "<p>After</p>");
```

```
Position keywords:
                "beforebegin"
                      │
         ┌────────────▼────────────┐
         │      "afterbegin"       │
         │            │            │
         │     [existing content]  │
         │            │            │
         │      "beforeend"        │
         └────────────┬────────────┘
                      │
                "afterend"
```

### Real Example: Add Todo Item

```html
<ul id="todo-list">
    <li>Existing task</li>
</ul>
<input id="todo-input" type="text">
<button id="add-btn">Add</button>
```

```javascript
const list = document.querySelector("#todo-list");
const input = document.querySelector("#todo-input");
const addBtn = document.querySelector("#add-btn");

addBtn.addEventListener("click", () => {
    // Get input value
    const text = input.value.trim();
    if (!text) return;
    
    // Create new list item
    const li = document.createElement("li");
    li.textContent = text;
    
    // Add delete button
    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "❌";
    deleteBtn.className = "delete-btn";
    li.appendChild(deleteBtn);
    
    // Add to list
    list.appendChild(li);
    
    // Clear input
    input.value = "";
});

// Event delegation for delete (works for NEW items too!)
list.addEventListener("click", (e) => {
    if (e.target.classList.contains("delete-btn")) {
        e.target.parentElement.remove();
    }
});
```

**Visual Flow:**
```
User types "Buy milk" and clicks Add:

BEFORE:                              AFTER:
┌────────────────────────┐           ┌────────────────────────┐
│  • Existing task       │           │  • Existing task       │
│                        │  ──────►  │  • Buy milk  ❌        │ ← NEW!
└────────────────────────┘           └────────────────────────┘
```

### Removing Elements

```javascript
// Modern way (recommended)
element.remove();

// Old way (still works)
element.parentElement.removeChild(element);

// Remove all children
container.innerHTML = "";  // Quick but heavy
// OR
while (container.firstChild) {
    container.firstChild.remove();
}
```

### Cloning Elements

```javascript
const original = document.querySelector(".card");

// Shallow clone (element only, no children)
const shallowClone = original.cloneNode(false);

// Deep clone (element + all children)
const deepClone = original.cloneNode(true);

document.body.appendChild(deepClone);
```

### Moving Elements

```javascript
// Moving is automatic! Just append to new location
const element = document.querySelector("#movable");
const newParent = document.querySelector("#new-container");

newParent.appendChild(element);  // Moves, doesn't copy!
```

### DocumentFragment (Performance)

When adding MANY elements, use a fragment to avoid multiple repaints:

```javascript
// ❌ Slow - 100 DOM updates
for (let i = 0; i < 100; i++) {
    const li = document.createElement("li");
    li.textContent = `Item ${i}`;
    list.appendChild(li);  // DOM updates 100 times!
}

// ✅ Fast - 1 DOM update
const fragment = document.createDocumentFragment();

for (let i = 0; i < 100; i++) {
    const li = document.createElement("li");
    li.textContent = `Item ${i}`;
    fragment.appendChild(li);  // No DOM update yet
}

list.appendChild(fragment);  // ONE DOM update!
```

**Visual:**
```
WITHOUT Fragment:              WITH Fragment:
┌─────────────────┐            ┌─────────────────┐
│  Add item 1     │ → Repaint  │  Build in       │
│  Add item 2     │ → Repaint  │  memory...      │
│  Add item 3     │ → Repaint  │  ...            │
│  ...            │            │  ...            │
│  Add item 100   │ → Repaint  │  Add ALL        │ → 1 Repaint
└─────────────────┘            └─────────────────┘
    100 repaints                   1 repaint
        ❌                            ✅
```

### Modify Existing Elements

```javascript
const element = document.querySelector("#myElement");

// Text
element.textContent = "New text";

// HTML
element.innerHTML = "<strong>Bold text</strong>";

// Attributes
element.setAttribute("data-id", "123");
element.getAttribute("data-id");        // "123"
element.removeAttribute("data-id");
element.hasAttribute("data-id");        // false

// Classes
element.classList.add("active", "visible");
element.classList.remove("hidden");
element.classList.toggle("dark-mode");
element.classList.replace("old", "new");

// Styles
element.style.backgroundColor = "blue";
element.style.display = "none";
element.style.cssText = "color: red; font-size: 20px;";

// Data attributes
element.dataset.userId = "42";          // sets data-user-id="42"
console.log(element.dataset.userId);    // "42"
```

---

## 🎯 Quick Reference

```
┌─────────────────────────────────────────────────────────────────┐
│                    EVENT LISTENER CHEATSHEET                    │
├─────────────────────────────────────────────────────────────────┤
│ ADD LISTENER                                                    │
│ element.addEventListener("click", myFunction);                  │
│                                                                 │
│ REMOVE LISTENER                                                 │
│ element.removeEventListener("click", myFunction);               │
│                                                                 │
│ ONE-TIME LISTENER                                               │
│ element.addEventListener("click", fn, { once: true });          │
│                                                                 │
│ STOP DEFAULT BEHAVIOR                                           │
│ e.preventDefault();                                             │
│                                                                 │
│ STOP BUBBLING                                                   │
│ e.stopPropagation();                                            │
│                                                                 │
│ GET CLICKED ELEMENT                                             │
│ e.target                                                        │
│                                                                 │
│ CHECK WHICH KEY                                                 │
│ e.key === "Enter"                                               │
│                                                                 │
│ CHECK MODIFIER                                                  │
│ if (e.ctrlKey && e.key === "s")                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🏋️ Practice Exercises

### Exercise 1: Click Counter
```javascript
// Create a button that shows how many times it's been clicked
let count = 0;
const btn = document.querySelector("#counter-btn");
const display = document.querySelector("#count");

btn.addEventListener("click", () => {
    count++;
    display.textContent = count;
});
```

### Exercise 2: Keyboard Navigation
```javascript
// Move a box with arrow keys
const box = document.querySelector("#movable-box");
let x = 0, y = 0;

document.addEventListener("keydown", (e) => {
    switch(e.key) {
        case "ArrowUp":    y -= 10; break;
        case "ArrowDown":  y += 10; break;
        case "ArrowLeft":  x -= 10; break;
        case "ArrowRight": x += 10; break;
    }
    box.style.transform = `translate(${x}px, ${y}px)`;
});
```

### Exercise 3: Form Validation
```javascript
// Validate email on blur
const emailInput = document.querySelector("#email");

emailInput.addEventListener("blur", (e) => {
    const email = e.target.value;
    const isValid = email.includes("@");
    
    e.target.style.borderColor = isValid ? "green" : "red";
});
```

---

## 📚 Event Types Summary

| Category   | Events                                          |
|------------|------------------------------------------------|
| Mouse      | click, dblclick, mouseenter, mouseleave        |
| Keyboard   | keydown, keyup                                 |
| Form       | submit, input, change, focus, blur             |
| Window     | load, scroll, resize                           |
| Touch      | touchstart, touchend, touchmove                |
| Drag       | dragstart, dragend, drop, dragover             |

---

> **Next Steps:** Practice by building a simple interactive component like a dropdown menu, modal, or image gallery using event listeners!
