# 📦 JavaScript Arrays - Complete Guide

> **Master Arrays & Higher-Order Methods** - Store, manipulate, and transform data efficiently!

---

## 📚 Table of Contents

1. [What Are Arrays?](#1-what-are-arrays)
2. [Creating Arrays](#2-creating-arrays)
3. [Array Methods - Basic](#3-array-methods---basic)
4. [Higher-Order Array Methods](#4-higher-order-array-methods)
5. [forEach vs map vs filter vs for loop](#5-foreach-vs-map-vs-filter-vs-for-loop)
6. [Other Useful Methods](#6-other-useful-methods)
7. [Array Destructuring](#7-array-destructuring)
8. [Spread Operator](#8-spread-operator)

---

## 1. What Are Arrays?

An **array** is a special variable that can hold **multiple values** in a single ordered list.

```javascript
// Instead of this:
const fruit1 = "Apple";
const fruit2 = "Banana";
const fruit3 = "Orange";

// Use this:
const fruits = ["Apple", "Banana", "Orange"];
```

**Key Features:**
- Arrays use **index** (position) starting from `0`
- Can hold **different data types** (strings, numbers, objects, even other arrays!)
- Have a **length** property

```javascript
const mixedArray = ["John", 25, true, null, {city: "NYC"}];
console.log(mixedArray[0]);    // "John"
console.log(mixedArray.length); // 5
```

---

## 2. Creating Arrays

```javascript
// Method 1: Array literal (recommended)
const numbers = [1, 2, 3, 4, 5];

// Method 2: Array constructor
const colors = new Array("red", "green", "blue");

// Empty array
const empty = [];
```

---

## 3. Array Methods - Basic

### Adding Elements

```javascript
const fruits = ["Apple", "Banana"];

// Add to END
fruits.push("Orange");
console.log(fruits); // ["Apple", "Banana", "Orange"]

// Add to START
fruits.unshift("Mango");
console.log(fruits); // ["Mango", "Apple", "Banana", "Orange"]
```

**Visual:**
```
BEFORE:  ["Apple", "Banana"]
         
.push("Orange")      → ["Apple", "Banana", "Orange"]    (END)
.unshift("Mango")    → ["Mango", "Apple", "Banana"]     (START)
```

### Removing Elements

```javascript
const fruits = ["Mango", "Apple", "Banana", "Orange"];

// Remove from END
fruits.pop();
console.log(fruits); // ["Mango", "Apple", "Banana"]

// Remove from START
fruits.shift();
console.log(fruits); // ["Apple", "Banana"]
```

**Visual:**
```
BEFORE:  ["Mango", "Apple", "Banana", "Orange"]
         
.pop()     → ["Mango", "Apple", "Banana"]   (removes last)
.shift()   → ["Apple", "Banana", "Orange"]  (removes first)
```

### Finding Elements

```javascript
const fruits = ["Apple", "Banana", "Cherry"];

// Get index of element
console.log(fruits.indexOf("Banana"));     // 1
console.log(fruits.indexOf("Mango"));      // -1 (not found)

// Check if exists
console.log(fruits.includes("Cherry"));    // true
console.log(fruits.includes("Mango"));     // false
```

### Other Basics

```javascript
const fruits = ["Apple", "Banana", "Cherry"];

// Length
console.log(fruits.length);  // 3

// Reverse (modifies original!)
fruits.reverse();
console.log(fruits);  // ["Cherry", "Banana", "Apple"]

// Join into string
const str = fruits.join(" - ");
console.log(str);  // "Cherry - Banana - Apple"
```

---

## 4. Higher-Order Array Methods

Higher-order methods are functions that **take a function as an argument** (callback).

### 🔄 forEach - Loop Through Array

**Purpose:** Execute a function for each element (for side effects like logging).

```javascript
const numbers = [1, 2, 3, 4, 5];

// Traditional for loop
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}

// forEach (cleaner)
numbers.forEach((num) => {
    console.log(num);
});

// forEach with index
numbers.forEach((num, index) => {
    console.log(`Index ${index}: ${num}`);
});
```

**Output:**
```
Index 0: 1
Index 1: 2
Index 2: 3
Index 3: 4
Index 4: 5
```

⚠️ **Important:** `forEach` does NOT return anything!

---

### 🔀 map - Transform Each Element

**Purpose:** Create a **new array** by transforming each element.

```javascript
const numbers = [1, 2, 3, 4, 5];

// Double each number
const doubled = numbers.map((num) => num * 2);
console.log(doubled);  // [2, 4, 6, 8, 10]
console.log(numbers);  // [1, 2, 3, 4, 5] (original unchanged!)

// More complex transformation
const users = [
    { name: "John", age: 25 },
    { name: "Jane", age: 30 }
];

const names = users.map((user) => user.name);
console.log(names);  // ["John", "Jane"]
```

**Visual:**
```
BEFORE:  [1, 2, 3, 4, 5]
           ↓  ↓  ↓  ↓  ↓  (multiply by 2)
AFTER:   [2, 4, 6, 8, 10]  ← NEW ARRAY
```

---

### 🔍 filter - Keep Only Matching Elements

**Purpose:** Create a **new array** with elements that pass a test.

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Get only even numbers
const evens = numbers.filter((num) => num % 2 === 0);
console.log(evens);  // [2, 4, 6, 8, 10]

// Filter users by age
const users = [
    { name: "John", age: 17 },
    { name: "Jane", age: 25 },
    { name: "Bob", age: 30 }
];

const adults = users.filter((user) => user.age >= 18);
console.log(adults);  
// [{ name: "Jane", age: 25 }, { name: "Bob", age: 30 }]
```

**Visual:**
```
BEFORE:  [1, 2, 3, 4, 5, 6]
          ✗  ✓  ✗  ✓  ✗  ✓  (keep only even)
AFTER:   [2, 4, 6]  ← NEW ARRAY (smaller)
```

---

### 🎯 find - Get First Match

**Purpose:** Return the **first element** that passes a test.

```javascript
const users = [
    { id: 1, name: "John" },
    { id: 2, name: "Jane" },
    { id: 3, name: "Bob" }
];

const user = users.find((user) => user.id === 2);
console.log(user);  // { id: 2, name: "Jane" }

const notFound = users.find((user) => user.id === 99);
console.log(notFound);  // undefined
```

---

### 📍 findIndex - Get First Match Index

**Purpose:** Return the **index** of the first element that passes a test.

```javascript
const fruits = ["Apple", "Banana", "Cherry", "Banana"];

const index = fruits.findIndex((fruit) => fruit === "Banana");
console.log(index);  // 1 (first occurrence)

const notFound = fruits.findIndex((fruit) => fruit === "Mango");
console.log(notFound);  // -1
```

---

### ➕ reduce - Accumulate/Combine Values

**Purpose:** Reduce array to a **single value** (sum, product, etc.).

```javascript
const numbers = [1, 2, 3, 4, 5];

// Sum all numbers
const sum = numbers.reduce((accumulator, current) => {
    return accumulator + current;
}, 0);  // 0 is initial value
console.log(sum);  // 15

// Shorter version
const sum2 = numbers.reduce((acc, cur) => acc + cur, 0);
console.log(sum2);  // 15
```

**How reduce works:**
```
Step 1: acc = 0,  current = 1  →  0 + 1 = 1
Step 2: acc = 1,  current = 2  →  1 + 2 = 3
Step 3: acc = 3,  current = 3  →  3 + 3 = 6
Step 4: acc = 6,  current = 4  →  6 + 4 = 10
Step 5: acc = 10, current = 5  →  10 + 5 = 15
Result: 15
```

---

## 5. forEach vs map vs filter vs for loop

```
┌──────────────┬─────────────┬──────────────┬───────────────────┐
│ Method       │ Returns     │ Creates New  │ Use Case          │
│              │             │ Array?       │                   │
├──────────────┼─────────────┼──────────────┼───────────────────┤
│ for loop     │ Nothing     │ No           │ Full control      │
│              │             │              │ (break/continue)  │
├──────────────┼─────────────┼──────────────┼───────────────────┤
│ forEach      │ undefined   │ No           │ Execute code for  │
│              │             │              │ each item (log)   │
├──────────────┼─────────────┼──────────────┼───────────────────┤
│ map          │ New array   │ Yes ✓        │ Transform each    │
│              │             │              │ element           │
├──────────────┼─────────────┼──────────────┼───────────────────┤
│ filter       │ New array   │ Yes ✓        │ Keep matching     │
│              │             │              │ elements          │
└──────────────┴─────────────┴──────────────┴───────────────────┘
```

### Side-by-Side Comparison

```javascript
const numbers = [1, 2, 3, 4, 5];

// ──────────────────────────────────────────────────────
// FOR LOOP - Traditional
// ──────────────────────────────────────────────────────
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i] * 2);
}
// Logs: 2, 4, 6, 8, 10
// Returns: nothing

// ──────────────────────────────────────────────────────
// forEach - Execute function (no return value)
// ──────────────────────────────────────────────────────
const result1 = numbers.forEach((num) => {
    console.log(num * 2);
    return num * 2;  // This return is IGNORED!
});
// Logs: 2, 4, 6, 8, 10
console.log(result1);  // undefined ❌

// ──────────────────────────────────────────────────────
// map - Transform and CREATE NEW ARRAY
// ──────────────────────────────────────────────────────
const result2 = numbers.map((num) => {
    return num * 2;
});
console.log(result2);  // [2, 4, 6, 8, 10] ✓

// ──────────────────────────────────────────────────────
// filter - CREATE NEW ARRAY with matches only
// ──────────────────────────────────────────────────────
const result3 = numbers.filter((num) => {
    return num > 2;
});
console.log(result3);  // [3, 4, 5] ✓
```

### Real-World Example

```javascript
const products = [
    { name: "Laptop", price: 1000, inStock: true },
    { name: "Phone", price: 500, inStock: false },
    { name: "Tablet", price: 300, inStock: true },
    { name: "Watch", price: 200, inStock: true }
];

// ✅ Use filter - Get available products
const available = products.filter((p) => p.inStock);
console.log(available);
// [{ name: "Laptop", ... }, { name: "Tablet", ... }, { name: "Watch", ... }]

// ✅ Use map - Get just the names
const names = products.map((p) => p.name);
console.log(names);
// ["Laptop", "Phone", "Tablet", "Watch"]

// ✅ Use forEach - Log each product (side effect)
products.forEach((p) => {
    console.log(`${p.name}: $${p.price}`);
});
// Logs each product, returns nothing

// 🔥 CHAINING - Combine multiple methods!
const cheapAvailable = products
    .filter((p) => p.inStock)        // Get available
    .filter((p) => p.price < 500)     // Get cheap ones
    .map((p) => p.name);              // Get names only

console.log(cheapAvailable);  // ["Tablet", "Watch"]
```

**Visual Flow:**
```
products (4 items)
    ↓
.filter(inStock)  →  [Laptop, Tablet, Watch]  (3 items)
    ↓
.filter(price<500) →  [Tablet, Watch]         (2 items)
    ↓
.map(name)         →  ["Tablet", "Watch"]     (2 strings)
```

---

## 6. Other Useful Methods

### slice - Copy Portion (Doesn't Modify Original)

```javascript
const fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"];

// slice(start, end) - end NOT included
const sliced = fruits.slice(1, 4);
console.log(sliced);   // ["Banana", "Cherry", "Date"]
console.log(fruits);   // Original unchanged!

// Copy entire array
const copy = fruits.slice();
```

**Visual:**
```
Index:     0        1         2        3         4
Array:  ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
                    ↑                   ↑
                 start=1             end=4 (not included)
                    
Result: ["Banana", "Cherry", "Date"]
```

### splice - Add/Remove Elements (Modifies Original!)

```javascript
const fruits = ["Apple", "Banana", "Cherry", "Date"];

// splice(start, deleteCount, itemsToAdd...)
fruits.splice(2, 1, "Mango", "Orange");
//           ↑   ↑   ↑
//       index  remove  add these
//              1 item

console.log(fruits);
// ["Apple", "Banana", "Mango", "Orange", "Date"]
```

**Visual:**
```
BEFORE: ["Apple", "Banana", "Cherry", "Date"]
                             ↓ Remove "Cherry" (index 2)
                             ↓ Insert "Mango", "Orange"
AFTER:  ["Apple", "Banana", "Mango", "Orange", "Date"]
```

### some & every - Test Array

```javascript
const numbers = [1, 2, 3, 4, 5];

// some - At least ONE passes?
const hasEven = numbers.some((num) => num % 2 === 0);
console.log(hasEven);  // true (2 and 4 are even)

// every - ALL pass?
const allEven = numbers.every((num) => num % 2 === 0);
console.log(allEven);  // false (1, 3, 5 are odd)
```

### sort - Sort Array (Modifies Original!)

```javascript
const numbers = [5, 2, 8, 1, 9];

// Numbers need compare function!
numbers.sort((a, b) => a - b);  // Ascending
console.log(numbers);  // [1, 2, 5, 8, 9]

numbers.sort((a, b) => b - a);  // Descending
console.log(numbers);  // [9, 8, 5, 2, 1]

// Strings work without compare function
const fruits = ["Banana", "Apple", "Cherry"];
fruits.sort();
console.log(fruits);  // ["Apple", "Banana", "Cherry"]
```

---

## 7. Array Destructuring

Extract values from arrays into variables:

```javascript
const fruits = ["Apple", "Banana", "Cherry"];

// Old way
const first = fruits[0];
const second = fruits[1];

// New way (destructuring)
const [first, second, third] = fruits;
console.log(first);   // "Apple"
console.log(second);  // "Banana"
console.log(third);   // "Cherry"

// Skip elements
const [a, , c] = fruits;
console.log(a);  // "Apple"
console.log(c);  // "Cherry" (skipped "Banana")

// Rest operator
const [head, ...rest] = fruits;
console.log(head);  // "Apple"
console.log(rest);  // ["Banana", "Cherry"]
```

---

## 8. Spread Operator

The `...` operator spreads array elements:

```javascript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

// Combine arrays
const combined = [...arr1, ...arr2];
console.log(combined);  // [1, 2, 3, 4, 5, 6]

// Copy array
const copy = [...arr1];
console.log(copy);  // [1, 2, 3]

// Add elements
const expanded = [0, ...arr1, 4];
console.log(expanded);  // [0, 1, 2, 3, 4]

// Spread into function
const numbers = [1, 2, 3];
console.log(Math.max(...numbers));  // 3
// Same as: Math.max(1, 2, 3)
```

---

## 🚀 Quick Reference

```javascript
// BASIC
.push(item)         // Add to end
.pop()              // Remove from end
.unshift(item)      // Add to start
.shift()            // Remove from start
.length             // Get size

// SEARCH
.indexOf(item)      // Get index (-1 if not found)
.includes(item)     // Check exists (true/false)
.find(fn)           // Get first match
.findIndex(fn)      // Get index of first match

// TRANSFORM
.map(fn)            // Transform each → new array
.filter(fn)         // Keep matches → new array
.reduce(fn, init)   // Combine to single value

// LOOP
.forEach(fn)        // Execute for each (no return)

// SLICE/SPLICE
.slice(start, end)  // Copy portion (no modify)
.splice(i, n, ...)  // Add/remove (modifies!)

// TEST
.some(fn)           // At least one passes?
.every(fn)          // All pass?

// OTHER
.sort(fn)           // Sort (modifies!)
.reverse()          // Reverse (modifies!)
.join(separator)    // Array → string
```

---

## 📝 Practice Exercises

```javascript
// Exercise 1: Double all numbers
const nums = [1, 2, 3, 4, 5];
const doubled = nums.map((n) => n * 2);

// Exercise 2: Get adults only
const users = [
    { name: "John", age: 17 },
    { name: "Jane", age: 25 }
];
const adults = users.filter((u) => u.age >= 18);

// Exercise 3: Sum all numbers
const total = nums.reduce((sum, n) => sum + n, 0);

// Exercise 4: Chain methods
const result = nums
    .filter((n) => n > 2)   // [3, 4, 5]
    .map((n) => n * 2)      // [6, 8, 10]
    .reduce((sum, n) => sum + n, 0);  // 24
```

---

> **Next Steps:** Practice chaining methods together - that's where the real power is! 🔥