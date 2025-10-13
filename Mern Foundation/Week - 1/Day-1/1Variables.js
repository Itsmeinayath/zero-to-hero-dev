// Here in this file we will learn about variables in JavaScript
// Variables are used to store data values
// In JavaScript, we use the let, or const keywords to declare variables

let name  = "John" // let is used to declare a variable whose value can be changed
console.log(name) // console.log() is used to print something on the console

const pi = 3.14 // const is used to declare a variable whose value cannot be changed
console.log(pi)

// We can also declare multiple variables in one line
let a = 10 , b = 20 , c = 30
console.log(a, b, c)

// We can also declare variables without initializing them
let age
console.log(age) // undefined

age = 25 // now we are initializing the variable
console.log(age) // 25

// We can also declare variables with different data types
let isStudent = true // boolean
let grade = 'A' // string
let marks = 95.5 // number
console.log(isStudent, grade, marks)
// JavaScript is a dynamically typed language, so we can change the data type of a variable
let data = 100 // number
console.log(data) // 100
data = "Hello" // string
console.log(data) // Hello
data = false // boolean
console.log(data) // false
// types of variables in JavaScript are: number, string, boolean, object, undefined, null, symbol
// You can use the typeof operator to check the type of a variable
console.log(typeof name) // string
console.log(typeof pi) // number
console.log(typeof isStudent) // boolean
console.log(typeof age) // number
console.log(typeof data) // boolean


// Explation of variable types
// Number: Used to represent both integer and floating-point numbers. Example: 42, 3.14
// String: Used to represent text. Strings are enclosed in single or double quotes. Example: 'Hello', "World"
// Boolean: Represents a logical entity and can have two values: true or false. Example: true, false
// Object: Used to store collections of data and more complex entities. Example: {name: 'John', age: 30}
// Undefined: A variable that has been declared but not assigned a value. Example: let x; console.log(x); // undefined
// Null: Represents the intentional absence of any object value. Example: let y = null; console.log(y); // null
// Symbol: A unique and immutable primitive value, often used to identify object properties. Example: let sym = Symbol('description');

// This is how we can use variables in JavaScript
// Practice using variables and see how they work
// Happy coding!
