/*
=====================================================
 Day 1 Playground: JavaScript Fundamentals (Basic.js)
-----------------------------------------------------
 Run:  node Basic.js
 Purpose: Self‑contained examples for variables, conditionals,
                    loops, and functions. Trimmed & structured.
=====================================================
*/

// SECTION 1: VARIABLES & TYPES -------------------------------------------
// Use const by default, let when you need reassignment.
const name = "John";      // string
let age = 30;              // number (dynamic type)
const isStudent = true;    // boolean
const country = "India";  // another constant

console.log("--- Variables ---");
console.log({ name, age, isStudent, country });

// SECTION 2: CONDITIONALS ------------------------------------------------
console.log("\n--- Conditionals ---");
if (age >= 18) {
    console.log("Adult");
} else {
    console.log("Minor");
}

// Nested (avoid deep nesting; here just for demonstration)
if (age < 18) {
    console.log("Minor (nested check)");
} else if (age < 65) {
    console.log("Adult (nested check)");
} else {
    console.log("Senior (nested check)");
}

// Ternary example
const statusLabel = age >= 18 ? "Eligible" : "Not Eligible";
console.log("Status (ternary):", statusLabel);

// SECTION 3: LOOPS GALLERY -----------------------------------------------
console.log("\n--- Loops Gallery ---");

// For loop (counting)
for (let i = 0; i < 3; i++) {
    console.log("for i=", i);
}

// While loop (condition evaluated before body)
let w = 0;
while (w < 3) {
    console.log("while w=", w);
    w++;
}

// Do...while (runs at least once)
let d = 0;
do {
    console.log("do...while d=", d);
    d++;
} while (d < 3);

// Array iteration: for...of
const numbers = [1, 2, 3];
for (const n of numbers) {
    console.log("for...of value=", n);
}

// Object property iteration: for...in
const stats = { a: 10, b: 20, c: 30 };
for (const key in stats) {
    console.log(`for...in ${key} ->`, stats[key]);
}

// forEach (callback style)
numbers.forEach((n, idx) => console.log(`forEach idx=${idx} val=${n}`));

// SECTION 4: FUNCTIONS ---------------------------------------------------
console.log("\n--- Functions ---");

// Declaration (hoisted)
function add(a, b) {
    return a + b;
}

// Function expression
const multiply = function (a, b) {
    return a * b;
};

// Arrow function (concise)
const square = n => n * n;

console.log("add(5,10) =", add(5, 10));
console.log("multiply(5,10) =", multiply(5, 10));
console.log("square(6) =", square(6));

// Arrow 'this' note (brief illustration)
const objExample = {
    label: "Demo",
    normalFn: function () { return this.label; },
    arrowFn: () => this && this.label
};
console.log("normalFn this ->", objExample.normalFn()); // 'Demo'
console.log("arrowFn this ->", objExample.arrowFn());  // likely undefined (lexical this)

// SECTION 5: MINI PRACTICE PROMPTS (COMMENTS) ---------------------------
// Try implementing (not executed here):
// 1. Write a function that returns the max of two numbers.
// 2. Sum all numbers in an array (loop or reduce).
// 3. Create an object representing a book: { title, author, year } and log a formatted string.
// 4. Add a function that counts vowels in a string.
// 5. Convert a for loop example into a while loop version.

// SECTION 6: SUMMARY OUTPUT ---------------------------------------------
console.log("\nSummary: basics executed successfully ✅");

/*
Key Takeaways:
 - Prefer const; use let only when reassignment needed.
 - Use strict comparisons (===) to avoid coercion surprises.
 - Keep functions small & descriptive.
 - Choose the simplest loop that reads well (for...of over index loops when index not needed).
 - Arrow functions inherit 'this'; declarations have their own.
*/


