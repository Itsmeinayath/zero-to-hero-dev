// This file about Function in JavaScript

// === Exercise 1: Basic Function ===

function SayHello(){
    console.log("Hello Welcome to our app!")
}

// Test
SayHello()
SayHello()

// === Exercise 2: Function with Parameters ===
// Parametres are values you can pass into functions to make them more dynamic
function GreetUser(username){
    console.log(`Welcome back, ${username}!`) // here we use backtick for string interpolation when using variables inside string ${}
}

GreetUser("Alice")
GreetUser("Bob")

// === Exercise 3: Function with Return Value ===

function addNumbers(num1, num2){
    let sum = num1 + num2
    // What is returned from the function 
    return sum
}

// Test
let result = addNumbers(5, 10)
console.log(`The sum is: ${result}`) // The sum is: 15


result = addNumbers(20, 30)
console.log(`The sum is: ${result}`) // The sum is: 50

// === Exercise 4: Arrow Function ===
const MultipleNumbers = (num1, num2) => {
    return num1 * num2
}
// Test
let product = MultipleNumbers(4, 5)
console.log(`The product is: ${product}`) // The product is: 20

product = MultipleNumbers(7, 8)
console.log(`The product is: ${product}`) // The product is: 56

// the difference between normal function and arrow function is the way they handle the "this" keyword, arrow functions do not have their own "this" context, they inherit it from the surrounding scope. Normal functions have their own "this" context based on how they are called.

// === Exercise 5: Function Expression ===
const divideNumbers = function(num1, num2){
    if(num2 === 0){
        return "Error: Division by zero"
    }
    return num1 / num2
}
// Test
let quotient = divideNumbers(20, 4)
console.log(`The quotient is: ${quotient}`) // The quotient is: 5