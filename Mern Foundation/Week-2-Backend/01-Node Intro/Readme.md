# 🟢 Node.js Introduction - Complete Guide

> **Master Node.js Basics** - Run JavaScript outside the browser!

---

## 📚 Table of Contents

1. [What is Node.js?](#1-what-is-nodejs)
2. [Why Node.js?](#2-why-nodejs)
3. [Installing Node.js](#3-installing-nodejs)
4. [Running JavaScript Files](#4-running-javascript-files)
5. [Node.js vs Browser JavaScript](#5-nodejs-vs-browser-javascript)
6. [Global Objects in Node](#6-global-objects-in-node)
7. [Node REPL](#7-node-repl)
8. [Package.json Basics](#8-packagejson-basics)

---

## 1. What is Node.js?

**Node.js** is a **JavaScript runtime** that lets you run JavaScript code **outside the browser** (on your computer or server).

### Visual Comparison

**BEFORE Node.js:**

- ❌ JavaScript ONLY runs in browsers (Chrome, Firefox, Safari)
- ❌ Can't access files on computer
- ❌ Can't create servers
- ❌ Can't run scripts on your machine

**AFTER Node.js:**

- ✅ JavaScript runs ANYWHERE
- ✅ Access files and folders
- ✅ Create web servers
- ✅ Build command-line tools
- ✅ Connect to databases

### Key Points:

- **Built on Chrome's V8 Engine** (same engine that runs JS in Chrome browser)
- **Single-threaded** but handles many requests using **event loop**
- **Non-blocking I/O** (can do multiple things at once)
- Perfect for **APIs, real-time apps, microservices**

---

## 2. Why Node.js?

### ✅ Advantages

```javascript
// 1. SAME LANGUAGE (Frontend + Backend)
// Frontend (React)
const greeting = "Hello from React!";

// Backend (Node.js) - SAME JavaScript!
const greeting = "Hello from Node!";

// 2. HUGE ECOSYSTEM (npm packages)
// Over 2 million packages available!

// 3. FAST & EFFICIENT
// Non-blocking I/O = handles thousands of connections

// 4. REAL-TIME APPS
// Perfect for chat apps, live notifications, gaming
```

### Popular Companies Using Node.js:
- Netflix
- LinkedIn
- Uber
- PayPal
- NASA
- Walmart

---

## 3. Installing Node.js

### Check if Already Installed

```bash
node -v
# Output: v20.10.0 (or similar)

npm -v
# Output: 10.2.3 (or similar)
```

### Download & Install

1. Go to https://nodejs.org/
2. Download **LTS version** (Long Term Support - more stable)
3. Run installer
4. Verify installation with `node -v`

**What Gets Installed:**
- ✅ **Node.js** - JavaScript runtime
- ✅ **npm** - Package manager
- ✅ **npx** - Package executor

---

## 4. Running JavaScript Files

### Create Your First Node.js File

**app.js:**
```javascript
console.log("Hello from Node.js!");

const numbers = [1, 2, 3, 4, 5];
const sum = numbers.reduce((acc, num) => acc + num, 0);

console.log("Sum:", sum);
```

### Run It

```bash
node app.js
```

**Output:**
```
Hello from Node.js!
Sum: 15
```

**How it works:**
1. 📝 Write code in `app.js`
2. ▶️ Run with `node app.js`
3. 📺 See output in Terminal

---

## 5. Node.js vs Browser JavaScript

| Feature | Browser | Node.js |
|---------|---------|---------|
| **Environment** | Browser window | Server/Computer |
| **Global Object** | `window` | `global` |
| **Access DOM?** | ✅ Yes | ❌ No |
| **Access File System?** | ❌ No | ✅ Yes |
| **Create Servers?** | ❌ No | ✅ Yes |
| **Modules** | ES6 modules | CommonJS + ES6 |

### What's Available Where?

```javascript
// ✅ WORKS IN BOTH (Standard JavaScript)
const name = "John";
const numbers = [1, 2, 3];
console.log("Hello");
setTimeout(() => {}, 1000);
JSON.parse('{"key": "value"}');

// ✅ BROWSER ONLY
window.alert("Hello");           // ❌ Error in Node
document.querySelector("#id");   // ❌ Error in Node
localStorage.setItem("key", "val"); // ❌ Error in Node

// ✅ NODE.JS ONLY
const fs = require('fs');        // ❌ Error in Browser
const http = require('http');    // ❌ Error in Browser
process.exit(0);                 // ❌ Error in Browser
```

### Quick Comparison

**Browser Environment:**
- JavaScript ✅
- DOM manipulation ✅
- `window` object ✅
- `localStorage` ✅

**Node.js Environment:**
- JavaScript ✅
- File System access ✅
- HTTP Server creation ✅
- OS-level operations ✅

---

## 6. Global Objects in Node

Unlike the browser's `window`, Node.js has `global` and special objects:

### __dirname & __filename

```javascript
console.log(__dirname);   // Current folder path
console.log(__filename);  // Current file path
```

**Example Output:**
```
__dirname:  C:\Users\John\Projects\myapp
__filename: C:\Users\John\Projects\myapp\app.js
```

### process

```javascript
// Get Node version
console.log(process.version);  // v20.10.0

// Get platform
console.log(process.platform); // win32, darwin, linux

// Get command line arguments
console.log(process.argv);

// Exit the program
process.exit(0);  // 0 = success, 1 = error
```

**Running with arguments:**
```bash
node app.js John 25
```

```javascript
// app.js
console.log(process.argv);
// Output: ['C:\\...\\node.exe', 'C:\\...\\app.js', 'John', '25']

const name = process.argv[2];  // "John"
const age = process.argv[3];   // "25"
```

### module & exports

```javascript
// Every file in Node is a module
console.log(module);

// Export values to use in other files
module.exports = {
    name: "MyApp",
    version: "1.0.0"
};
```

### Common Global Functions

```javascript
// ✅ Available in Node (same as browser)
setTimeout(() => console.log("After 1 sec"), 1000);
setInterval(() => console.log("Every 2 sec"), 2000);
console.log("Logging");
```

---

## 7. Node REPL

**REPL** = Read-Eval-Print-Loop (Interactive JavaScript shell)

### Start REPL

```bash
node
```

You'll see:
```
Welcome to Node.js v20.10.0.
Type ".help" for more information.
>
```

### Try It Out

```javascript
> 2 + 2
4

> const name = "John"
undefined

> name
'John'

> [1, 2, 3].map(x => x * 2)
[ 2, 4, 6 ]

> .exit  // or Ctrl+C twice to exit
```

**REPL is perfect for:**
- 🧪 Testing code snippets quickly
- 🔍 Debugging small functions
- 📚 Learning JavaScript concepts
- ⚡ Quick calculations

---

## 8. Package.json Basics

**package.json** is the **heart of every Node.js project**. It tracks:
- Project info (name, version, description)
- Dependencies (packages you installed)
- Scripts (commands you can run)

### Create package.json

```bash
npm init
```

Follow the prompts, or use:

```bash
npm init -y  # Skip questions, use defaults
```

### Example package.json

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "description": "My first Node.js app",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js"
  },
  "author": "Your Name",
  "license": "MIT",
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "nodemon": "^3.0.1"
  }
}
```

### Scripts Section

```json
"scripts": {
  "start": "node app.js",
  "dev": "nodemon app.js",
  "test": "jest"
}
```

Run them with:
```bash
npm start      # Runs "node app.js"
npm run dev    # Runs "nodemon app.js"
npm test       # Runs "jest"
```

**Package.json contains:**
- 📦 **Name & Version** - Project identity
- 📝 **Description** - What your project does
- 🎯 **Main Entry File** - Starting point (usually index.js)
- 🔧 **Scripts** - Shortcuts to run commands
- 📚 **Dependencies** - Packages your project needs

---

## 🚀 Quick Reference

```bash
# Check versions
node -v
npm -v

# Run a file
node app.js

# Start REPL (interactive shell)
node

# Initialize project
npm init -y

# Run script from package.json
npm start
npm run dev
```

### Common Node.js Globals

```javascript
__dirname          // Current directory path
__filename         // Current file path
process.version    // Node version
process.platform   // OS platform
process.argv       // Command line arguments
process.exit()     // Exit program
module.exports     // Export from file
require()          // Import from file
console.log()      // Print to terminal
```

---

## 📝 Practice Exercises

### Exercise 1: Hello World
```javascript
// hello.js
console.log("Hello, Node.js!");
```
```bash
node hello.js
```

### Exercise 2: Use Command Arguments
```javascript
// greet.js
const name = process.argv[2] || "Guest";
console.log(`Hello, ${name}!`);
```
```bash
node greet.js John
# Output: Hello, John!
```

### Exercise 3: Display System Info
```javascript
// info.js
console.log("Node Version:", process.version);
console.log("Platform:", process.platform);
console.log("Current Directory:", __dirname);
```

### Exercise 4: Create package.json
```bash
npm init -y
```

Then add a script:
```json
"scripts": {
  "greet": "node greet.js"
}
```

Run it:
```bash
npm run greet
```

---

## 🎯 Key Takeaways

1. **Node.js = JavaScript outside the browser**
2. **Run files with:** `node filename.js`
3. **No DOM, no window** - but you get file system, servers, OS access
4. **package.json** tracks your project info and dependencies
5. **REPL** for quick testing: just type `node`

---

> **Next Steps:** Learn about Node.js modules (require/import) and the File System module! 🚀