# JavaScript Functions - Complete Guide

## 📚 Table of Contents
- [What is a Function?](#what-is-a-function)
- [Function Declaration](#function-declaration)
- [Function Expression](#function-expression)
- [Arrow Functions](#arrow-functions)
- [Parameters and Arguments](#parameters-and-arguments)
- [Return Statement](#return-statement)
- [Function Scope](#function-scope)
- [Callback Functions](#callback-functions)
- [Higher-Order Functions](#higher-order-functions)
- [Immediately Invoked Function Expression (IIFE)](#iife)
- [Best Practices](#best-practices)
- [Practice Exercises](#practice-exercises)

---

## What is a Function?

A **function** is a reusable block of code designed to perform a specific task. Functions help organize code, make it more readable, and reduce repetition.

### Why Use Functions?

✅ **Reusability** - Write once, use multiple times  
✅ **Organization** - Break complex problems into smaller pieces  
✅ **Maintainability** - Easier to debug and update code  
✅ **Abstraction** - Hide implementation details  

---

## Function Declaration

The most common way to define a function using the `function` keyword.

### Syntax
```javascript
function functionName(parameters) {
    // Code to execute
    return value; // Optional
}
```

### Examples

#### Basic Function
```javascript
function greet() {
    console.log("Hello, World!");
}

greet(); // Output: Hello, World!
```

#### Function with Parameters
```javascript
function greetUser(name) {
    console.log(`Hello, ${name}!`);
}

greetUser("Alice");  // Output: Hello, Alice!
greetUser("Bob");    // Output: Hello, Bob!
```

#### Function with Return Value
```javascript
function add(a, b) {
    return a + b;
}

let sum = add(5, 3);
console.log(sum); // Output: 8
```

#### Function with Multiple Parameters
```javascript
function calculateArea(length, width) {
    return length * width;
}

let area = calculateArea(10, 5);
console.log(`Area: ${area}`); // Output: Area: 50
```

### 🔑 Key Points
- Function declarations are **hoisted** (can be called before definition)
- Use descriptive names (verbs: `calculateTotal`, `getUserData`)

---

## Function Expression

A function stored in a variable. These are **not hoisted**.

### Syntax
```javascript
const functionName = function(parameters) {
    // Code to execute
    return value;
};
```

### Examples

#### Anonymous Function Expression
```javascript
const multiply = function(x, y) {
    return x * y;
};

console.log(multiply(4, 5)); // Output: 20
```

#### Named Function Expression
```javascript
const factorial = function fact(n) {
    if (n <= 1) return 1;
    return n * fact(n - 1);
};

console.log(factorial(5)); // Output: 120
```

### 📌 Difference from Declaration

```javascript
// This works (hoisting)
sayHi(); 
function sayHi() {
    console.log("Hi!");
}

// This throws an error (no hoisting)
sayBye(); // ❌ Error: Cannot access 'sayBye' before initialization
const sayBye = function() {
    console.log("Bye!");
};
```

---

## Arrow Functions

Modern, concise syntax introduced in ES6. Great for shorter functions.

### Syntax
```javascript
const functionName = (parameters) => {
    // Code to execute
    return value;
};

// Shorter syntax for single expression
const functionName = (parameters) => expression;
```

### Examples

#### Basic Arrow Function
```javascript
const greet = () => {
    console.log("Hello!");
};

greet(); // Output: Hello!
```

#### With Parameters
```javascript
const square = (num) => {
    return num * num;
};

console.log(square(4)); // Output: 16
```

#### Implicit Return (Single Expression)
```javascript
const cube = num => num * num * num;
console.log(cube(3)); // Output: 27

const add = (a, b) => a + b;
console.log(add(10, 5)); // Output: 15
```

#### Multiple Parameters
```javascript
const getFullName = (firstName, lastName) => `${firstName} ${lastName}`;
console.log(getFullName("John", "Doe")); // Output: John Doe
```

#### Arrow Functions in Arrays
```javascript
const numbers = [1, 2, 3, 4, 5];

// Double each number
const doubled = numbers.map(num => num * 2);
console.log(doubled); // Output: [2, 4, 6, 8, 10]

// Filter even numbers
const evens = numbers.filter(num => num % 2 === 0);
console.log(evens); // Output: [2, 4]
```

### ⚡ Arrow Function Characteristics

1. **No `this` binding** - Inherits `this` from parent scope
2. **Cannot be used as constructors**
3. **No `arguments` object**
4. **More concise syntax**

```javascript
// Traditional function
function traditional() {
    console.log(arguments); // Works
}

// Arrow function
const arrow = () => {
    console.log(arguments); // ❌ Error: arguments is not defined
};
```

---

## Parameters and Arguments

### Default Parameters

```javascript
function greet(name = "Guest") {
    return `Hello, ${name}!`;
}

console.log(greet());          // Output: Hello, Guest!
console.log(greet("Sarah"));   // Output: Hello, Sarah!
```

### Rest Parameters

Collect multiple arguments into an array.

```javascript
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}

console.log(sum(1, 2, 3));        // Output: 6
console.log(sum(10, 20, 30, 40)); // Output: 100
```

### Example: Calculate Average
```javascript
function calculateAverage(...scores) {
    if (scores.length === 0) return 0;
    const total = scores.reduce((sum, score) => sum + score, 0);
    return total / scores.length;
}

console.log(calculateAverage(80, 90, 85, 95)); // Output: 87.5
```

### Destructuring Parameters

```javascript
// Object destructuring
function displayUser({ name, age, city }) {
    console.log(`${name} is ${age} years old and lives in ${city}`);
}

const user = { name: "Emma", age: 25, city: "New York" };
displayUser(user); // Output: Emma is 25 years old and lives in New York

// Array destructuring
function getFirstTwo([first, second]) {
    return { first, second };
}

console.log(getFirstTwo([10, 20, 30])); // Output: { first: 10, second: 20 }
```

---

## Return Statement

The `return` statement ends function execution and specifies a value to return.

### Examples

#### Single Return
```javascript
function isEven(num) {
    return num % 2 === 0;
}

console.log(isEven(4));  // Output: true
console.log(isEven(7));  // Output: false
```

#### Multiple Return Paths
```javascript
function getGrade(score) {
    if (score >= 90) return "A";
    if (score >= 80) return "B";
    if (score >= 70) return "C";
    if (score >= 60) return "D";
    return "F";
}

console.log(getGrade(85)); // Output: B
console.log(getGrade(55)); // Output: F
```

#### Returning Objects
```javascript
function createUser(name, email) {
    return {
        name: name,
        email: email,
        createdAt: new Date()
    };
}

const user = createUser("John", "john@example.com");
console.log(user);
// Output: { name: 'John', email: 'john@example.com', createdAt: ... }
```

#### Early Return Pattern
```javascript
function divide(a, b) {
    // Guard clause
    if (b === 0) {
        return "Cannot divide by zero";
    }
    
    return a / b;
}

console.log(divide(10, 2));  // Output: 5
console.log(divide(10, 0));  // Output: Cannot divide by zero
```

---

## Function Scope

Variables defined inside a function are **not accessible** outside it.

### Examples

#### Local Scope
```javascript
function calculate() {
    let result = 10 + 5;
    console.log(result); // Output: 15
}

calculate();
// console.log(result); // ❌ Error: result is not defined
```

#### Global vs Local
```javascript
let globalVar = "I'm global";

function testScope() {
    let localVar = "I'm local";
    console.log(globalVar); // ✅ Can access global
    console.log(localVar);  // ✅ Can access local
}

testScope();
console.log(globalVar); // ✅ Can access global
// console.log(localVar);  // ❌ Error: localVar is not defined
```

#### Nested Functions (Closure)
```javascript
function outer() {
    let outerVar = "I'm from outer";
    
    function inner() {
        let innerVar = "I'm from inner";
        console.log(outerVar); // ✅ Can access outer scope
        console.log(innerVar); // ✅ Can access own scope
    }
    
    inner();
    // console.log(innerVar); // ❌ Error: innerVar is not defined
}

outer();
```

---

## Callback Functions

A function passed as an argument to another function.

### Examples

#### Basic Callback
```javascript
function processUserInput(callback) {
    let name = "Alice";
    callback(name);
}

function greetUser(userName) {
    console.log(`Hello, ${userName}!`);
}

processUserInput(greetUser); // Output: Hello, Alice!
```

#### Anonymous Callback
```javascript
function calculate(a, b, operation) {
    return operation(a, b);
}

let result = calculate(5, 3, function(x, y) {
    return x + y;
});

console.log(result); // Output: 8
```

#### Arrow Function Callback
```javascript
const numbers = [1, 2, 3, 4, 5];

// Using forEach
numbers.forEach(num => console.log(num * 2));
// Output: 2, 4, 6, 8, 10

// Using map
const squared = numbers.map(num => num * num);
console.log(squared); // Output: [1, 4, 9, 16, 25]

// Using filter
const evens = numbers.filter(num => num % 2 === 0);
console.log(evens); // Output: [2, 4]
```

#### Real-World Example: Event Handling
```javascript
// Simulating event handling
function addEventListener(event, callback) {
    console.log(`Listening for ${event} event...`);
    // Simulate event trigger
    setTimeout(() => {
        callback();
    }, 1000);
}

addEventListener('click', () => {
    console.log('Button was clicked!');
});
```

---

## Higher-Order Functions

Functions that take other functions as arguments or return functions.

### Examples

#### Function Returning Function
```javascript
function createMultiplier(multiplier) {
    return function(number) {
        return number * multiplier;
    };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

console.log(double(5));  // Output: 10
console.log(triple(5));  // Output: 15
```

#### Function with Function Parameter
```javascript
function repeat(n, action) {
    for (let i = 0; i < n; i++) {
        action(i);
    }
}

repeat(3, index => {
    console.log(`Iteration ${index}`);
});
// Output:
// Iteration 0
// Iteration 1
// Iteration 2
```

#### Practical Example: Logger
```javascript
function createLogger(prefix) {
    return function(message) {
        console.log(`[${prefix}] ${message}`);
    };
}

const infoLog = createLogger('INFO');
const errorLog = createLogger('ERROR');

infoLog('Application started');   // Output: [INFO] Application started
errorLog('Something went wrong'); // Output: [ERROR] Something went wrong
```

---

## IIFE (Immediately Invoked Function Expression)

A function that runs as soon as it's defined.

### Syntax
```javascript
(function() {
    // Code here
})();

// Arrow function IIFE
(() => {
    // Code here
})();
```

### Examples

#### Basic IIFE
```javascript
(function() {
    console.log("This runs immediately!");
})();
// Output: This runs immediately!
```

#### IIFE with Parameters
```javascript
(function(name) {
    console.log(`Hello, ${name}!`);
})("World");
// Output: Hello, World!
```

#### IIFE for Private Variables
```javascript
const counter = (function() {
    let count = 0; // Private variable
    
    return {
        increment: function() {
            count++;
            return count;
        },
        decrement: function() {
            count--;
            return count;
        },
        getCount: function() {
            return count;
        }
    };
})();

console.log(counter.increment()); // Output: 1
console.log(counter.increment()); // Output: 2
console.log(counter.getCount());  // Output: 2
// console.log(count); // ❌ Error: count is not defined (private)
```

---

## Best Practices

### ✅ Do's

1. **Use Descriptive Names**
```javascript
// ❌ Bad
function fn(x, y) {
    return x + y;
}

// ✅ Good
function calculateTotal(price, tax) {
    return price + tax;
}
```

2. **Keep Functions Small and Focused**
```javascript
// ✅ Good - Single responsibility
function validateEmail(email) {
    return email.includes('@');
}

function sendEmail(email, message) {
    if (!validateEmail(email)) {
        return "Invalid email";
    }
    // Send email logic
}
```

3. **Use Default Parameters**
```javascript
// ✅ Good
function greet(name = "Guest") {
    return `Hello, ${name}!`;
}
```

4. **Use Arrow Functions for Short Operations**
```javascript
// ✅ Good
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(n => n * 2);
```

### ❌ Don'ts

1. **Don't Modify Global Variables**
```javascript
// ❌ Bad
let total = 0;
function addToTotal(value) {
    total += value; // Modifying global
}

// ✅ Good
function addToTotal(total, value) {
    return total + value; // Pure function
}
```

2. **Don't Use Too Many Parameters**
```javascript
// ❌ Bad
function createUser(name, age, email, phone, address, city, zip) {
    // Too many parameters
}

// ✅ Good
function createUser(userDetails) {
    const { name, age, email, phone, address, city, zip } = userDetails;
}
```

---

## Practice Exercises

### Exercise 1: Temperature Converter
Create a function that converts Celsius to Fahrenheit.

```javascript
function celsiusToFahrenheit(celsius) {
    // Your code here
    // Formula: (C × 9/5) + 32
}

// Test
console.log(celsiusToFahrenheit(0));   // Should output: 32
console.log(celsiusToFahrenheit(100)); // Should output: 212
```

### Exercise 2: Array Filter
Create a function that filters numbers greater than a given value.

```javascript
function filterGreaterThan(numbers, threshold) {
    // Your code here
}

// Test
console.log(filterGreaterThan([10, 20, 30, 40], 25)); 
// Should output: [30, 40]
```

### Exercise 3: String Reverser
Create a function that reverses a string.

```javascript
function reverseString(str) {
    // Your code here
}

// Test
console.log(reverseString("hello")); // Should output: "olleh"
```

### Exercise 4: Find Maximum
Create a function using rest parameters to find the maximum number.

```javascript
function findMax(...numbers) {
    // Your code here
}

// Test
console.log(findMax(5, 12, 3, 19, 7)); // Should output: 19
```

### Exercise 5: Counter with Closure
Create a counter function that increments and returns the count.

```javascript
function createCounter() {
    // Your code here (use closure)
}

// Test
const counter = createCounter();
console.log(counter()); // Should output: 1
console.log(counter()); // Should output: 2
console.log(counter()); // Should output: 3
```

### Exercise 6: Array Mapper
Create a higher-order function that applies a transformation to each array element.

```javascript
function mapArray(array, transformFn) {
    // Your code here
}

// Test
const numbers = [1, 2, 3, 4];
const doubled = mapArray(numbers, num => num * 2);
console.log(doubled); // Should output: [2, 4, 6, 8]
```

### Exercise 7: Palindrome Checker
Create a function that checks if a string is a palindrome.

```javascript
function isPalindrome(str) {
    // Your code here
    // Ignore spaces and case
}

// Test
console.log(isPalindrome("racecar")); // Should output: true
console.log(isPalindrome("hello"));   // Should output: false
```

### Exercise 8: Calculator with Callbacks
Create a calculator that uses callbacks for operations.

```javascript
function calculator(num1, num2, operation) {
    // Your code here
}

// Test
console.log(calculator(10, 5, (a, b) => a + b));  // Should output: 15
console.log(calculator(10, 5, (a, b) => a - b));  // Should output: 5
console.log(calculator(10, 5, (a, b) => a * b));  // Should output: 50
```

---

## 🎯 Challenge Project

### Build a Task Manager

Create a simple task manager with the following functions:

```javascript
// Task Manager
const taskManager = (function() {
    let tasks = [];
    let nextId = 1;
    
    return {
        // Add a new task
        addTask: function(description) {
            // Your code here
        },
        
        // Remove task by ID
        removeTask: function(id) {
            // Your code here
        },
        
        // Mark task as complete
        completeTask: function(id) {
            // Your code here
        },
        
        // Get all tasks
        getAllTasks: function() {
            // Your code here
        },
        
        // Get completed tasks
        getCompletedTasks: function() {
            // Your code here
        }
    };
})();

// Test your task manager
taskManager.addTask("Learn JavaScript Functions");
taskManager.addTask("Practice Coding");
console.log(taskManager.getAllTasks());
```

---

## 📚 Summary

| Type | Syntax | Hoisted | Use Case |
|------|--------|---------|----------|
| **Declaration** | `function name() {}` | ✅ Yes | General purpose functions |
| **Expression** | `const name = function() {}` | ❌ No | Storing functions in variables |
| **Arrow** | `const name = () => {}` | ❌ No | Short functions, callbacks |
| **IIFE** | `(function() {})()` | N/A | Immediate execution, privacy |

### Key Takeaways

✅ Functions make code reusable and organized  
✅ Use arrow functions for short, simple operations  
✅ Callbacks enable flexible, dynamic behavior  
✅ Higher-order functions are powerful for abstraction  
✅ Keep functions small and focused (single responsibility)  
✅ Use descriptive names and default parameters  

---

🎉 **Congratulations!** You now have a solid understanding of JavaScript functions. Practice with the exercises and build the challenge project to reinforce your knowledge!
