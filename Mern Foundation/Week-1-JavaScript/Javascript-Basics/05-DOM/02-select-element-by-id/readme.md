# getElementById - Complete Guide

## 📚 Table of Contents

- [What is getElementById?](#what-is-getelementbyid)
- [Changing Text Content](#changing-text-content)
- [Working with Classes](#working-with-classes)
- [Inline Styles](#inline-styles)
- [Parent & Child Traversal](#parent--child-traversal)
- [Removing Elements](#removing-elements)
- [Quick Reference](#quick-reference)

---

## What is getElementById?

**`getElementById()`** selects a single HTML element by its unique `id` attribute.

```javascript
const element = document.getElementById("myId");
```

> ⚠️ **Note:** IDs must be unique! Only ONE element should have a specific ID.

---

## Changing Text Content

### textContent vs innerText

```html
<span id="username">John Doe</span>
```

```javascript
const username = document.getElementById("username");

// textContent - Sets/gets ALL text (including hidden)
username.textContent = "Inyath";

// innerText - Sets/gets VISIBLE text only
username.innerText = "Alice";
```

**Visual Output:**
```
BEFORE:  John Doe
AFTER:   Alice
```

### innerHTML - Add HTML Tags

```javascript
username.innerHTML = "<strong>Alice</strong>";
```

**Visual Output:**
```
BEFORE:  Alice
AFTER:   Alice  (but bold!)
```

| Property | Use For | Parses HTML? |
|----------|---------|--------------|
| `textContent` | Plain text (faster) | ❌ No |
| `innerText` | Visible text only | ❌ No |
| `innerHTML` | Text with HTML tags | ✅ Yes |

---

## Working with Classes

### Add Classes

```html
<style>
    .red-color { color: red; }
    .underline { text-decoration: underline; }
</style>

<span id="username">Alice</span>
```

```javascript
const username = document.getElementById("username");

// Add single class
username.classList.add("red-color");

// Add multiple classes at once
username.classList.add("red-color", "underline");
```

**Visual Output:**
```
BEFORE:  Alice        (normal black text)
AFTER:   Alice        (red + underlined)
         ‾‾‾‾‾
```

### Remove Classes

```javascript
// Remove single class
username.classList.remove("red-color");

// Remove multiple classes
username.classList.remove("red-color", "underline");
```

### Toggle Classes

```javascript
// If class exists → remove it
// If class doesn't exist → add it
username.classList.toggle("red-color");
```

### Check if Class Exists

```javascript
if (username.classList.contains("red-color")) {
    console.log("Has red-color class!");
}
```

---

## Inline Styles

Add CSS directly to elements using the `style` property.

```javascript
const username = document.getElementById("username");

// Single style
username.style.color = "blue";

// Multiple styles
username.style.color = "blue";
username.style.fontSize = "20px";
username.style.textDecoration = "line-through";
username.style.backgroundColor = "yellow";
```

**Visual Output:**
```
BEFORE:  Alice
AFTER:   Alice   (blue, larger, strikethrough, yellow bg)
         ━━━━━
```

### CSS Property → JavaScript Property

| CSS Property | JavaScript Property |
|--------------|-------------------|
| `color` | `style.color` |
| `font-size` | `style.fontSize` |
| `background-color` | `style.backgroundColor` |
| `text-decoration` | `style.textDecoration` |
| `margin-top` | `style.marginTop` |

> 💡 **Rule:** Remove `-` and capitalize next letter (camelCase)

---

## Parent & Child Traversal

### Get Parent Element

```html
<h4>                              ← parentElement
    <span id="username">Alice</span>   ← we select this
</h4>
```

```javascript
const username = document.getElementById("username");
const parent = username.parentElement;

console.log(parent);  // <h4>...</h4>

// Style the parent
parent.style.backgroundColor = "lightgrey";
```

**Visual Output:**
```
BEFORE:                    AFTER:
┌──────────────────┐      ┌──────────────────┐
│ Hey There, Alice │  →   │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
│ Here is a code   │      │▒Hey There, Alice▒│
└──────────────────┘      │▒Here is a code  ▒│
                          └──────────────────┘
                           (grey background)
```

### Get Child Elements

```javascript
const parent = username.parentElement;

// All children
const children = parent.children;
console.log(children);  // HTMLCollection [span, p]

// First child
const first = parent.firstElementChild;
console.log(first);  // <span id="username">

// Last child
const last = parent.lastElementChild;
console.log(last);  // <p class="paragraph">
```

**Visual: Parent-Child Structure:**
```
<h4>  ← parent
  │
  ├── <span id="username">  ← firstElementChild, children[0]
  │
  └── <p class="paragraph"> ← lastElementChild, children[1]
```

### Loop Through Children

```javascript
const children = parent.children;

for (let i = 0; i < children.length; i++) {
    children[i].style.fontWeight = "bold";
}
```

**Visual Output:**
```
BEFORE:                    AFTER:
Hey There, Alice      →    Hey There, Alice
Here is a code             Here is a code
(normal weight)            (ALL BOLD!)
```

---

## Removing Elements

### remove() - Delete Element

```javascript
const username = document.getElementById("username");
username.remove();
```

**Visual Output:**
```
BEFORE:                         AFTER:
Hey There, My name is Alice  →  Hey There, My name is
Here is a code                  Here is a code

(Alice is GONE!)
```

### removeChild() - Remove via Parent

```javascript
const parent = username.parentElement;
parent.removeChild(username);
```

---

## Quick Reference

```javascript
// SELECT
const el = document.getElementById("myId");

// TEXT
el.textContent = "New text";      // Set text
el.innerText = "Visible text";    // Set visible text
el.innerHTML = "<b>Bold</b>";     // Set HTML

// CLASSES
el.classList.add("class1", "class2");
el.classList.remove("class1");
el.classList.toggle("class1");
el.classList.contains("class1");  // returns true/false

// STYLES
el.style.color = "red";
el.style.fontSize = "20px";
el.style.backgroundColor = "yellow";

// TRAVERSAL
el.parentElement               // Get parent
el.children                    // Get all children
el.firstElementChild          // Get first child
el.lastElementChild           // Get last child

// REMOVE
el.remove();                   // Delete element
```

---

## 📚 Summary

| Task | Code |
|------|------|
| Select by ID | `document.getElementById("id")` |
| Change text | `el.textContent = "text"` |
| Add class | `el.classList.add("class")` |
| Remove class | `el.classList.remove("class")` |
| Add style | `el.style.color = "red"` |
| Get parent | `el.parentElement` |
| Get children | `el.children` |
| Remove element | `el.remove()` |

---

🎉 **Pro Tip:** Use `classList` for styling (reusable CSS) and `style` for quick one-off changes!
