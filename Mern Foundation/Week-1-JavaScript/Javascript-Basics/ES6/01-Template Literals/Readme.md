# Template Literals - Complete Guide

## 📚 Table of Contents

- [What are Template Literals?](#what-are-template-literals)
- [Basic Syntax](#basic-syntax)
- [String Interpolation](#string-interpolation)
- [Multi-line Strings](#multi-line-strings)
- [Expressions in Template Literals](#expressions-in-template-literals)
- [Practical Examples](#practical-examples)
- [Best Practices](#best-practices)
- [Practice Exercises](#practice-exercises)

---

## What are Template Literals?

**Template literals** are a modern way to create strings in JavaScript (introduced in ES6). They provide a cleaner, more powerful syntax for working with strings compared to traditional string concatenation.

### 🎯 Key Features

✅ **String interpolation** - Embed variables and expressions directly  
✅ **Multi-line strings** - No need for `\n` or string concatenation  
✅ **Expression evaluation** - Perform calculations inside strings  

### 💡 Analogy

**Old way (concatenation):** Like taping separate pieces of paper together with glue.  
**New way (template literals):** Like filling in a clean, pre-formatted form with blanks.

---

## Basic Syntax

Template literals use **backticks** (`` ` ``) instead of quotes (`'` or `"`).

### Syntax

```javascript
// Regular string (old way)
let regularString = "Hello, World!";

// Template literal (new way)
let templateLiteral = `Hello, World!`;
```

### Key Difference

```javascript
// Single quotes
let str1 = 'This is a string';

// Double quotes
let str2 = "This is a string";

// Backticks (template literal)
let str3 = `This is a template literal`;
```

---

## String Interpolation

Embed variables and expressions using `${...}` placeholder syntax.

### Old Way vs New Way

```javascript
console.log("--- STRING INTERPOLATION ---");

let username = "Mohammed";
let item = "laptop";

// ❌ OLD WAY: Concatenation with + operator
let oldMessage = "Hello, " + username + ", your order for a " + item + " is ready.";
console.log("OLD:", oldMessage);
// Output: Hello, Mohammed, your order for a laptop is ready.

// ✅ NEW WAY: Template literal interpolation
let newMessage = `Hello, ${username}, your order for a ${item} is ready.`;
console.log("NEW:", newMessage);
// Output: Hello, Mohammed, your order for a laptop is ready.
```

### Multiple Variables

```javascript
let firstName = "Sarah";
let lastName = "Johnson";
let age = 28;
let city = "New York";

// Old way (messy)
let bio1 = "My name is " + firstName + " " + lastName + ". I am " + age + " years old and I live in " + city + ".";

// New way (clean)
let bio2 = `My name is ${firstName} ${lastName}. I am ${age} years old and I live in ${city}.`;

console.log(bio2);
// Output: My name is Sarah Johnson. I am 28 years old and I live in New York.
```

### Numbers and Other Types

```javascript
let price = 99.99;
let quantity = 3;
let productName = "Wireless Mouse";

let orderSummary = `You ordered ${quantity} x ${productName} at $${price} each.`;
console.log(orderSummary);
// Output: You ordered 3 x Wireless Mouse at $99.99 each.
```

---

## Multi-line Strings

Template literals make creating multi-line strings incredibly easy.

### Old Way vs New Way

```javascript
// ❌ OLD WAY: Using \n for line breaks
let oldPoem = "Roses are red,\nViolets are blue,\nJavaScript is awesome,\nAnd so are you!";
console.log(oldPoem);

// ❌ OLD WAY: Using concatenation
let oldEmail = "Dear Customer,\n\n" +
               "Thank you for your order.\n" +
               "Your package will arrive soon.\n\n" +
               "Best regards,\n" +
               "The Team";
console.log(oldEmail);

// ✅ NEW WAY: Natural multi-line strings
let newPoem = `Roses are red,
Violets are blue,
JavaScript is awesome,
And so are you!`;
console.log(newPoem);

let newEmail = `Dear Customer,

Thank you for your order.
Your package will arrive soon.

Best regards,
The Team`;
console.log(newEmail);
```

### HTML Templates

Perfect for creating HTML strings:

```javascript
let productName = "Smart Watch";
let productPrice = 199.99;
let productImage = "watch.jpg";

let htmlCard = `
  <div class="product-card">
    <img src="${productImage}" alt="${productName}">
    <h2>${productName}</h2>
    <p class="price">$${productPrice}</p>
    <button>Add to Cart</button>
  </div>
`;

console.log(htmlCard);
```

### Code Snippets

```javascript
let language = "JavaScript";
let code = `
function greet(name) {
  return \`Hello, \${name}!\`;
}

console.log(greet("${language}"));
`;

console.log(code);
```

---

## Expressions in Template Literals

You can evaluate any JavaScript expression inside `${...}`.

### Mathematical Operations

```javascript
let num1 = 10;
let num2 = 5;

console.log(`${num1} + ${num2} = ${num1 + num2}`);
// Output: 10 + 5 = 15

console.log(`${num1} * ${num2} = ${num1 * num2}`);
// Output: 10 * 5 = 50

let price = 100;
let discount = 20;
console.log(`Final price: $${price - discount}`);
// Output: Final price: $80
```

### Function Calls

```javascript
function getDiscount(price, percent) {
  return price * (percent / 100);
}

let itemPrice = 200;
let discountPercent = 15;

console.log(`Original price: $${itemPrice}`);
console.log(`Discount: $${getDiscount(itemPrice, discountPercent)}`);
console.log(`Final price: $${itemPrice - getDiscount(itemPrice, discountPercent)}`);
// Output:
// Original price: $200
// Discount: $30
// Final price: $170
```

### Conditional (Ternary) Operator

```javascript
let score = 85;
let result = `You ${score >= 60 ? 'passed' : 'failed'} the exam!`;
console.log(result);
// Output: You passed the exam!

let age = 17;
let status = `You are ${age >= 18 ? 'an adult' : 'a minor'}.`;
console.log(status);
// Output: You are a minor.
```

### Array Methods

```javascript
let numbers = [1, 2, 3, 4, 5];
console.log(`Sum: ${numbers.reduce((sum, n) => sum + n, 0)}`);
// Output: Sum: 15

let names = ["Alice", "Bob", "Charlie"];
console.log(`Names: ${names.join(", ")}`);
// Output: Names: Alice, Bob, Charlie
```

### Object Properties

```javascript
let user = {
  name: "Emma",
  age: 25,
  email: "emma@example.com"
};

console.log(`User: ${user.name} (${user.email})`);
// Output: User: Emma (emma@example.com)

let product = {
  name: "Laptop",
  price: 999,
  inStock: true
};

console.log(`${product.name} - $${product.price} - ${product.inStock ? 'Available' : 'Out of Stock'}`);
// Output: Laptop - $999 - Available
```

---

## Practical Examples

Real-world use cases for template literals.

### Example 1: User Greeting

```javascript
function greetUser(name, time) {
  let greeting;
  
  if (time < 12) {
    greeting = `Good morning, ${name}! ☀️`;
  } else if (time < 18) {
    greeting = `Good afternoon, ${name}! 🌤️`;
  } else {
    greeting = `Good evening, ${name}! 🌙`;
  }
  
  return greeting;
}

console.log(greetUser("Sarah", 10));  // Output: Good morning, Sarah! ☀️
console.log(greetUser("John", 14));   // Output: Good afternoon, John! 🌤️
console.log(greetUser("Emma", 20));   // Output: Good evening, Emma! 🌙
```

### Example 2: Shopping Cart Summary

```javascript
function generateCartSummary(cart) {
  let subtotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
  let tax = subtotal * 0.1;
  let total = subtotal + tax;
  
  let summary = `
=== SHOPPING CART ===

${cart.map(item => `${item.name} x${item.quantity} - $${(item.price * item.quantity).toFixed(2)}`).join('\n')}

--------------------
Subtotal: $${subtotal.toFixed(2)}
Tax (10%): $${tax.toFixed(2)}
Total: $${total.toFixed(2)}
  `;
  
  return summary;
}

let cart = [
  { name: "Laptop", price: 999, quantity: 1 },
  { name: "Mouse", price: 25, quantity: 2 },
  { name: "Keyboard", price: 75, quantity: 1 }
];

console.log(generateCartSummary(cart));
// Output:
// === SHOPPING CART ===
//
// Laptop x1 - $999.00
// Mouse x2 - $50.00
// Keyboard x1 - $75.00
//
// --------------------
// Subtotal: $1124.00
// Tax (10%): $112.40
// Total: $1236.40
```

### Example 3: Welcome Message

```javascript
function createWelcomeMessage(user) {
  return `
Hello ${user.firstName} ${user.lastName}!

Welcome to our platform. Here are your account details:

Email: ${user.email}
Username: ${user.username}
Joined: ${user.joinDate}

Thank you for signing up!
  `.trim();
}

let newUser = {
  firstName: "Alice",
  lastName: "Johnson",
  email: "alice@example.com",
  username: "alice_j",
  joinDate: "2025-11-17"
};

console.log(createWelcomeMessage(newUser));
// Output:
// Hello Alice Johnson!
//
// Welcome to our platform. Here are your account details:
//
// Email: alice@example.com
// Username: alice_j
// Joined: 2025-11-17
//
// Thank you for signing up!
```

### Example 4: Progress Bar

```javascript
function createProgressBar(progress, total = 100) {
  let percentage = (progress / total) * 100;
  let filled = Math.floor(percentage / 5);
  let empty = 20 - filled;
  let bar = '='.repeat(filled) + '-'.repeat(empty);
  
  return `Progress: [${bar}] ${percentage.toFixed(0)}% (${progress}/${total})`;
}

console.log(createProgressBar(25, 100));
// Output: Progress: [=====--------------] 25% (25/100)

console.log(createProgressBar(75, 100));
// Output: Progress: [===============-----] 75% (75/100)

console.log(createProgressBar(100, 100));
// Output: Progress: [====================] 100% (100/100)
```

---

## Best Practices

### ✅ Do's

1. **Use Template Literals for String Interpolation**

```javascript
// ✅ Good
let name = "Alice";
let message = `Hello, ${name}!`;

// ❌ Avoid
let message2 = "Hello, " + name + "!";
```

2. **Keep Expressions Simple and Readable**

```javascript
// ✅ Good
let total = price + tax;
let message = `Total: $${total}`;

// ❌ Avoid (too complex)
let message2 = `Total: $${((price * 1.1) + (price * 0.05) - discount) * quantity}`;
```

3. **Use for Dynamic HTML Content**

```javascript
// ✅ Good
let items = ['Apple', 'Banana', 'Orange'];
let list = `<ul>${items.map(item => `<li>${item}</li>`).join('')}</ul>`;
```

### ❌ Don'ts

1. **Don't Use When Not Needed**

```javascript
// ❌ Unnecessary
let message = `Hello`;

// ✅ Better
let message = "Hello";
```

2. **Don't Put Complex Logic Inside Templates**

```javascript
// ❌ Bad
let result = `Total: ${users.filter(u => u.active).reduce((sum, u) => sum + u.orders.reduce((s, o) => s + o.price, 0), 0)}`;

// ✅ Good
let activeUsers = users.filter(u => u.active);
let total = activeUsers.reduce((sum, u) => {
  return sum + u.orders.reduce((s, o) => s + o.price, 0);
}, 0);
let result = `Total: ${total}`;
```

---

## Practice Exercises

### Exercise 1: Personal Introduction

Create a function that generates a personal introduction using template literals.

```javascript
function introduce(firstName, lastName, age, profession, city) {
  // Your code here
}

// Test
console.log(introduce("John", "Doe", 30, "Software Engineer", "San Francisco"));
// Expected: "Hello! I'm John Doe, a 30-year-old Software Engineer from San Francisco."
```

### Exercise 2: Product Details

Create a product detail string with pricing and availability.

```javascript
function productDetails(name, price, inStock, quantity) {
  // Your code here
  // Include: product name, price, stock status, and quantity if in stock
}

// Test
console.log(productDetails("Wireless Headphones", 89.99, true, 15));
console.log(productDetails("Smart Watch", 199.99, false, 0));
```

### Exercise 3: Table Generator

Generate a multiplication table using template literals.

```javascript
function multiplicationTable(number, rows = 10) {
  // Your code here
  // Format: "5 x 1 = 5"
}

// Test
console.log(multiplicationTable(5, 5));
```

### Exercise 4: Email Validator Message

Create a message for email validation results.

```javascript
function emailValidationMessage(email, isValid, errors = []) {
  // Your code here
  // Show email, status, and list errors if any
}

// Test
console.log(emailValidationMessage("test@example.com", true));
console.log(emailValidationMessage("invalid-email", false, ["Missing @", "Invalid domain"]));
```

### Exercise 5: Recipe Card

Generate a recipe card with ingredients and instructions.

```javascript
function recipeCard(recipe) {
  // recipe object: { name, servings, prepTime, ingredients[], instructions[] }
  // Your code here
}

// Test
let recipe = {
  name: "Chocolate Chip Cookies",
  servings: 24,
  prepTime: 30,
  ingredients: ["2 cups flour", "1 cup butter", "1 cup sugar", "2 eggs", "2 cups chocolate chips"],
  instructions: ["Mix dry ingredients", "Cream butter and sugar", "Combine and bake at 350°F"]
};

console.log(recipeCard(recipe));
```

### Exercise 6: Weather Report

Create a weather report string with current conditions.

```javascript
function weatherReport(city, temp, condition, humidity, wind) {
  // Your code here
  // Include emoji based on condition (☀️ sunny, ☁️ cloudy, 🌧️ rainy)
}

// Test
console.log(weatherReport("New York", 72, "sunny", 60, 10));
console.log(weatherReport("Seattle", 55, "rainy", 85, 15));
```

### Exercise 7: Invoice Generator

Create a simple invoice with items and total.

```javascript
function generateInvoice(invoiceNumber, date, items) {
  // items: [{ name, quantity, price }]
  // Your code here
  // Calculate subtotal, tax (8%), and total
}

// Test
let items = [
  { name: "Item 1", quantity: 2, price: 25.00 },
  { name: "Item 2", quantity: 1, price: 50.00 }
];
console.log(generateInvoice("INV-001", "2025-11-17", items));
```

### Exercise 8: Social Media Post

Generate a formatted social media post with hashtags.

```javascript
function createPost(author, content, hashtags, likes, comments) {
  // Your code here
  // Format hashtags with #, show engagement metrics
}

// Test
console.log(createPost(
  "Alice Johnson",
  "Just finished learning JavaScript template literals! 🎉",
  ["JavaScript", "Coding", "WebDev"],
  42,
  8
));
```

---

## 🎯 Challenge Project

### Build a Student Report Card Generator

Create a comprehensive report card system:

```javascript
function generateReportCard(student) {
  // student object structure:
  // {
  //   name: string,
  //   grade: string,
  //   subjects: [{ name, score, maxScore }],
  //   attendance: number (percentage),
  //   comments: string
  // }
  
  // Your implementation here
  
  // Requirements:
  // 1. Display student name and grade
  // 2. List all subjects with scores and percentages
  // 3. Calculate overall average
  // 4. Show attendance percentage
  // 5. Include teacher comments
  // 6. Add pass/fail status (pass >= 60%)
  // 7. Format nicely with borders/lines
}

// Test data
let student = {
  name: "Emma Wilson",
  grade: "10th",
  subjects: [
    { name: "Mathematics", score: 85, maxScore: 100 },
    { name: "Science", score: 92, maxScore: 100 },
    { name: "English", score: 78, maxScore: 100 },
    { name: "History", score: 88, maxScore: 100 }
  ],
  attendance: 95,
  comments: "Excellent performance! Keep up the good work."
};

console.log(generateReportCard(student));
```

---

## 📚 Summary

### Comparison: Old vs New

| Feature | Old Way | Template Literal |
|---------|---------|------------------|
| **Syntax** | `"string"` or `'string'` | `` `string` `` |
| **Variables** | `"Hello " + name` | `` `Hello ${name}` `` |
| **Multi-line** | `"Line 1\nLine 2"` | `` `Line 1<br>Line 2` `` |
| **Expressions** | Not directly possible | `` `Sum: ${a + b}` `` |
| **Readability** | ⭐⭐ | ⭐⭐⭐⭐⭐ |

### Key Takeaways

✅ Use backticks (`` ` ``) instead of quotes  
✅ Embed variables with `${variable}`  
✅ Evaluate expressions with `${expression}`  
✅ Create multi-line strings naturally  
✅ Great for HTML templates and dynamic content  
✅ Tagged templates for advanced processing  
✅ More readable than concatenation  

---

🎉 **Congratulations!** You now understand template literals! Practice with the exercises to master this essential ES6 feature.

**Pro Tip:** Always prefer template literals over string concatenation for cleaner, more maintainable code! 🚀