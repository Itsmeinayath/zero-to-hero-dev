console.log("------1. template literals------");

let userName = "Alice";
let item = "laptop";

// old way

let oldMessage = "Hello, " + userName + ", your " + item + " is ready for pickup.";
console.log(oldMessage);

// new way with template literals

let newMessage = `Hello, ${userName}, your ${item} is ready for pickup.`;
console.log(newMessage);