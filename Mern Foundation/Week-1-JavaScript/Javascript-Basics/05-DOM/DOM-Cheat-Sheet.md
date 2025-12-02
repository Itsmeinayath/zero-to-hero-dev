# 🛡️ DOM Cheat Sheet: Modern vs Old Way

> Quick reference for **what to use** in real projects.

---

## 1. Selecting Elements

```
┌────────────────────────────────────────────────────────────────┐
│  MODERN (Use These)          │  OLD (Avoid)                   │
├────────────────────────────────────────────────────────────────┤
│  querySelector("#id")        │  getElementById("id")          │
│  querySelector(".class")     │  getElementsByClassName()      │
│  querySelectorAll(".items")  │  getElementsByTagName()        │
└────────────────────────────────────────────────────────────────┘
```

| Modern ✅ | Old ❌ | Why Modern Wins |
|-----------|--------|-----------------|
| `querySelector` | `getElementById` | Same syntax for IDs, classes, any CSS selector |
| `querySelectorAll` | `getElementsBy*` | Returns static list + has `.forEach()` built-in |

```javascript
// ✅ Modern - One consistent pattern
document.querySelector("#header");      // by ID
document.querySelector(".btn");         // by class
document.querySelector("div.card > p"); // complex selectors work!

// ❌ Old - Different method for everything
document.getElementById("header");
document.getElementsByClassName("btn")[0];
```

---

## 2. Changing Text

```
┌─────────────────────────────────────────────────────────────────┐
│  textContent    │  innerHTML         │  innerText              │
├─────────────────────────────────────────────────────────────────┤
│  ✅ USE THIS    │  ⚠️ Only for HTML   │  ❌ AVOID              │
│  Fast & Safe    │  XSS Risk!         │  Slow (checks styles)   │
└─────────────────────────────────────────────────────────────────┘
```

```javascript
// ✅ textContent - Safe, treats everything as plain text
element.textContent = "<b>Hello</b>";  
// Shows: <b>Hello</b>  (as text, not bold)

// ⚠️ innerHTML - Renders HTML (danger with user input!)
element.innerHTML = "<b>Hello</b>";    
// Shows: Hello  (bold)

// ❌ innerText - Slower, rarely needed
element.innerText = "Hello";
```

**Rule:** Use `textContent` unless you NEED to render HTML tags.

---

## 3. Changing Classes

```
┌─────────────────────────────────────────────────────────────────┐
│  classList (✅ Precise)        │  className (❌ Destructive)   │
├─────────────────────────────────────────────────────────────────┤
│  .add("new")                   │  = "new"  (WIPES all others!) │
│  .remove("old")                │                               │
│  .toggle("active")             │                               │
│  .contains("check")            │                               │
└─────────────────────────────────────────────────────────────────┘
```

```javascript
// ✅ classList - Surgical precision
element.classList.add("active");      // adds without affecting others
element.classList.remove("hidden");   // removes one class
element.classList.toggle("dark");     // on/off switch

// ❌ className - Nuclear option
element.className = "active";         // DESTROYS all existing classes!
```

---

## 4. Events

```
┌─────────────────────────────────────────────────────────────────┐
│  addEventListener (✅)          │  onclick="" (❌)              │
├─────────────────────────────────────────────────────────────────┤
│  Multiple listeners OK          │  Only ONE allowed             │
│  JS stays in .js file           │  Mixes HTML + JS (messy)      │
│  Easy to remove                 │  Hard to manage               │
└─────────────────────────────────────────────────────────────────┘
```

```javascript
// ✅ Modern
btn.addEventListener("click", handleClick);
btn.addEventListener("click", trackAnalytics); // Can add multiple!

// ❌ Old - Only one works, second overwrites first
btn.onclick = handleClick;
btn.onclick = trackAnalytics; // handleClick is GONE!
```

---

## 5. Creating Elements

```javascript
// ✅ Best Practice
const card = document.createElement("div");
card.className = "card";
card.textContent = "Hello";
container.appendChild(card);

// ⚠️ innerHTML - Quick but risky with user data
container.innerHTML = `<div class="card">Hello</div>`;

// ✅ For multiple elements - Use DocumentFragment
const fragment = document.createDocumentFragment();
items.forEach(item => {
    const li = document.createElement("li");
    li.textContent = item;
    fragment.appendChild(li);
});
list.appendChild(fragment); // One DOM update!
```

---

## 🚀 Quick Reference

```
┌────────────────────┬──────────────────────────────────────────┐
│ Task               │ Use This                                 │
├────────────────────┼──────────────────────────────────────────┤
│ Select one         │ querySelector()                          │
│ Select many        │ querySelectorAll()                       │
│ Change text        │ textContent                              │
│ Render HTML        │ innerHTML (careful!)                     │
│ Add/remove class   │ classList.add() / .remove()              │
│ Toggle class       │ classList.toggle()                       │
│ Handle events      │ addEventListener()                       │
│ Stop default       │ e.preventDefault()                       │
│ Get clicked elem   │ e.target                                 │
│ Create element     │ document.createElement()                 │
│ Add to DOM         │ parent.appendChild(child)                │
│ Remove from DOM    │ element.remove()                         │
└────────────────────┴──────────────────────────────────────────┘
```

---

## ⚡ One-Liners You'll Use Daily

```javascript
// Select & modify
document.querySelector(".btn").classList.add("active");

// Toggle dark mode
document.body.classList.toggle("dark-mode");

// Hide element
element.style.display = "none";

// Get input value
const value = document.querySelector("#input").value;

// Event delegation (handle dynamic elements)
document.querySelector("#list").addEventListener("click", (e) => {
    if (e.target.matches(".delete-btn")) {
        e.target.closest("li").remove();
    }
});
```