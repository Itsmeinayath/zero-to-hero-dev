
## Day 1 — JavaScript Basics (MERN Foundation)

Goal: grasp variables, data types, functions, and control flow to add interactivity to a webpage.

### Learning outcomes
- Use let/const correctly; avoid var in modern code
- Know primitive types (string, number, boolean, undefined, null)
- Write simple functions and use if/switch, for/while

### Theory (60–90 min)
- Variables: prefer const, use let when reassignment is needed; block scope vs function scope
  - Example:
    ```javascript
    let name = "Ada";
    const pi = 3.14159;
    // pi = 3.14; // TypeError
    ```
- Scope:
  ```javascript
  if (true) {
    let x = 1;
  }
  // x is not defined here
  ```
- Data types and basics:
  ```javascript
  const greeting = "Hello"; // string
  const age = 30;            // number
  const isStudent = false;   // boolean
  let notSet;                // undefined
  ```
- Functions and control flow:
  ```javascript
  function add(a, b) { return a + b; }
  const square = (n) => n * n;
  if (age > 18) { /* ... */ } else { /* ... */ }
  for (let i = 0; i < 3; i++) { /* ... */ }
  ```
- Reference: JavaScript.info — Variables
  https://javascript.info/variables

### Practice (60–90 min)
1) Variables & Types
   - Create let/const variables for name, age, isMember; log types with typeof
2) Functions
   - Implement add, subtract, multiply, divide; test with a few values
3) Loops & Arrays
   - Given [1,2,3,4,5], print squares with for and for...of; then map
4) Conditionals
   - Given score 0–100, print a letter grade using if/else or switch

### Mini-exercises (optional)
- Prompt user for two numbers and alert their sum (in browser)
- Format a number to 2 decimals with toFixed(2)

### Tips
- Default to const; switch to let only when you must reassign
- Keep functions small and pure when possible



