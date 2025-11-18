
# Destructuring - Complete Guide

## 📚 Table of Contents

- [What is Destructuring?](#what-is-destructuring)
- [Object Destructuring](#object-destructuring)
- [Array Destructuring](#array-destructuring)
- [Default Values](#default-values)
- [Renaming Variables](#renaming-variables)
- [Nested Destructuring](#nested-destructuring)
- [Function Parameters](#function-parameters)
- [Practical Examples](#practical-examples)
- [Best Practices](#best-practices)
- [Practice Exercises](#practice-exercises)

---

## What is Destructuring?

**Destructuring** is a shortcut to extract (unpack) values from objects and arrays and assign them to variables in a single line.

### 💡 Analogy

Imagine an object is a **gift box** with labeled items inside:

```javascript
const user = { name: "Ali", age: 30 };
```

- **Old way:** Taking items out one by one
- **Destructuring:** Saying "I want the name and age from the user box" and they magically pop into variables!

### 🎯 Key Benefits

✅ **Cleaner code** - Less repetitive typing  
✅ **More readable** - Clear what values you're extracting  
✅ **Flexible** - Set defaults, rename, skip values  
✅ **Works with functions** - Great for function parameters  

---

## Object Destructuring

Extract properties from objects into variables.

### Basic Object Destructuring

```javascript
// OLD WAY: Accessing properties one by one
const user = { name: "Ali", age: 30, city: "Dubai" };

const name = user.name;
const age = user.age;
const city = user.city;

console.log(name); // Output: Ali
console.log(age);  // Output: 30

// NEW WAY: Destructuring
const user = { name: "Ali", age: 30, city: "Dubai" };

const { name, age, city } = user;

console.log(name); // Output: Ali
console.log(age);  // Output: 30
console.log(city); // Output: Dubai
```

### Extract Specific Properties

You don't have to extract all properties:

```javascript
const person = { 
  firstName: "John", 
  lastName: "Doe", 
  age: 25, 
  email: "john@example.com" 
};

// Only extract what you need
const { firstName, email } = person;

console.log(firstName); // Output: John
console.log(email);     // Output: john@example.com
```

### Order Doesn't Matter

Unlike arrays, object property order doesn't matter:

```javascript
const product = { name: "Laptop", price: 1000, brand: "Dell" };

// These are the same:
const { name, price, brand } = product;
const { price, name, brand } = product;
const { brand, price, name } = product;

console.log(name);  // Output: Laptop
console.log(price); // Output: 1000
console.log(brand); // Output: Dell
```

---

## Array Destructuring

Extract values from arrays based on position.

### Basic Array Destructuring

```javascript
// OLD WAY: Accessing array elements by index
const colors = ["red", "green", "blue"];

const first = colors[0];
const second = colors[1];
const third = colors[2];

console.log(first);  // Output: red
console.log(second); // Output: green

// NEW WAY: Destructuring
const colors = ["red", "green", "blue"];

const [first, second, third] = colors;

console.log(first);  // Output: red
console.log(second); // Output: green
console.log(third);  // Output: blue
```

### Skip Values

Use commas to skip array elements:

```javascript
const numbers = [1, 2, 3, 4, 5];

// Skip the second and fourth values
const [first, , third, , fifth] = numbers;

console.log(first); // Output: 1
console.log(third); // Output: 3
console.log(fifth); // Output: 5
```

### Rest Operator with Arrays

Collect remaining elements:

```javascript
const fruits = ["apple", "banana", "orange", "grape", "mango"];

const [first, second, ...rest] = fruits;

console.log(first);  // Output: apple
console.log(second); // Output: banana
console.log(rest);   // Output: ['orange', 'grape', 'mango']
```

### Swapping Variables

Easy variable swap without temporary variable:

```javascript
let a = 10;
let b = 20;

// OLD WAY: Need temporary variable
let temp = a;
a = b;
b = temp;

// NEW WAY: Destructuring swap
let a = 10;
let b = 20;

[a, b] = [b, a];

console.log(a); // Output: 20
console.log(b); // Output: 10
```

---

## Default Values

Set fallback values if property/element doesn't exist.

### Default Values with Objects

```javascript
const user = { name: "Alice" };

// Without defaults
const { name, age } = user;
console.log(age); // Output: undefined

// With defaults
const { name, age = 25, city = "Unknown" } = user;
console.log(name); // Output: Alice
console.log(age);  // Output: 25 (default)
console.log(city); // Output: Unknown (default)
```

### Default Values with Arrays

```javascript
const colors = ["red"];

const [first, second = "blue", third = "green"] = colors;

console.log(first);  // Output: red
console.log(second); // Output: blue (default)
console.log(third);  // Output: green (default)
```

### Default Values in Practice

```javascript
const settings = {
  theme: "dark",
  fontSize: 16
};

const { 
  theme = "light", 
  fontSize = 14, 
  language = "en",
  notifications = true 
} = settings;

console.log(theme);         // Output: dark (from object)
console.log(fontSize);      // Output: 16 (from object)
console.log(language);      // Output: en (default)
console.log(notifications); // Output: true (default)
```

---

## Renaming Variables

Assign extracted values to different variable names.

### Rename Object Properties

```javascript
const user = { name: "Bob", age: 30 };

// Syntax: { originalName: newName }
const { name: userName, age: userAge } = user;

console.log(userName); // Output: Bob
console.log(userAge);  // Output: 30

// Note: 'name' and 'age' variables don't exist
// console.log(name); // Error: name is not defined
```

### Rename with Defaults

```javascript
const product = { title: "Phone", price: 500 };

const { 
  title: productName = "Unknown", 
  price: productPrice = 0,
  stock: available = 0 
} = product;

console.log(productName);  // Output: Phone
console.log(productPrice); // Output: 500
console.log(available);    // Output: 0 (default)
```

### Practical Renaming Example

```javascript
// API response with confusing names
const apiResponse = {
  usr_nm: "Alice",
  usr_id: 123,
  usr_eml: "alice@example.com"
};

// Rename to readable variables
const {
  usr_nm: userName,
  usr_id: userId,
  usr_eml: email
} = apiResponse;

console.log(userName); // Output: Alice
console.log(userId);   // Output: 123
console.log(email);    // Output: alice@example.com
```

---

## Nested Destructuring

Extract values from nested objects and arrays.

### Nested Objects

```javascript
const user = {
  name: "John",
  age: 30,
  address: {
    street: "123 Main St",
    city: "New York",
    country: "USA"
  }
};

// Extract nested properties
const { 
  name, 
  address: { city, country } 
} = user;

console.log(name);    // Output: John
console.log(city);    // Output: New York
console.log(country); // Output: USA

// Note: 'address' variable is not created
// console.log(address); // Error: address is not defined
```

### Extract Both Parent and Nested

```javascript
const user = {
  name: "Jane",
  contact: {
    email: "jane@example.com",
    phone: "555-1234"
  }
};

// Get both contact object and its properties
const { 
  name, 
  contact,
  contact: { email, phone } 
} = user;

console.log(name);    // Output: Jane
console.log(contact); // Output: { email: '...', phone: '...' }
console.log(email);   // Output: jane@example.com
console.log(phone);   // Output: 555-1234
```

### Nested Arrays

```javascript
const data = [1, [2, 3], 4];

const [first, [second, third], fourth] = data;

console.log(first);  // Output: 1
console.log(second); // Output: 2
console.log(third);  // Output: 3
console.log(fourth); // Output: 4
```

### Complex Nested Example

```javascript
const company = {
  name: "Tech Corp",
  employees: [
    { name: "Alice", role: "Developer" },
    { name: "Bob", role: "Designer" }
  ],
  location: {
    city: "San Francisco",
    coordinates: { lat: 37.7749, lng: -122.4194 }
  }
};

const {
  name: companyName,
  employees: [firstEmployee, secondEmployee],
  location: { city, coordinates: { lat, lng } }
} = company;

console.log(companyName);    // Output: Tech Corp
console.log(firstEmployee);  // Output: { name: 'Alice', role: 'Developer' }
console.log(city);           // Output: San Francisco
console.log(lat, lng);       // Output: 37.7749 -122.4194
```

---

## Function Parameters

Destructuring is powerful with function parameters.

### Object Parameters

```javascript
// OLD WAY: Accessing object properties
function greetUser(user) {
  console.log(`Hello, ${user.name}! You are ${user.age} years old.`);
}

greetUser({ name: "Alice", age: 25 });

// NEW WAY: Destructure in parameters
function greetUser({ name, age }) {
  console.log(`Hello, ${name}! You are ${age} years old.`);
}

greetUser({ name: "Alice", age: 25 });
// Output: Hello, Alice! You are 25 years old.
```

### Default Values in Parameters

```javascript
function createUser({ name, age = 18, role = "User" }) {
  console.log(`${name}, ${age}, ${role}`);
}

createUser({ name: "Bob" });
// Output: Bob, 18, User

createUser({ name: "Alice", age: 25, role: "Admin" });
// Output: Alice, 25, Admin
```

### Array Parameters

```javascript
function displayColors([first, second, third = "yellow"]) {
  console.log(`Primary: ${first}, Secondary: ${second}, Tertiary: ${third}`);
}

displayColors(["red", "blue"]);
// Output: Primary: red, Secondary: blue, Tertiary: yellow
```

### Real-World Function Example

```javascript
function renderProduct({ 
  name, 
  price, 
  description = "No description", 
  inStock = true 
}) {
  return `
    Product: ${name}
    Price: $${price}
    Description: ${description}
    Status: ${inStock ? "In Stock" : "Out of Stock"}
  `;
}

console.log(renderProduct({ 
  name: "Laptop", 
  price: 1000 
}));
// Output:
// Product: Laptop
// Price: $1000
// Description: No description
// Status: In Stock
```

---

## Practical Examples

### Example 1: User Profile

```javascript
const userProfile = {
  id: 101,
  username: "johndoe",
  email: "john@example.com",
  settings: {
    theme: "dark",
    notifications: true,
    privacy: {
      showEmail: false,
      showPhone: true
    }
  }
};

// Extract multiple levels
const {
  username,
  email,
  settings: {
    theme,
    privacy: { showEmail }
  }
} = userProfile;

console.log(`User: ${username}`);
console.log(`Email: ${email}`);
console.log(`Theme: ${theme}`);
console.log(`Show Email: ${showEmail}`);
```

### Example 2: API Response Handling

```javascript
function handleAPIResponse(response) {
  const {
    data: { user, posts = [] },
    status = 200,
    message = "Success"
  } = response;
  
  console.log(`Status: ${status} - ${message}`);
  console.log(`User: ${user.name}`);
  console.log(`Posts: ${posts.length}`);
}

handleAPIResponse({
  data: {
    user: { name: "Alice", id: 1 },
    posts: [{ id: 1, title: "Hello" }, { id: 2, title: "World" }]
  },
  status: 200
});
```

### Example 3: Configuration Merging

```javascript
function createConfig(userConfig) {
  const defaultConfig = {
    theme: "light",
    language: "en",
    notifications: true,
    autoSave: false
  };
  
  // Destructure with defaults
  const {
    theme = defaultConfig.theme,
    language = defaultConfig.language,
    notifications = defaultConfig.notifications,
    autoSave = defaultConfig.autoSave
  } = userConfig;
  
  return { theme, language, notifications, autoSave };
}

const config = createConfig({ theme: "dark", autoSave: true });
console.log(config);
// Output: { theme: 'dark', language: 'en', notifications: true, autoSave: true }
```

### Example 4: Coordinate Calculations

```javascript
function calculateDistance([x1, y1], [x2, y2]) {
  const dx = x2 - x1;
  const dy = y2 - y1;
  return Math.sqrt(dx * dx + dy * dy);
}

const pointA = [0, 0];
const pointB = [3, 4];

console.log(calculateDistance(pointA, pointB));
// Output: 5
```

---

## Best Practices

### ✅ Do's

**1. Use Descriptive Names**

```javascript
// ✅ Good
const { firstName, lastName, email } = user;

// ❌ Avoid single letters
const { f, l, e } = user;
```

**2. Set Defaults for Optional Properties**

```javascript
// ✅ Good
const { name, age = 18, role = "User" } = userData;

// ❌ Could be undefined
const { name, age, role } = userData;
```

**3. Keep Destructuring Simple**

```javascript
// ✅ Good - easy to read
const { name, email } = user;
const { city, street } = user.address;

// ❌ Too complex - hard to read
const {
  name,
  address: {
    city,
    street,
    coordinates: { lat, lng }
  },
  contacts: [primary, ...others]
} = user;
```

**4. Use in Function Parameters**

```javascript
// ✅ Good - clear what function expects
function createPost({ title, content, author }) {
  // Function body
}

// ❌ Less clear
function createPost(data) {
  const title = data.title;
  const content = data.content;
  // ...
}
```

### ❌ Don'ts

**1. Don't Over-Destructure**

```javascript
// ❌ Overkill for simple access
const { id } = user;
console.log(id);

// ✅ Better for single property
console.log(user.id);
```

**2. Don't Destructure in Loops Unnecessarily**

```javascript
const users = [{ name: "Alice" }, { name: "Bob" }];

// ❌ Slower
users.forEach(({ name }) => console.log(name));

// ✅ Better for performance
users.forEach(user => console.log(user.name));
```

---

## Practice Exercises

### Exercise 1: Basic Object Destructuring

Extract properties from this object:

```javascript
const book = {
  title: "JavaScript Guide",
  author: "John Doe",
  year: 2024,
  pages: 500
};

// Extract title, author, and pages using destructuring
// Your code here
```

### Exercise 2: Array Destructuring

Extract values from this array:

```javascript
const scores = [95, 87, 92, 78, 88];

// Extract first, second, and last score
// Your code here
// Hint: Use rest operator for last
```

### Exercise 3: Default Values

Create a function that uses defaults:

```javascript
// Create a function displayProduct that takes an object
// with name, price (default: 0), inStock (default: true)
// Your code here

// Test
displayProduct({ name: "Laptop", price: 1000 });
displayProduct({ name: "Mouse" });
```

### Exercise 4: Renaming

Rename these properties to more readable names:

```javascript
const data = {
  u_n: "alice123",
  u_e: "alice@example.com",
  u_a: 25
};

// Rename to: username, email, age
// Your code here
```

### Exercise 5: Nested Destructuring

Extract nested values:

```javascript
const student = {
  name: "Emma",
  scores: {
    math: 95,
    science: 88,
    english: 92
  },
  contact: {
    email: "emma@example.com",
    phone: "555-1234"
  }
};

// Extract: name, math score, science score, email
// Your code here
```

### Exercise 6: Function Parameters

Create a function that calculates total price:

```javascript
// Function should accept object with: price, quantity, tax (default: 0.1)
// Return total: price * quantity * (1 + tax)
function calculateTotal(/* Your destructuring here */) {
  // Your code here
}

// Test
console.log(calculateTotal({ price: 100, quantity: 2 }));
// Should output: 220

console.log(calculateTotal({ price: 100, quantity: 2, tax: 0.2 }));
// Should output: 240
```

### Exercise 7: Swapping

Swap these variables using destructuring:

```javascript
let player1Score = 100;
let player2Score = 150;

// Swap the values
// Your code here

console.log(player1Score); // Should be 150
console.log(player2Score); // Should be 100
```

### Exercise 8: Array Rest

Extract first two and collect rest:

```javascript
const cities = ["New York", "London", "Tokyo", "Paris", "Dubai", "Sydney"];

// Extract first two cities, collect rest in 'otherCities'
// Your code here

console.log(first);       // New York
console.log(second);      // London
console.log(otherCities); // ['Tokyo', 'Paris', 'Dubai', 'Sydney']
```

---

## 🎯 Challenge Project

### Build a User Management System

```javascript
// Sample data
const users = [
  {
    id: 1,
    profile: {
      firstName: "Alice",
      lastName: "Johnson",
      age: 28,
      contact: {
        email: "alice@example.com",
        phone: "555-0001"
      }
    },
    settings: {
      theme: "dark",
      notifications: true
    }
  },
  {
    id: 2,
    profile: {
      firstName: "Bob",
      lastName: "Smith",
      age: 35,
      contact: {
        email: "bob@example.com",
        phone: "555-0002"
      }
    }
    // Note: settings missing
  }
];

// 1. Create function to display user card
function displayUserCard(user) {
  // Use destructuring to extract:
  // - id
  // - firstName, lastName from profile
  // - email from contact
  // - theme from settings (default: "light")
  
  // Your code here
}

// 2. Create function to update user email
function updateEmail(user, newEmail) {
  // Extract and update email, return new user object
  // Your code here
}

// 3. Create function to get full names
function getFullNames(users) {
  // Use map and destructuring to return array of full names
  // Your code here
}

// 4. Create function to filter adult users
function getAdults(users) {
  // Filter users age >= 18
  // Your code here
}

// Test your functions
users.forEach(displayUserCard);
console.log(getFullNames(users));
```

---

## 📚 Summary

### Key Concepts

| Type | Syntax | Example |
|------|--------|---------|
| **Object** | `const { a, b } = obj` | `const { name, age } = user` |
| **Array** | `const [a, b] = arr` | `const [first, second] = colors` |
| **Default** | `const { a = 10 } = obj` | `const { age = 18 } = user` |
| **Rename** | `const { a: newName } = obj` | `const { name: userName } = user` |
| **Nested** | `const { a: { b } } = obj` | `const { address: { city } } = user` |
| **Rest** | `const [a, ...rest] = arr` | `const [first, ...others] = nums` |

### Key Takeaways

✅ Destructuring makes code cleaner and more readable  
✅ Works with both objects and arrays  
✅ Can set default values and rename variables  
✅ Great for function parameters  
✅ Order matters for arrays, not for objects  
✅ Use rest operator (`...`) to collect remaining values  

---

🎉 **Congratulations!** You now understand destructuring! Practice with the exercises to master this powerful ES6 feature.

**Pro Tip:** Destructuring is especially useful when working with API responses and React props! 🚀
