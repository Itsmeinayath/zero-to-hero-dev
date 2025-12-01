// High order and Callback Functions
// A function that takes another function as an argument or returns a function as a return value is called a higher-order function.

// Example of a higher-order function that takes a callback function as an argument

function add(a,b){
    return a + b;
}
console.log(add(2,3)); // 5



function operateOnNumbers(num1, num2, cb){
    let result = num1 + num2;
    cb(result);
}

operateOnNumbers(5, 10, function(result){
    console.log("The result is: " + result);
}); // The result is: 15

// we can also use arrow function as callback

operateOnNumbers(7, 3, (result) => {
    console.log("The result using arrow function is: " + result);
}); // The result using arrow function is: 10

// Example of a higher-order function that returns a function

// real world example
function makeMultiplier(multiplier){
    return function(x){
        return x * multiplier;
    }
}

const double = makeMultiplier(2);
console.log(double(5)); // 10

const triple = makeMultiplier(3);
console.log(triple(5)); // 15   


// a function returing another function
function greet(message){
    return function(name){
        console.log(message + ', ' + name + '!');
    }
}

const sayHello = greet('Hello');
sayHello('Alice'); // Hello, Alice!