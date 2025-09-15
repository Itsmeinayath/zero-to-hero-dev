## Day 1 – JavaScript Fundamentals for Beginners (Zero to Hero)

Duration: ~4-5 hours  
Goal: Master JavaScript basics from scratch with real examples and build your first interactive webpage.

---
## What You'll Learn Today
By the end of this day, you'll understand:
1. **Variables** - How to store and manage data (like saving a user's name)
2. **Data Types** - Different kinds of information (text, numbers, true/false)
3. **Functions** - Reusable blocks of code (like a recipe you can follow multiple times)
4. **Control Flow** - Making decisions and repeating actions in code
5. **DOM Manipulation** - Making webpages interactive (responding to clicks, changing content)
6. **Event Handling** - Responding to user actions (clicks, typing, etc.)
7. **Building Your First Project** - A real interactive webpage you can show others

---
## Chapter 1: Variables - Your Data Storage Containers

### What are Variables?
Think of variables like labeled boxes where you store things. In real life, you might have a box labeled "Photos" to store your pictures. In programming, you create labeled containers to store information.

**Real-world analogy:** Your phone's contacts list
- Contact Name: "John" (this is like a variable name)
- Phone Number: "123-456-7890" (this is the value stored in that variable)

### The Three Ways to Create Variables

#### 1. `let` - For Things That Change
```javascript
let userAge = 25;
userAge = 26; // ✅ This works - you can change it
console.log(userAge); // Shows: 26
```

**Real Example:** Shopping cart items
```javascript
let cartItems = 2;
cartItems = cartItems + 1; // User adds another item
console.log(cartItems); // Now shows: 3
```

#### 2. `const` - For Things That Stay the Same
```javascript
const websiteName = "My Awesome Site";
// websiteName = "Different Name"; // ❌ This would cause an error!
```

**Real Example:** Configuration settings
```javascript
const maxLoginAttempts = 3;
const companyEmail = "support@company.com";
const taxRate = 0.08; // 8% tax that doesn't change
```

#### 3. `var` - The Old Way (Avoid This!)
```javascript
var oldStyle = "Don't use this"; // ❌ Causes problems, use let/const instead
```

### Choosing Between let and const
**Simple Rule:** Use `const` by default. Only use `let` if you know the value will change.

```javascript
// User profile example
const username = "sarah123";     // Username doesn't change after signup
const birthYear = 1995;          // Birth year never changes
let currentScore = 0;            // Score changes as user plays game
let isLoggedIn = false;          // Login status changes
```

### Variable Naming Rules
1. **Must start with letter, $, or _**
   ```javascript
   let userName = "John";    // ✅ Good
   let _private = "secret";  // ✅ Good  
   let $element = "div";     // ✅ Good
   let 123invalid = "no";    // ❌ Can't start with number
   ```

2. **Use descriptive names**
   ```javascript
   let n = "John";           // ❌ What does 'n' mean?
   let userName = "John";    // ✅ Clear and descriptive
   let u = 25;               // ❌ Unclear
   let userAge = 25;         // ✅ Self-explaining
   ```

3. **Use camelCase**
   ```javascript
   let firstname = "John";        // ❌ Hard to read
   let first_name = "John";       // ❌ Not JavaScript style
   let firstName = "John";        // ✅ Perfect!
   let userAccountBalance = 1500; // ✅ Multiple words, easy to read
   ```

---
## Chapter 2: Data Types - Different Kinds of Information

Just like in real life, we deal with different types of information. Your age is a number, your name is text, and whether you're hungry is yes/no.

### 1. Strings - Text Information
Strings are for storing text. Always wrap them in quotes!

```javascript
const firstName = "Sarah";
const message = 'Hello there!';
const description = `This is a long description 
that spans multiple lines`;
```

**Real Examples:**
```javascript
const userEmail = "sarah@gmail.com";
const errorMessage = "Password must be at least 8 characters";
const welcomeText = "Welcome to our website!";
```

**String Operations:**
```javascript
const first = "Sarah";
const last = "Johnson";
const fullName = first + " " + last; // "Sarah Johnson"

// Modern way (template literals):
const greeting = `Hello, ${first}!`; // "Hello, Sarah!"
const age = 25;
const intro = `I am ${age} years old`; // "I am 25 years old"
```

### 2. Numbers - Mathematical Values
```javascript
const userAge = 25;
const price = 19.99;
const temperature = -5;
const huge = 1000000;
```

**Real Examples:**
```javascript
const productPrice = 49.99;
const quantity = 3;
const totalCost = productPrice * quantity; // 149.97

const currentYear = 2025;
const birthYear = 1995;
const age = currentYear - birthYear; // 30
```

### 3. Booleans - True or False
Perfect for yes/no questions, on/off states, or any either/or situation.

```javascript
const isLoggedIn = true;
const isEmailValid = false;
const hasPermission = true;
```

**Real Examples:**
```javascript
const isUserPremium = true;
const isPasswordStrong = false;
const isDarkModeOn = true;

// Using booleans in decisions:
if (isUserPremium) {
    console.log("Show premium features");
}
```

### 4. Arrays - Lists of Things
Arrays store multiple items in a specific order, like a shopping list.

```javascript
const shoppingList = ["milk", "bread", "eggs", "cheese"];
const scores = [85, 92, 78, 96];
const mixedArray = ["John", 25, true, "Engineer"];
```

**Real Examples:**
```javascript
const todoList = [
    "Buy groceries", 
    "Call dentist", 
    "Finish project"
];

const userRoles = ["admin", "editor", "viewer"];
const monthlyExpenses = [1200, 980, 1450, 890];

// Working with arrays:
console.log(todoList[0]); // "Buy groceries" (first item)
console.log(todoList.length); // 3 (how many items)

todoList.push("Walk the dog"); // Add new item
console.log(todoList); // Now has 4 items
```

### 5. Objects - Complex Information Containers
Objects store related information together, like a contact card with name, phone, email, etc.

```javascript
const user = {
    name: "Sarah Johnson",
    age: 28,
    email: "sarah@email.com",
    isActive: true
};
```

**Real Examples:**
```javascript
const product = {
    name: "Wireless Headphones",
    price: 89.99,
    brand: "TechCorp",
    inStock: true,
    colors: ["black", "white", "blue"]
};

const blogPost = {
    title: "Learning JavaScript",
    author: "John Doe",
    publishDate: "2025-01-15",
    likes: 47,
    tags: ["programming", "beginner", "tutorial"]
};

// Accessing object properties:
console.log(user.name); // "Sarah Johnson"
console.log(product.price); // 89.99

// Changing object properties:
user.age = 29;
product.inStock = false;
```

### Understanding Data Types
```javascript
// Check what type something is:
console.log(typeof "Hello"); // "string"
console.log(typeof 42); // "number"  
console.log(typeof true); // "boolean"
console.log(typeof []); // "object" (arrays are special objects)
console.log(typeof {}); // "object"
```

---
## Chapter 3: Operators - Working with Data

### Arithmetic Operators - Math Operations
Just like a calculator, JavaScript can do math for you!

```javascript
const price = 100;
const tax = 8;

console.log(price + tax);     // 108 (addition)
console.log(price - tax);     // 92  (subtraction)  
console.log(price * 2);       // 200 (multiplication)
console.log(price / 4);       // 25  (division)
console.log(price % 3);       // 1   (remainder/modulo)
console.log(2 ** 3);          // 8   (exponentiation - 2 to the power of 3)
```

**Real Examples:**
```javascript
// E-commerce calculations
const itemPrice = 29.99;
const quantity = 3;
const subtotal = itemPrice * quantity;        // 89.97
const taxRate = 0.08;
const taxAmount = subtotal * taxRate;         // 7.20
const total = subtotal + taxAmount;           // 97.17

// Age calculator
const currentYear = 2025;
const birthYear = 1995;
const age = currentYear - birthYear;          // 30

// Even/odd checker using modulo
const number = 17;
const isEven = number % 2 === 0;              // false (17 is odd)
```

### Comparison Operators - Comparing Values
Used to compare things and get true/false answers:

```javascript
const userAge = 25;
const requiredAge = 18;

console.log(userAge > requiredAge);    // true
console.log(userAge < requiredAge);    // false
console.log(userAge >= 25);            // true
console.log(userAge <= 20);            // false
console.log(userAge === 25);           // true (exactly equal)
console.log(userAge !== 30);           // true (not equal)
```

**Important:** Always use `===` (strict equality) instead of `==`:
```javascript
console.log(5 == "5");    // true  (converts string to number)
console.log(5 === "5");   // false (different types - number vs string)
console.log(0 == false);  // true  (both convert to false)
console.log(0 === false); // false (different types)
```

**Real Examples:**
```javascript
// Password validation
const password = "myPassword123";
const isLongEnough = password.length >= 8;        // true
const hasTooManyChars = password.length > 50;     // false

// User permissions
const userRole = "admin";
const isAdmin = userRole === "admin";             // true
const isNotGuest = userRole !== "guest";          // true

// Product inventory
const stockLevel = 5;
const lowStock = stockLevel <= 10;                // true
const outOfStock = stockLevel === 0;              // false
```

### Logical Operators - Combining Conditions

#### AND (&&) - Both conditions must be true
```javascript
const userAge = 25;
const hasLicense = true;

if (userAge >= 18 && hasLicense) {
    console.log("Can drive!"); // Both conditions are true
}
```

#### OR (||) - At least one condition must be true  
```javascript
const isWeekend = true;
const isHoliday = false;

if (isWeekend || isHoliday) {
    console.log("No work today!"); // One condition is true
}
```

#### NOT (!) - Flips true to false, false to true
```javascript
const isLoggedIn = false;

if (!isLoggedIn) {
    console.log("Please log in"); // !false becomes true
}
```

**Real Examples:**
```javascript
// User access control
const userAge = 22;
const isVerified = true;
const hasSubscription = true;

const canAccessPremium = userAge >= 18 && isVerified && hasSubscription;
console.log(canAccessPremium); // true

// Notification settings
const emailEnabled = false;
const smsEnabled = true;

const shouldNotify = emailEnabled || smsEnabled;
console.log(shouldNotify); // true (SMS is enabled)

// Form validation
const emailEmpty = true;
const passwordEmpty = false;

const formHasErrors = emailEmpty || passwordEmpty;
console.log(formHasErrors); // true (email is empty)
```

### Assignment Operators - Shortcuts for Math
Instead of writing `x = x + 5`, you can write `x += 5`:

```javascript
let score = 100;

score += 10;    // score = score + 10;  (now 110)
score -= 5;     // score = score - 5;   (now 105)  
score *= 2;     // score = score * 2;   (now 210)
score /= 3;     // score = score / 3;   (now 70)
score %= 7;     // score = score % 7;   (now 0)
```

**Real Examples:**
```javascript
// Shopping cart
let cartTotal = 50.00;
cartTotal += 25.99;  // Add new item
cartTotal -= 10.00;  // Apply discount
cartTotal *= 1.08;   // Add 8% tax

// Game scoring
let playerHealth = 100;
playerHealth -= 25;  // Take damage
playerHealth += 10;  // Health potion

// Counter example
let loginAttempts = 0;
loginAttempts += 1;  // Increment counter
---
## Chapter 4: Functions - Reusable Code Blocks

### What are Functions?
Think of functions like recipes. Once you write a recipe for making pancakes, you can use it over and over without rewriting all the steps each time.

**Real-world analogy:** A vending machine
- You put in money (input)
- Press a button (call the function)  
- Get a snack (output)

### Why Use Functions?
1. **Avoid repetition** - Write once, use many times
2. **Organization** - Keep related code together
3. **Testing** - Easy to test small pieces
4. **Collaboration** - Others can use your functions

### Function Declaration - The Traditional Way
```javascript
function greetUser(name) {
    return `Hello, ${name}! Welcome to our site.`;
}

// Using the function:
const message = greetUser("Sarah");
console.log(message); // "Hello, Sarah! Welcome to our site."
```

**Real Example:** Calculator function
```javascript
function calculateTotal(price, tax) {
    const taxAmount = price * tax;
    const total = price + taxAmount;
    return total;
}

const billTotal = calculateTotal(100, 0.08); // $100 with 8% tax
console.log(billTotal); // 108
```

### Function Expression - Storing Functions in Variables
```javascript
const calculateDiscount = function(price, discountPercent) {
    const discount = price * (discountPercent / 100);
    return price - discount;
};

const finalPrice = calculateDiscount(200, 20); // 20% off $200
console.log(finalPrice); // 160
```

### Arrow Functions - The Modern Shortcut
Perfect for short, simple functions:

```javascript
// Traditional function:
function double(number) {
    return number * 2;
}

// Arrow function version:
const double = (number) => {
    return number * 2;
};

// Even shorter (for one-line functions):
const double = number => number * 2;
```

**Real Examples:**
```javascript
// Email validator
const isValidEmail = email => email.includes('@') && email.includes('.');

// Age calculator
const calculateAge = birthYear => 2025 - birthYear;

// Price formatter
const formatPrice = price => `$${price.toFixed(2)}`;

console.log(isValidEmail("user@site.com")); // true
console.log(calculateAge(1995)); // 30
console.log(formatPrice(19.5)); // "$19.50"
```

### Parameters vs Arguments
- **Parameters** = placeholders in function definition
- **Arguments** = actual values you pass in

```javascript
function createProfile(name, age) {    // name & age are parameters
    return `${name} is ${age} years old`;
}

createProfile("John", 25);  // "John" & 25 are arguments
```

### Default Parameters
Give parameters default values in case none are provided:

```javascript
function greetUser(name = "Guest", timeOfDay = "day") {
    return `Good ${timeOfDay}, ${name}!`;
}

console.log(greetUser()); // "Good day, Guest!"
console.log(greetUser("Sarah")); // "Good day, Sarah!"
console.log(greetUser("Mike", "morning")); // "Good morning, Mike!"
```

**Real Example:** User registration
```javascript
function createUser(username, role = "user", isActive = true) {
    return {
        username: username,
        role: role,
        isActive: isActive,
        createdAt: new Date()
    };
}

const newUser = createUser("sarah123");
// Creates user with default role="user" and isActive=true
```

### Return Statement - Getting Results Back
Functions can send information back using `return`:

```javascript
function checkPassword(password) {
    if (password.length < 8) {
        return "Too short"; // Function stops here
    }
    if (!password.includes('@')) {
        return "Must include @";
    }
    return "Valid password"; // All checks passed
}

const result = checkPassword("abc123");
console.log(result); // "Too short"
```

**Important:** Once a function hits `return`, it stops running!

### Functions Without Return
Some functions do things but don't need to return values:

```javascript
function displayWelcomeMessage(userName) {
    console.log(`Welcome back, ${userName}!`);
    console.log("Here are your recent activities:");
    // No return statement = returns undefined
}

displayWelcomeMessage("Sarah");
// Shows messages in console, but function returns undefined
```

### Scope - Where Variables Live
Variables inside functions are private to that function:

```javascript
const globalMessage = "I'm global"; // Everyone can see this

function createGreeting() {
    const secretMessage = "I'm private"; // Only this function can see this
    return `${globalMessage} and ${secretMessage}`;
}

console.log(globalMessage); // ✅ Works
console.log(secretMessage); // ❌ Error! secretMessage doesn't exist here
console.log(createGreeting()); // ✅ "I'm global and I'm private"
```

**Real Example:** User authentication
```javascript
function authenticateUser(username, password) {
    const hashedPassword = hashPassword(password); // Private variable
    const isValid = checkDatabase(username, hashedPassword);
    
    if (isValid) {
        return { success: true, message: "Login successful" };
    } else {
        return { success: false, message: "Invalid credentials" };
    }
    
    // hashedPassword is destroyed when function ends
}
```

---
## Chapter 5: Control Flow - Making Decisions

### Conditional Statements - If This, Then That

Life is full of decisions: "If it's raining, take an umbrella." Programming works the same way!

### Basic If Statement
```javascript
const userAge = 17;

if (userAge >= 18) {
    console.log("You can vote!");
}
// Nothing happens if userAge is less than 18
```

### If-Else - Handle Both Cases
```javascript
const userAge = 17;

if (userAge >= 18) {
    console.log("You can vote!");
} else {
    console.log("You're too young to vote.");
}
```

**Real Example:** E-commerce discount
```javascript
const orderTotal = 150;

if (orderTotal >= 100) {
    console.log("Free shipping applied!");
} else {
    console.log("Add $" + (100 - orderTotal) + " more for free shipping");
}
```

### Multiple Conditions - If, Else If, Else
```javascript
const score = 85;

if (score >= 90) {
    console.log("Grade: A - Excellent!");
} else if (score >= 80) {
    console.log("Grade: B - Good job!");
} else if (score >= 70) {
    console.log("Grade: C - Average");
} else if (score >= 60) {
    console.log("Grade: D - Below average");
} else {
    console.log("Grade: F - Please study more");
}
```

**Real Example:** Weather app
```javascript
const temperature = 75;

if (temperature > 85) {
    console.log("It's hot! Stay hydrated.");
} else if (temperature > 70) {
    console.log("Perfect weather for a walk!");
} else if (temperature > 50) {
    console.log("A bit cool, bring a light jacket.");
} else {
    console.log("It's cold! Bundle up.");
}
```

### Switch Statements - Multiple Exact Matches
When you have many exact values to check, `switch` is cleaner than multiple `if-else`:

```javascript
const dayOfWeek = "monday";

switch (dayOfWeek) {
    case "monday":
        console.log("Start of work week");
        break;
    case "tuesday":
        console.log("Tuesday blues");
        break;
    case "wednesday":
        console.log("Hump day!");
        break;
    case "thursday":
        console.log("Almost there");
        break;
    case "friday":
        console.log("TGIF!");
        break;
    case "saturday":
    case "sunday":
        console.log("Weekend!");
        break;
    default:
        console.log("Not a valid day");
}
```

**Real Example:** User role permissions
```javascript
const userRole = "editor";

switch (userRole) {
    case "admin":
        console.log("Full access to everything");
        break;
    case "editor":
        console.log("Can edit and publish content");
        break;
    case "viewer":
        console.log("Can only view content");
        break;
    case "guest":
        console.log("Limited access");
        break;
    default:
        console.log("Unknown role - contact admin");
}
```

**Important:** Don't forget `break;` or the code will "fall through" to the next case!

---
## Chapter 6: Loops - Repeating Actions

### What are Loops?
Instead of writing the same code over and over, loops let you repeat actions automatically.

**Real-world analogy:** Washing dishes
- While there are dirty dishes, keep washing
- For each dish in the sink, wash it
- Repeat until done

### For Loop - When You Know How Many Times
Perfect when you know exactly how many times to repeat:

```javascript
// Count from 1 to 5
for (let i = 1; i <= 5; i++) {
    console.log(`Count: ${i}`);
}
// Output: Count: 1, Count: 2, Count: 3, Count: 4, Count: 5
```

**Breaking it down:**
- `let i = 1` - Start at 1
- `i <= 5` - Keep going while i is 5 or less  
- `i++` - Add 1 to i after each round

**Real Examples:**
```javascript
// Send email to 10 users
for (let i = 1; i <= 10; i++) {
    console.log(`Sending email ${i} of 10`);
    // sendEmail() would go here
}

// Generate multiplication table
const number = 7;
for (let i = 1; i <= 10; i++) {
    console.log(`${number} × ${i} = ${number * i}`);
}
// 7 × 1 = 7, 7 × 2 = 14, etc.
```

### For...Of Loop - For Arrays and Lists
Best way to go through each item in a list:

```javascript
const fruits = ["apple", "banana", "orange", "grape"];

for (const fruit of fruits) {
    console.log(`I like ${fruit}s`);
}
// I like apples, I like bananas, etc.
```

**Real Examples:**
```javascript
// Process shopping cart items
const cartItems = [
    { name: "Laptop", price: 999 },
    { name: "Mouse", price: 25 },
    { name: "Keyboard", price: 75 }
];

let total = 0;
for (const item of cartItems) {
    console.log(`${item.name}: $${item.price}`);
    total += item.price;
}
console.log(`Total: $${total}`); // Total: $1099

// Validate multiple passwords
const passwords = ["123", "password123", "StrongP@ss1"];

for (const password of passwords) {
    if (password.length >= 8) {
        console.log(`${password}: Valid`);
    } else {
        console.log(`${password}: Too short`);
    }
}
```

### While Loop - Keep Going Until Something Changes
Continues as long as a condition is true:

```javascript
let countdown = 5;

while (countdown > 0) {
    console.log(`${countdown}...`);
    countdown--; // IMPORTANT: Change the condition or loop forever!
}
console.log("Blast off! 🚀");
```

**Real Examples:**
```javascript
// Keep asking for valid input
let userInput = "";

while (userInput !== "yes" && userInput !== "no") {
    userInput = prompt("Please enter 'yes' or 'no':");
}
console.log(`You entered: ${userInput}`);

// Process items until queue is empty
let tasksToProcess = ["email", "backup", "update"];

while (tasksToProcess.length > 0) {
    const currentTask = tasksToProcess.shift(); // Remove first item
    console.log(`Processing: ${currentTask}`);
}
console.log("All tasks complete!");
```

### Do...While Loop - Run At Least Once
Like `while`, but guarantees the code runs at least once:

```javascript
let attempts = 0;

do {
    attempts++;
    console.log(`Attempt ${attempts}`);
    // Try something here
} while (attempts < 3);
```

### Loop Control - Break and Continue

#### Break - Exit the loop early
```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

for (const num of numbers) {
    if (num === 6) {
        console.log("Found 6! Stopping here.");
        break; // Exit the loop completely
    }
    console.log(num);
}
// Output: 1, 2, 3, 4, 5, Found 6! Stopping here.
```

#### Continue - Skip to next iteration
```javascript
for (let i = 1; i <= 10; i++) {
    if (i % 2 === 0) {
        continue; // Skip even numbers
    }
    console.log(i); // Only odd numbers
}
// Output: 1, 3, 5, 7, 9
```

**Real Example:** Form validation
```javascript
const formData = ["john@email.com", "", "jane@email.com", "invalid-email", "bob@email.com"];

for (const email of formData) {
    if (email === "") {
        continue; // Skip empty emails
    }
    
    if (!email.includes("@")) {
        console.log(`Invalid email: ${email}`);
        break; // Stop processing if we find invalid format
    }
    
    console.log(`Valid email: ${email}`);
}
```

---
## Chapter 10: Complete Beginner Project - Interactive Profile Card

Let's build a complete project that uses everything we've learned! We'll create an interactive profile card that demonstrates variables, functions, control flow, arrays, objects, and DOM manipulation.

### Project Overview
We'll build a personal profile card where users can:
- Update their name and bio
- Add skills to a list
- Toggle between light and dark themes
- See a simple calculator

### HTML Structure (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Interactive Profile</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <div class="profile-card">
            <!-- Header Section -->
            <header class="card-header">
                <h1 id="profileName">Your Name</h1>
                <button id="themeToggle" class="theme-btn">🌙</button>
            </header>

            <!-- Profile Info Section -->
            <section class="profile-info">
                <div class="form-group">
                    <input type="text" id="nameInput" placeholder="Enter your name">
                    <button id="updateName">Update Name</button>
                </div>
                
                <div class="form-group">
                    <textarea id="bioInput" placeholder="Tell us about yourself..."></textarea>
                    <button id="updateBio">Update Bio</button>
                </div>
                
                <p id="profileBio">Welcome! Click 'Update Bio' to personalize your profile.</p>
            </section>

            <!-- Skills Section -->
            <section class="skills-section">
                <h3>My Skills</h3>
                <div class="form-group">
                    <input type="text" id="skillInput" placeholder="Add a skill">
                    <button id="addSkill">Add Skill</button>
                </div>
                <ul id="skillsList"></ul>
            </section>

            <!-- Calculator Section -->
            <section class="calculator-section">
                <h3>Quick Calculator</h3>
                <div class="calc-inputs">
                    <input type="number" id="num1" placeholder="Number 1">
                    <select id="operation">
                        <option value="add">+</option>
                        <option value="subtract">-</option>
                        <option value="multiply">×</option>
                        <option value="divide">÷</option>
                    </select>
                    <input type="number" id="num2" placeholder="Number 2">
                    <button id="calculate">Calculate</button>
                </div>
                <div id="calcResult" class="result"></div>
            </section>

            <!-- Activity Log -->
            <section class="log-section">
                <h3>Activity Log</h3>
                <div id="activityLog" class="log-container"></div>
                <button id="clearLog">Clear Log</button>
            </section>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### CSS Styling (style.css)
```css
/* Reset and base styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding: 20px;
    transition: all 0.3s ease;
}

.container {
    max-width: 600px;
    margin: 0 auto;
}

.profile-card {
    background: white;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    transition: all 0.3s ease;
}

/* Header */
.card-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.theme-btn {
    background: rgba(255, 255, 255, 0.2);
    border: none;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    font-size: 20px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.theme-btn:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: scale(1.1);
}

/* Sections */
section {
    padding: 25px 30px;
    border-bottom: 1px solid #f0f0f0;
}

section:last-child {
    border-bottom: none;
}

h3 {
    color: #333;
    margin-bottom: 15px;
    font-size: 1.2em;
}

/* Form elements */
.form-group {
    display: flex;
    gap: 10px;
    margin-bottom: 15px;
    flex-wrap: wrap;
}

input, textarea, select {
    padding: 12px;
    border: 2px solid #e1e1e1;
    border-radius: 8px;
    font-size: 14px;
    transition: border-color 0.3s ease;
    flex: 1;
    min-width: 150px;
}

input:focus, textarea:focus, select:focus {
    outline: none;
    border-color: #667eea;
}

textarea {
    resize: vertical;
    min-height: 80px;
}

button {
    background: #667eea;
    color: white;
    border: none;
    padding: 12px 20px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 600;
    transition: all 0.3s ease;
}

button:hover {
    background: #5a6fd8;
    transform: translateY(-2px);
}

button:active {
    transform: translateY(0);
}

/* Skills list */
#skillsList {
    list-style: none;
}

.skill-item {
    background: #f8f9ff;
    padding: 10px 15px;
    margin: 8px 0;
    border-radius: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-left: 4px solid #667eea;
}

.skill-item button {
    background: #ff6b6b;
    padding: 5px 10px;
    font-size: 12px;
    border-radius: 12px;
}

.skill-item button:hover {
    background: #ff5252;
}

/* Calculator */
.calc-inputs {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    align-items: center;
}

.calc-inputs input, .calc-inputs select {
    flex: 1;
    min-width: 80px;
}

.result {
    margin-top: 15px;
    padding: 15px;
    background: #f8f9ff;
    border-radius: 8px;
    font-weight: 600;
    font-size: 16px;
    border-left: 4px solid #667eea;
    min-height: 20px;
}

/* Activity log */
.log-container {
    background: #f8f9ff;
    border-radius: 8px;
    padding: 15px;
    max-height: 200px;
    overflow-y: auto;
    border: 1px solid #e1e1e1;
    margin-bottom: 15px;
}

.log-item {
    padding: 8px 0;
    border-bottom: 1px solid #eee;
    font-size: 14px;
    color: #666;
}

.log-item:last-child {
    border-bottom: none;
}

/* Dark theme */
body.dark {
    background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
}

.dark .profile-card {
    background: #2c3e50;
    color: #ecf0f1;
}

.dark .card-header {
    background: linear-gradient(135deg, #34495e 0%, #2c3e50 100%);
}

.dark h3 {
    color: #ecf0f1;
}

.dark input, .dark textarea, .dark select {
    background: #34495e;
    border-color: #4a5f7a;
    color: #ecf0f1;
}

.dark .skill-item, .dark .result, .dark .log-container {
    background: #34495e;
    border-color: #4a5f7a;
}

.dark section {
    border-color: #4a5f7a;
}
```

### JavaScript Functionality (script.js)
```javascript
// DOM element references
const profileName = document.getElementById('profileName');
const nameInput = document.getElementById('nameInput');
const updateNameBtn = document.getElementById('updateName');
const bioInput = document.getElementById('bioInput');
const updateBioBtn = document.getElementById('updateBio');
const profileBio = document.getElementById('profileBio');
const skillInput = document.getElementById('skillInput');
const addSkillBtn = document.getElementById('addSkill');
const skillsList = document.getElementById('skillsList');
const themeToggle = document.getElementById('themeToggle');
const num1 = document.getElementById('num1');
const num2 = document.getElementById('num2');
const operation = document.getElementById('operation');
const calculateBtn = document.getElementById('calculate');
const calcResult = document.getElementById('calcResult');
const activityLog = document.getElementById('activityLog');
const clearLogBtn = document.getElementById('clearLog');

// Application state
let isDarkTheme = false;
const skills = [];

// Utility functions
function logActivity(message) {
    const timestamp = new Date().toLocaleTimeString();
    const logItem = document.createElement('div');
    logItem.className = 'log-item';
    logItem.textContent = `${timestamp}: ${message}`;
    activityLog.appendChild(logItem);
    activityLog.scrollTop = activityLog.scrollHeight; // Auto scroll to bottom
}

function validateInput(input, fieldName) {
    const value = input.value.trim();
    if (value === '') {
        alert(`Please enter ${fieldName}`);
        return false;
    }
    return true;
}

// Name update functionality
function updateName() {
    if (!validateInput(nameInput, 'your name')) return;
    
    const newName = nameInput.value.trim();
    profileName.textContent = newName;
    nameInput.value = '';
    logActivity(`Name updated to "${newName}"`);
}

// Bio update functionality
function updateBio() {
    if (!validateInput(bioInput, 'your bio')) return;
    
    const newBio = bioInput.value.trim();
    profileBio.textContent = newBio;
    bioInput.value = '';
    logActivity('Bio updated successfully');
}

// Skills management
function addSkill() {
    if (!validateInput(skillInput, 'a skill')) return;
    
    const skillName = skillInput.value.trim();
    
    // Check if skill already exists
    if (skills.includes(skillName.toLowerCase())) {
        alert('This skill is already added!');
        return;
    }
    
    // Add to skills array
    skills.push(skillName.toLowerCase());
    
    // Create skill element
    const skillItem = document.createElement('li');
    skillItem.className = 'skill-item';
    skillItem.innerHTML = `
        <span>${skillName}</span>
        <button onclick="removeSkill('${skillName.toLowerCase()}', this)">Remove</button>
    `;
    
    skillsList.appendChild(skillItem);
    skillInput.value = '';
    logActivity(`Added skill: "${skillName}"`);
}

function removeSkill(skillName, buttonElement) {
    // Remove from array
    const index = skills.indexOf(skillName);
    if (index > -1) {
        skills.splice(index, 1);
    }
    
    // Remove from DOM
    buttonElement.parentElement.remove();
    logActivity(`Removed skill: "${skillName}"`);
}

// Theme toggle functionality
function toggleTheme() {
    isDarkTheme = !isDarkTheme;
    document.body.classList.toggle('dark', isDarkTheme);
    themeToggle.textContent = isDarkTheme ? '☀️' : '🌙';
    logActivity(`Switched to ${isDarkTheme ? 'dark' : 'light'} theme`);
}

// Calculator functionality
function calculate() {
    const number1 = parseFloat(num1.value);
    const number2 = parseFloat(num2.value);
    const op = operation.value;
    
    // Validate inputs
    if (isNaN(number1) || isNaN(number2)) {
        calcResult.textContent = 'Please enter valid numbers';
        calcResult.style.color = '#ff6b6b';
        return;
    }
    
    let result;
    let operationSymbol;
    
    switch (op) {
        case 'add':
            result = number1 + number2;
            operationSymbol = '+';
            break;
        case 'subtract':
            result = number1 - number2;
            operationSymbol = '-';
            break;
        case 'multiply':
            result = number1 * number2;
            operationSymbol = '×';
            break;
        case 'divide':
            if (number2 === 0) {
                calcResult.textContent = 'Cannot divide by zero!';
                calcResult.style.color = '#ff6b6b';
                return;
            }
            result = number1 / number2;
            operationSymbol = '÷';
            break;
        default:
            calcResult.textContent = 'Invalid operation';
            calcResult.style.color = '#ff6b6b';
            return;
    }
    
    calcResult.textContent = `${number1} ${operationSymbol} ${number2} = ${result}`;
    calcResult.style.color = '#667eea';
    logActivity(`Calculated: ${number1} ${operationSymbol} ${number2} = ${result}`);
}

// Clear activity log
function clearLog() {
    activityLog.innerHTML = '';
    logActivity('Activity log cleared');
}

// Event listeners
updateNameBtn.addEventListener('click', updateName);
updateBioBtn.addEventListener('click', updateBio);
addSkillBtn.addEventListener('click', addSkill);
themeToggle.addEventListener('click', toggleTheme);
calculateBtn.addEventListener('click', calculate);
clearLogBtn.addEventListener('click', clearLog);

// Allow Enter key to trigger actions
nameInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') updateName();
});

bioInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        updateBio();
    }
});

skillInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') addSkill();
});

// Calculator inputs - Enter to calculate
num1.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') calculate();
});

num2.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') calculate();
});

// Initialize app
logActivity('Profile app initialized successfully! 🎉');
```

### How the Project Works

This project demonstrates all the JavaScript fundamentals we've covered:

#### 1. **Variables and Data Types**
```javascript
let isDarkTheme = false;    // Boolean
const skills = [];          // Array
const skillName = "JavaScript"; // String
```

#### 2. **Functions**
- `updateName()` - Updates the profile name
- `validateInput()` - Checks if input is valid
- `logActivity()` - Adds messages to activity log

#### 3. **Control Flow**
```javascript
// If-else statements
if (!validateInput(nameInput, 'your name')) return;

// Switch statement in calculator
switch (op) {
    case 'add':
        result = number1 + number2;
        break;
    // ... more cases
}
```

#### 4. **Arrays and Objects**
```javascript
// Array operations
skills.push(skillName);        // Add skill
skills.includes(skillName);    // Check if exists
skills.splice(index, 1);       // Remove skill
```

#### 5. **DOM Manipulation**
```javascript
// Selecting elements
const profileName = document.getElementById('profileName');

// Changing content
profileName.textContent = newName;

// Creating new elements
const skillItem = document.createElement('li');

// Event listeners
updateNameBtn.addEventListener('click', updateName);
```

#### 6. **Event Handling**
- Click events for buttons
- Keypress events for Enter key shortcuts
- Form validation and user feedback

### Key Features Explained

1. **Profile Updates**: Users can change their name and bio with validation
2. **Skills Management**: Add/remove skills with duplicate checking
3. **Theme Toggle**: Switch between light and dark modes
4. **Calculator**: Perform basic math with error handling
5. **Activity Log**: Track all user actions with timestamps
6. **Keyboard Shortcuts**: Enter key works for quick actions

This project shows how all the concepts work together to create a real, interactive web application!
  try { const res = await fetch('/api/user'); const data = await res.json(); return data; }
  catch(e){ console.error(e); }
}
```
Not core for Day 1, but sets mental model for future MERN API calls.

---
## 3. DOM Essentials
```html
<button id="helloBtn">Say Hi</button>
<p id="message"></p>
```
```javascript
const btn = document.getElementById('helloBtn');
const message = document.querySelector('#message');

btn.addEventListener('click', () => {
  const name = prompt('Your name?');
  if (!name) return;
  message.textContent = `Welcome, ${name}!`;
});
```
Key APIs: `querySelector`, `textContent`, `classList.add/remove/toggle`.

DOM vs HTMLCollection vs NodeList:
`querySelectorAll` returns static NodeList; `getElementsByClassName` returns live HTMLCollection. Prefer static to avoid unexpected reactivity while iterating.

Batch DOM Writes:
Accumulate string / fragment then insert once to reduce reflows.
```javascript
const frag = document.createDocumentFragment();
for(let i=0;i<100;i++){ const li=document.createElement('li'); li.textContent=i; frag.append(li);} 
list.append(frag);
```

Security Note:
Use `textContent` for user input. Only use `innerHTML` with trusted / sanitized content.

Accessibility Tip: Use semantic elements (`<main>`, `<nav>`, `<button>`) – React and server frameworks later rely on good structure.

---
## 4. Mini Console Drills (10–15 min)
Open DevTools Console and type each:
```javascript
let total = 0; for (let i = 1; i <= 5; i++) total += i; total; // 15
const temperatures = [22, 18, 25];
let max = temperatures[0];
for (const t of temperatures) if (t > max) max = t; max;
function greet(who='Dev'){ return `Hello ${who}`; } greet();
```
Focus: loops, conditionals, function return, string interpolation.

---
## 5. Project: Interactive Bio Card
Deliver a polished `index.html` + `script.js` with 3 features.

### 5.1 Structure
```
MERN Foundation/
  Day-1/
    index.html
    script.js
```

### 5.2 HTML (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Day 1 – Interactive Bio</title>
  <style>
    body { font-family: system-ui, sans-serif; margin:0; background:#f5f7fa; }
    .card { max-width:640px; margin:40px auto; background:#fff; padding:32px; border-radius:16px; box-shadow:0 4px 20px rgba(0,0,0,.08); }
    h1 { margin:0 0 8px; font-size:2rem; color:#334155; }
    p  { line-height:1.5; color:#475569; }
    .actions { margin-top:24px; display:flex; flex-wrap:wrap; gap:12px; }
    button { cursor:pointer; border:none; padding:12px 20px; border-radius:8px; font-size:14px; font-weight:600; background:#6366f1; color:#fff; transition:.2s; }
    button:hover { background:#4f46e5; transform:translateY(-2px); }
    #log { margin-top:24px; background:#f1f5f9; padding:16px; border-radius:8px; font-family:monospace; max-height:180px; overflow:auto; }
    .badge { display:inline-block; background:#e0e7ff; color:#4338ca; padding:2px 8px; border-radius:999px; font-size:12px; margin-left:8px; }
  </style>
</head>
<body>
  <div class="card">
    <h1>My Bio <span class="badge" id="modeBadge">JS</span></h1>
    <p id="bioText">Hi, I'm learning modern JavaScript. Click a button below to interact.</p>
    <div class="actions">
      <button id="greetBtn">Personal Greeting</button>
      <button id="calcBtn">Quick Calculator</button>
      <button id="loopBtn">Loop Demo</button>
      <button id="themeBtn">Toggle Theme</button>
    </div>
    <div id="log" aria-live="polite"></div>
  </div>
  <script src="script.js" defer></script>
</body>
</html>
```

### 5.3 JavaScript (script.js)
```javascript
// Utility logger
function appendLog(msg) {
  const log = document.getElementById('log');
  const line = document.createElement('div');
  line.textContent = msg;
  log.appendChild(line);
}

function personalGreeting() {
  const name = prompt("What's your name?");
  if (!name || !name.trim()) { appendLog('No valid name provided'); return; }
  document.getElementById('bioText').textContent = `Welcome, ${name.trim()}! Keep building.`;
  appendLog(`Greeting set for ${name.trim()}`);
}

function quickCalculator() {
  const a = Number(prompt('First number?'));
  const b = Number(prompt('Second number?'));
  if (Number.isNaN(a) || Number.isNaN(b)) { appendLog('Invalid number(s)'); return; }
  appendLog(`${a} + ${b} = ${a + b}`);
  appendLog(`${a} * ${b} = ${a * b}`);
}

function loopDemo() {
  for (let i = 1; i <= 5; i++) appendLog(`Loop i=${i} square=${i*i}`);
}

function toggleTheme() {
  const badge = document.getElementById('modeBadge');
  const dark = document.body.classList.toggle('dark');
  if (dark) {
    document.body.style.background = '#0f172a';
    document.querySelector('.card').style.background = '#1e293b';
    document.querySelector('.card').style.color = '#e2e8f0';
    badge.textContent = 'Dark';
  } else {
    document.body.style.background = '#f5f7fa';
    document.querySelector('.card').style.background = '#fff';
    document.querySelector('.card').style.color = '#475569';
    badge.textContent = 'JS';
  }
  appendLog('Theme toggled');
}

// Wire events after DOM parse (defer attribute ensures script runs after HTML)
document.getElementById('greetBtn').addEventListener('click', personalGreeting);
document.getElementById('calcBtn').addEventListener('click', quickCalculator);
document.getElementById('loopBtn').addEventListener('click', loopDemo);
document.getElementById('themeBtn').addEventListener('click', toggleTheme);

appendLog('App initialized ✅');
```
Enhancements Explanation:
- `appendLog` isolates UI side-effect: easier to replace logging mechanism.
- Input validation prevents empty or NaN operations.
- Theme toggle: toggles a CSS state (simple manual style changes now; later move styles to classes).
- Defer script ensures DOM available (alternative: place script before closing body).

### 5.4 Feature Checklist
- Greeting modifies content
- Calculator handles invalid input gracefully
- Loop demonstrates iteration output
- Theme toggle visually switches modes
- Log keeps chronological feedback

Stretch Ideas:
- Persist user name with `localStorage`
- Clear log button
- Replace prompts with an input form

---
## 6. Debugging & DevTools Quick Wins
| Goal | Tool | Tip |
|------|------|-----|
| Inspect element | Elements panel | Check computed styles |
| Watch values | Console `console.log()` | Log before & after change |
| Profile code (later) | Performance tab | For slow loops / rendering |
| Clear console | `clear()` | Keep output readable |

Common mistakes:
1. Script tag missing / wrong path → 404 (check Network tab)
2. Using `innerHTML` when only text needed → prefer `textContent`
3. Forgetting `defer` leading to null DOM references

---
## 7. Common Pitfalls & Best Practices
| Pitfall | Fix |
|---------|-----|
| Accidental globals | Always use `const` / `let` |
| Bloated functions | Split into small utilities (e.g., `appendLog`) |
| Repeated selectors | Cache element references if reused frequently |
| Magic numbers | Extract to constants if reused (LOOP_LIMIT = 5) |
| Blocking prompts overused | Replace later with proper UI inputs |

Naming: verbs for functions (`toggleTheme`), nouns for data (`skills`).

---
## 8. Quick Reference Cheat Sheet
```
let / const        Block-scoped variable declarations
=== / !==          Strict comparison (avoid ==)
querySelector()    Select first matching DOM element
addEventListener() Attach event handler
textContent        Safe text update
template literal   `Hello ${name}`
Array.push(x)      Append item (mutates)
for..of            Iterate values of array
```

---
## 9. Exercises (Optional Reinforcement)
Basic:
1. Add a button that clears the log
2. Add a counter that increments every time greeting is used
Intermediate:
3. Add input field + button replacing prompt for name
4. Store last 5 calculations in an array and display them
Stretch:
5. Add light/dark preference persistence via `localStorage`
6. Animate card entrance using CSS transitions

---
## 10. Additional Practice Ideas
1. Build a simple counter with increment/decrement + reset (no prompts).  
2. Create a function that returns an object summary (`{min, max, average}`) from an array.  
3. Refactor calculator to support subtract/divide via menu prompt.  
4. Add form element for greeting instead of prompt; prevent default submit.

---
## 11. Reflection Prompts
1. Which concept felt least intuitive (scope, event loop, functions)?  
2. One improvement to code organization you can apply tomorrow?  
3. Summarize JS execution model in 2 sentences.
---
## 12 For better understanding do practice on solve javascript problems on all the topics covered in day 1.
practice at least 10 problems on each topic covered in day 1.

End of extended Day 1 foundational guide.

