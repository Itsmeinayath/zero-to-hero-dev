Day 1: JavaScript Basics (3 hours)
Goal: Learn JavaScript variables, functions, loops, and arrays, and apply them to add interactivity to a webpage.
Tasks:

Learn JavaScript Basics (1 hour):

Concepts: Variables (let, const, var), data types (strings, numbers, booleans), functions (declaration, expression), loops (for, while), and conditionals (if, switch).
Resources:

Watch a beginner-friendly tutorial (e.g., FreeCodeCamp’s JavaScript basics or Traversy Media on YouTube, ~30 minutes).
Read MDN Web Docs on JavaScript basics for reference (focus on variables, functions, loops).


Action: Write small code snippets in a browser console (open DevTools with F12) to practice:

Declare variables: let name = "YourName"; const age = 25;
Create a function: function greet(name) { return "Hello, " + name; }
Loop through numbers: for (let i = 1; i <= 5; i++) { console.log(i); }




Build a Simple Webpage (1 hour):

Use your HTML/CSS skills to create a basic webpage (e.g., a personal bio page with a heading, paragraph, and button).
Example structure:
html<!DOCTYPE html>
<html>
<head>
  <title>My Bio</title>
  <style>
    body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
    button { padding: 10px 20px; font-size: 16px; cursor: pointer; }
  </style>
</head>
<body>
  <h1>Welcome to My Bio</h1>
  <p>Hi, I'm [YourName]! Click the button to say hello.</p>
  <button onclick="sayHello()">Click Me</button>
  <script src="script.js"></script>
</body>
</html>

Save this as index.html in a new project folder.


Add Interactivity with JavaScript (1 hour):

Create a script.js file and link it to your HTML.
Write a function to add interactivity to the button:
javascriptfunction sayHello() {
  let name = prompt("What's your name?");
  if (name) {
    alert("Hello, " + name + "!");
    document.querySelector("p").innerText = "Hello, " + name + "! Welcome to my page.";
  } else {
    alert("Please enter a name!");
  }
}

Action: Test the page in a browser. Clicking the button should prompt for a name, display an alert, and update the paragraph text.
Experiment: Add a loop to log numbers 1–5 in the console when the button is clicked.



Deliverable:

A simple webpage (index.html, script.js) with a button that prompts for a name and updates the page.
Test it locally by opening index.html in a browser.

Mentor Feedback:
Great start! Your webpage should feel alive with that button interaction. Make sure your JavaScript code is clean—use let or const (avoid var), and indent properly. If the prompt/alert works, you’re nailing the basics! Try to understand how the DOM (document.querySelector) connects your JavaScript to HTML. Tomorrow, we’ll dive into ES6 to modernize your code. Push this to a GitHub repo by Day 5, but for now, save your files and test thoroughly.
Tips:

Use VS Code for coding (install if you haven’t).
Open the browser console (F12) to debug any errors.
If stuck, revisit MDN docs or ask me for clarification.
Take a quick break if you feel overwhelmed—3 hours is intense!