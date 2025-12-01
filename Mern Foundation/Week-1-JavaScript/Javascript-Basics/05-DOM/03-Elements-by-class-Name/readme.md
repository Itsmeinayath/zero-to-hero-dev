# getElementsBy* Methods - Complete Guide

## 📚 Table of Contents

- [Overview: Element vs Elements](#overview-element-vs-elements)
- [getElementsByClassName](#getelementsbyclassname)
- [getElementsByTagName](#getelementsbytagname)
- [Key Difference: HTMLCollection](#key-difference-htmlcollection)
- [Looping Through Elements](#looping-through-elements)
- [Live vs Static Collections](#live-vs-static-collections)
- [Comparison Table](#comparison-table)
- [Quick Reference](#quick-reference)

---

## Overview: Element vs Elements

| Method | Returns | Use For |
|--------|---------|---------|
| `getElementById()` | **Single** element | Unique ID (one element) |
| `getElementsByClassName()` | **Multiple** elements | All elements with a class |
| `getElementsByTagName()` | **Multiple** elements | All elements of a tag type |

> 💡 Notice the **"s"** in Element**s** - it means "give me ALL matching elements"!

---

## getElementsByClassName

Select **all elements** that have a specific class name.

### Syntax

```javascript
document.getElementsByClassName("className");
```

### Example

```html
<p class="paragraph">First paragraph</p>
<p class="paragraph">Second paragraph</p>
<p class="paragraph">Third paragraph</p>
<p class="other">Different class</p>
```

```javascript
// Get ALL elements with class "paragraph"
const paragraphs = document.getElementsByClassName("paragraph");

console.log(paragraphs);
// Output: HTMLCollection(3) [p.paragraph, p.paragraph, p.paragraph]

console.log(paragraphs.length);
// Output: 3
```

**Visual: What We Selected:**
```
<p class="paragraph">First paragraph</p>   ← ✅ Selected [0]
<p class="paragraph">Second paragraph</p>  ← ✅ Selected [1]
<p class="paragraph">Third paragraph</p>   ← ✅ Selected [2]
<p class="other">Different class</p>       ← ❌ NOT selected
```

### Access Individual Elements

```javascript
const paragraphs = document.getElementsByClassName("paragraph");

// Access by index (like an array)
console.log(paragraphs[0].textContent);  // Output: First paragraph
console.log(paragraphs[1].textContent);  // Output: Second paragraph
console.log(paragraphs[2].textContent);  // Output: Third paragraph
```

### Style All Elements

```javascript
const paragraphs = document.getElementsByClassName("paragraph");

// ❌ WRONG - Can't style the collection directly
paragraphs.style.color = "red";  // ERROR!

// ✅ CORRECT - Loop through each element
for (let i = 0; i < paragraphs.length; i++) {
    paragraphs[i].style.color = "red";
}
```

**Visual Output:**
```
BEFORE:                      AFTER:
First paragraph         →    First paragraph    (red)
Second paragraph             Second paragraph   (red)
Third paragraph              Third paragraph    (red)
Different class              Different class    (unchanged)
```

---

## getElementsByTagName

Select **all elements** of a specific HTML tag.

### Syntax

```javascript
document.getElementsByTagName("tagName");
```

### Example

```html
<div>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
    <span>A span element</span>
    <p>Paragraph 3</p>
</div>
```

```javascript
// Get ALL <p> elements
const allParagraphs = document.getElementsByTagName("p");

console.log(allParagraphs);
// Output: HTMLCollection(3) [p, p, p]

console.log(allParagraphs.length);
// Output: 3

// Get ALL <span> elements
const allSpans = document.getElementsByTagName("span");
console.log(allSpans.length);
// Output: 1
```

**Visual: What We Selected:**
```
<p>Paragraph 1</p>        ← ✅ allParagraphs[0]
<p>Paragraph 2</p>        ← ✅ allParagraphs[1]
<span>A span element</span>  ← ❌ NOT in allParagraphs
<p>Paragraph 3</p>        ← ✅ allParagraphs[2]
```

### Select All Elements

```javascript
// Get EVERY element in the document
const allElements = document.getElementsByTagName("*");
console.log(allElements.length);  // Total number of elements
```

---

## Key Difference: HTMLCollection

Both `getElementsByClassName` and `getElementsByTagName` return an **HTMLCollection**, NOT an array.

### HTMLCollection vs Array

```javascript
const paragraphs = document.getElementsByClassName("paragraph");

// ✅ Works - Access by index
console.log(paragraphs[0]);

// ✅ Works - Get length
console.log(paragraphs.length);

// ❌ FAILS - forEach doesn't work on HTMLCollection!
paragraphs.forEach(p => console.log(p));  // ERROR!

// ✅ Solution - Convert to array first
Array.from(paragraphs).forEach(p => console.log(p));
```

| Feature | HTMLCollection | Array |
|---------|---------------|-------|
| Access by index `[0]` | ✅ Yes | ✅ Yes |
| `.length` | ✅ Yes | ✅ Yes |
| `.forEach()` | ❌ No | ✅ Yes |
| `.map()` | ❌ No | ✅ Yes |
| `.filter()` | ❌ No | ✅ Yes |

---

## Looping Through Elements

### Method 1: Classic for Loop (Always Works)

```javascript
const items = document.getElementsByClassName("item");

for (let i = 0; i < items.length; i++) {
    items[i].style.color = "blue";
}
```

### Method 2: for...of Loop

```javascript
const items = document.getElementsByClassName("item");

for (const item of items) {
    item.style.color = "blue";
}
```

### Method 3: Convert to Array

```javascript
const items = document.getElementsByClassName("item");

// Using Array.from()
Array.from(items).forEach(item => {
    item.style.color = "blue";
});

// Using spread operator
[...items].forEach(item => {
    item.style.color = "blue";
});
```

**Visual: Styling All Items:**
```
BEFORE:                    AFTER (all blue):
┌─────────────┐           ┌─────────────┐
│ Item 1      │           │ Item 1      │ (blue)
│ Item 2      │     →     │ Item 2      │ (blue)
│ Item 3      │           │ Item 3      │ (blue)
└─────────────┘           └─────────────┘
```

---

## Live vs Static Collections

### HTMLCollection is LIVE

This means it automatically updates when the DOM changes!

```html
<div id="container">
    <p class="item">Item 1</p>
    <p class="item">Item 2</p>
</div>
```

```javascript
const items = document.getElementsByClassName("item");
console.log(items.length);  // Output: 2

// Add a new element
const newItem = document.createElement("p");
newItem.className = "item";
newItem.textContent = "Item 3";
document.getElementById("container").appendChild(newItem);

// Collection automatically updates!
console.log(items.length);  // Output: 3  ← Updated automatically!
```

**Visual:**
```
STEP 1: Get collection          STEP 2: Add new item
items.length = 2                items.length = 3 (auto-updated!)

┌─────────────┐                ┌─────────────┐
│ Item 1      │                │ Item 1      │
│ Item 2      │       →        │ Item 2      │
└─────────────┘                │ Item 3      │ ← NEW!
                               └─────────────┘
```

### querySelectorAll is STATIC

```javascript
const items = document.querySelectorAll(".item");
console.log(items.length);  // Output: 2

// Add new element...
// items.length is still 2! (doesn't update)
```

---

## Comparison Table

| Feature | `getElementById` | `getElementsByClassName` | `getElementsByTagName` | `querySelectorAll` |
|---------|-----------------|------------------------|----------------------|-------------------|
| **Returns** | Single element | HTMLCollection | HTMLCollection | NodeList |
| **Count** | 1 or null | 0 or more | 0 or more | 0 or more |
| **Live?** | N/A | ✅ Yes | ✅ Yes | ❌ No (static) |
| **forEach?** | N/A | ❌ No | ❌ No | ✅ Yes |
| **Speed** | ⚡ Fastest | ⚡ Fast | ⚡ Fast | 🐢 Slower |

---

## Practical Examples

### Example 1: Change All Paragraphs

```html
<p class="text">Paragraph 1</p>
<p class="text">Paragraph 2</p>
<p class="text">Paragraph 3</p>
```

```javascript
const texts = document.getElementsByClassName("text");

for (let i = 0; i < texts.length; i++) {
    texts[i].style.backgroundColor = "yellow";
    texts[i].style.padding = "10px";
}
```

**Visual Output:**
```
BEFORE:              AFTER:
Paragraph 1     →    ▓ Paragraph 1 ▓  (yellow bg)
Paragraph 2          ▓ Paragraph 2 ▓  (yellow bg)
Paragraph 3          ▓ Paragraph 3 ▓  (yellow bg)
```

### Example 2: Count Elements

```javascript
const allDivs = document.getElementsByTagName("div");
const allLinks = document.getElementsByTagName("a");

console.log(`This page has ${allDivs.length} divs`);
console.log(`This page has ${allLinks.length} links`);
```

### Example 3: Hide All Elements of a Class

```javascript
const warnings = document.getElementsByClassName("warning");

for (const warning of warnings) {
    warning.style.display = "none";
}
```

**Visual Output:**
```
BEFORE:                    AFTER:
┌─────────────────┐       ┌─────────────────┐
│ ⚠️ Warning 1    │       │                 │
│ ⚠️ Warning 2    │  →    │  (all hidden!)  │
│ ⚠️ Warning 3    │       │                 │
└─────────────────┘       └─────────────────┘
```

### Example 4: Add Click Event to Multiple Buttons

```html
<button class="btn">Button 1</button>
<button class="btn">Button 2</button>
<button class="btn">Button 3</button>
```

```javascript
const buttons = document.getElementsByClassName("btn");

for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", function() {
        this.style.backgroundColor = "green";
        this.textContent = "Clicked!";
    });
}
```

**Visual Output:**
```
BEFORE (click Button 2):        AFTER:
┌──────────┐                   ┌──────────┐
│ Button 1 │                   │ Button 1 │
│ Button 2 │  ← Click!    →    │ Clicked! │ (green)
│ Button 3 │                   │ Button 3 │
└──────────┘                   └──────────┘
```

---

## Quick Reference

```javascript
// SELECT MULTIPLE BY CLASS
const items = document.getElementsByClassName("className");

// SELECT MULTIPLE BY TAG
const paragraphs = document.getElementsByTagName("p");
const allElements = document.getElementsByTagName("*");

// ACCESS
items[0]              // First element
items[1]              // Second element
items.length          // Total count

// LOOP - Classic for
for (let i = 0; i < items.length; i++) {
    items[i].style.color = "red";
}

// LOOP - for...of
for (const item of items) {
    item.style.color = "red";
}

// LOOP - Convert to array
Array.from(items).forEach(item => {
    item.style.color = "red";
});

// CONVERT TO ARRAY
const itemsArray = Array.from(items);
const itemsArray2 = [...items];
```

---

## 📚 Summary

| Method | What It Does | Returns |
|--------|-------------|---------|
| `getElementById("id")` | Gets ONE element by ID | Single element |
| `getElementsByClassName("class")` | Gets ALL elements with class | HTMLCollection (live) |
| `getElementsByTagName("tag")` | Gets ALL elements of tag type | HTMLCollection (live) |
| `querySelectorAll(".class")` | Gets ALL matching elements | NodeList (static) |

### Key Takeaways

✅ Use `getElementsByClassName` to select multiple elements by class  
✅ Use `getElementsByTagName` to select all elements of a tag  
✅ Returns HTMLCollection - must loop to style  
✅ HTMLCollection is LIVE (auto-updates)  
✅ Convert to array for `forEach`, `map`, `filter`  
✅ Use classic `for` loop or `for...of` for best compatibility  

---

🎉 **Pro Tip:** For modern code, `querySelectorAll` is often preferred because it returns a NodeList that supports `forEach` directly!
