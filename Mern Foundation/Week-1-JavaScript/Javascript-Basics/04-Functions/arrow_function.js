// ============================================
// ARROW FUNCTIONS - A Beginner's Guide
// ============================================

// Arrow functions are a shorter way to write functions in JavaScript.
// Think of them as a "nickname" for regular functions - same thing, shorter name!


// ============================================
// 1. BASIC SYNTAX
// ============================================

// REGULAR FUNCTION (the old way)
function sayHelloRegular() {
    console.log("Hello from regular function!");
}

// ARROW FUNCTION (the new way) - same thing, shorter!
const sayHelloArrow = () => {
    console.log("Hello from arrow function!");
};

// Both work the same way:
sayHelloRegular(); // Output: Hello from regular function!
sayHelloArrow();   // Output: Hello from arrow function!


// ============================================
// 2. ARROW FUNCTIONS WITH PARAMETERS
// ============================================

// When you need to pass values to your function:

// REGULAR FUNCTION
function addRegular(num1, num2) {
    return num1 + num2;
}

// ARROW FUNCTION - notice the arrow => 
const addArrow = (num1, num2) => {
    return num1 + num2;
};

console.log(addRegular(5, 3)); // Output: 8
console.log(addArrow(5, 3));   // Output: 8


// ============================================
// 3. SHORT SYNTAX (One-Liner)
// ============================================

// If your function only has ONE line that returns something,
// you can make it even shorter!

// LONG VERSION
const multiplyLong = (a, b) => {
    return a * b;
};

// SHORT VERSION - no curly braces, no 'return' keyword needed!
const multiplyShort = (a, b) => a * b;

// Both do the same thing:
console.log(multiplyLong(4, 5));  // Output: 20
console.log(multiplyShort(4, 5)); // Output: 20

// More examples of one-liners:
const double = (num) => num * 2;
const isEven = (num) => num % 2 === 0;
const greet = (name) => `Hello, ${name}!`;

console.log(double(10));      // Output: 20
console.log(isEven(4));       // Output: true
console.log(greet("Mohammed")); // Output: Hello, Mohammed!


// ============================================
// 4. SINGLE PARAMETER SHORTCUT
// ============================================

// If you have only ONE parameter, you can skip the parentheses!

// With parentheses (both work)
const squareWithParens = (num) => num * num;

// Without parentheses (cleaner for single parameter)
const squareClean = num => num * num;

console.log(squareWithParens(5)); // Output: 25
console.log(squareClean(5));      // Output: 25

// BUT! If you have NO parameters, you MUST use empty parentheses:
const sayHi = () => "Hi there!";
console.log(sayHi()); // Output: Hi there!


// ============================================
// 5. THE 'arguments' KEYWORD (Key Difference!)
// ============================================

// Regular functions have a special 'arguments' object
// that contains ALL values passed to the function.

function showAllArguments() {
    console.log("Regular function arguments:", arguments);
}

showAllArguments(1, 2, 3, 4, 5); 
// Output: Regular function arguments: [1, 2, 3, 4, 5]

// Arrow functions DON'T have 'arguments'!
// Instead, use "rest parameters" with three dots (...)

const showAllArgsArrow = (...allMyArgs) => {
    console.log("Arrow function with rest:", allMyArgs);
};

showAllArgsArrow(1, 2, 3, 4, 5);
// Output: Arrow function with rest: [1, 2, 3, 4, 5]


// ============================================
// 6. HOISTING (Order Matters!)
// ============================================

// HOISTING = JavaScript's behavior of moving declarations to the top

// With REGULAR FUNCTIONS - you can call them BEFORE defining them:
sayGoodbye(); // This works! ✅

function sayGoodbye() {
    console.log("Goodbye!");
}

// With ARROW FUNCTIONS - you MUST define them BEFORE calling:
// sayHiFirst(); // ❌ ERROR! Cannot use before it's defined!

const sayHiFirst = () => {
    console.log("Hi first!");
};

sayHiFirst(); // This works! ✅ (defined before calling)


// ============================================
// 7. PRACTICAL EXAMPLES
// ============================================

// Example 1: Working with arrays
const numbers = [1, 2, 3, 4, 5];

// Double each number
const doubled = numbers.map(num => num * 2);
console.log("Doubled:", doubled); // Output: [2, 4, 6, 8, 10]

// Filter even numbers
const evens = numbers.filter(num => num % 2 === 0);
console.log("Evens:", evens); // Output: [2, 4]

// Example 2: Calculate total
const prices = [10, 20, 30];
const total = prices.reduce((sum, price) => sum + price, 0);
console.log("Total:", total); // Output: 60


// ============================================
// SUMMARY - When to Use Each
// ============================================

/*
✅ USE ARROW FUNCTIONS FOR:
   - Short, simple functions
   - Array methods (map, filter, reduce, forEach)
   - Callbacks (functions passed to other functions)

❌ DON'T USE ARROW FUNCTIONS FOR:
   - Object methods (when you need 'this')
   - When you need 'arguments' keyword
   - Constructor functions (with 'new')

QUICK SYNTAX REFERENCE:
   - No parameters:     () => { code }
   - One parameter:     param => { code }  OR  (param) => { code }
   - Multiple params:   (a, b) => { code }
   - One-line return:   (a, b) => a + b  (no braces, no return)
*/

