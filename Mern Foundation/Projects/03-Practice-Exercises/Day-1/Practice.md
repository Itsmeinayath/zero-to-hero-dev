# 🎉 Day 1: JavaScript Fundamentals – Fun Practice Playground

> **Goal:** Learn and practice all Day 1 topics with interactive, playful examples!

---

## 🚀 Topics Covered

1. **Variables**
2. **Data Types**
3. **Operators**
4. **Conditionals**
5. **Loops**
6. **Functions**
7. **Arrays**
8. **Objects**
9. **DOM Basics**

---

## 🕹️ Practice Playground

### 1. Variables – Name Game

```javascript
// What's your name? Let's store it!
let userName = "Alice";
console.log("Hello, " + userName + "!");

// Try changing userName to your name!
```

---

### 2. Data Types – Type Detective

```javascript
let age = 21;           // Number
let isStudent = true;   // Boolean
let city = "Paris";     // String

console.log(typeof age);        // number
console.log(typeof isStudent);  // boolean
console.log(typeof city);       // string
```

---

### 3. Operators – Math Magic

```javascript
let a = 5, b = 3;
console.log(a + b);    // Addition
console.log(a - b);    // Subtraction
console.log(a * b);    // Multiplication
console.log(a / b);    // Division
console.log(a % b);    // Remainder
```

---

### 4. Conditionals – Secret Door

```javascript
let secret = "open";
if (secret === "open") {
  console.log("🎉 The door opens!");
} else {
  console.log("🚪 The door stays closed.");
}
```

---

### 5. Loops – Counting Stars

```javascript
for (let i = 1; i <= 5; i++) {
  console.log("⭐ Star " + i);
}
```

---

### 6. Functions – Greeting Machine

```javascript
function greet(name) {
  return "Hello, " + name + "!";
}
console.log(greet("Bob"));
```

---

### 7. Arrays – Favorite Foods

```javascript
let foods = ["Pizza", "Sushi", "Burger"];
foods.push("Ice Cream");
console.log(foods);
console.log("First food:", foods[0]);
```

---

### 8. Objects – Superhero Card

```javascript
let hero = {
  name: "Spider-Man",
  power: "Web-slinging",
  city: "New York"
};
console.log(hero.name + " saves " + hero.city + "!");
```

---

### 9. DOM Basics – Button Click Fun

```html
<!-- Save this as index.html and open in browser -->
<button onclick="alert('You clicked me!')">Click Me!</button>
```

---

## 🎲 Challenge: Mini Quiz

Try these on your own!

1. Change the variable to your favorite color and print it.
2. Write a loop that prints numbers 1 to 10.
3. Create a function that adds two numbers.
4. Make an array of 3 animals and print the last one.
5. Create an object for your favorite movie (name, year, genre).

---

## 🎨 Bonus: Interactive Webpage Starter

```html
<!-- Save as index.html and open in browser -->
<!DOCTYPE html>
<html>
  <body>
    <h2>What's your name?</h2>
    <input id="nameInput" type="text" />
    <button onclick="sayHello()">Say Hello</button>
    <p id="greeting"></p>
    <script>
      function sayHello() {
        let name = document.getElementById('nameInput').value;
        document.getElementById('greeting').innerText = "Hello, " + name + "!";
      }
    </script>
  </body>
</html>
```

---

<!-- **Have fun practicing! Change values, try new things, and see what happens. That's how you learn best!** -->