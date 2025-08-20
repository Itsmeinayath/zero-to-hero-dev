Day 1: JavaScript Basi
Goal: Learn JavaScript variables, functions, loops, and arrays, and apply them to add interactivity to a webpage.
Tasks:

Learn JavaScript Basics (1 hour):

Concepts: Variables (let, const, var), data types (strings, numbers, booleans), functions (declaration, expression), loops (for, while), and conditionals (if, switch).
Resources:

What is a variable? variable means the data gonna be changed.

Variables are containers for data. 
In JavaScript, you can declare a variable using let, const, or var. Here var variable is not generally used in modern JavaScript due to its function-scoping behavior, which can lead to unexpected results. 
For example:
```javascript
var name = "YourName";
var age = 25;
```
output
```
YourName
25
```
Here in the above example you can see that the var keyword allows you to declare variables that can be re-assigned later.Because of this var is not commonly used in modern JavaScript.

Here some examples of using let and const:

```javascript
let name = "YourName";
const age = 25;
```

What is let? Let is a block-scoped variable declaration. It means that the variable is only accessible within the block it is defined in. For example:
```javascript
if (true) {
  let blockScoped = "I'm only accessible within this block";
}
console.log(blockScoped); // ReferenceError: blockScoped is not defined
```

what is const? Const is a variable declaration that creates a read-only reference to a value. This means that once a variable is assigned with const, it cannot be reassigned. For example:
```javascript
const pi = 3.14;
pi = 3.14159; // TypeError: Assignment to constant variable.
```

-  Web Docs: [JavaScript Basics](https://javascript.info/variables)
You can use these variables in functions, loops, and conditionals to create dynamic and interactive web pages.

We have only two types of variables:
Let and Const. with help of these we can create different types of variables.

The data types in JavaScript:

What is Data type?
A data type is a classification that specifies which type of value a variable can hold. In JavaScript, there are several built-in data types, including:

1. String: A sequence of characters enclosed in quotes. For example:
```javascript
let greeting = "Hello, world!";
```
2. Number: A numeric value, which can be an integer or a floating-point number. For example:
```javascript
let age = 30;
```
3. Boolean: A logical value that can be either true or false. For example:
```javascript
let isStudent = true;
```
4. Undefined: A variable that has been declared but not assigned a value. For example:
```javascript
let uninitialized;
console.log(uninitialized); // Output: undefined
```
```javascript
let ch = "Hello";
console.log(ch); // Output: Hello
```



