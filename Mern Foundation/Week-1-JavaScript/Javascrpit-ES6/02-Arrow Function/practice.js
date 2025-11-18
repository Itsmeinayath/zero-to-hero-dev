// This file is abour arrow functions in ES6

console.log("=== Arrow Function Examples ===");

// The traditional function expression

function add(num1, num2) {
  return num1 + num2;
}
console.log("Traditional Function:", add(2, 3)); // 5

// Arrow function equivalent

const addArrow = (num1, num2) => {
    return num1 + num2;
}

console.log("Arrow Function:", addArrow(2, 3)); // 5

const subtractArrow = (num1, num2) => num1 - num2;
console.log("Arrow Function (Concise):", subtractArrow(5, 2)); // 3