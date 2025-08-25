## Day 1 – JavaScript Fundamentals & Interactive DOM

Duration: ~3 hours  
Goal: Build a solid JavaScript base (syntax, logic, DOM) and ship a small interactive page.

---
## 1. Learning Outcomes
By end of Day 1 you can:
1. Declare & use variables (`let`, `const`) correctly (avoid accidental globals)
2. Differentiate primitive vs reference values
3. Write & call functions (declaration, expression, arrow) with clear purpose
4. Use conditionals & loops to control flow
5. Select & update DOM nodes safely
6. Handle basic user input (prompt / events)
7. Organize a tiny project (HTML + JS) inside your MERN Foundation folder

---
## 2. Core Concepts (Rapid Reference)

### 2.1 Variables & Types
```javascript
let username = "Ada";      // reassignable
const pi = 3.14159;        // not reassignable reference
// Primitive types: string, number, boolean, null, undefined, symbol, bigint
// Reference: object, array, function
```
Pitfalls:
- Forgetting `let/const` → creates global (avoid)
- Reassigning a `const` → TypeError (mutating object properties is still allowed)

### 2.2 Operators
Arithmetic: `+ - * / % **`  
Comparison: `=== !== > >= < <=` (prefer `===`)  
Logical: `&& || !`  
Template literals: `` `Hello ${username}` ``

### 2.3 Functions
```javascript
function add(a, b) { return a + b; }          // declaration (hoisted)
const multiply = function(a, b) { return a*b; }; // expression
const square = n => n * n;                    // arrow (concise)
```
Guideline: Single responsibility + meaningful name.

### 2.4 Control Flow
```javascript
if (score >= 90)      grade = "A";
else if (score >= 75) grade = "B";
else                  grade = "C";

for (let i = 0; i < 3; i++) console.log(i);
let n = 3; while (n--) console.log("tick");
```
Prefer `for..of` for arrays, avoid `for..in` on arrays.

### 2.5 Arrays & Objects (Preview)
```javascript
const skills = ["HTML", "CSS", "JS"];
skills.push("Git"); // mutate

const user = { name: "Ada", active: true };
user.active = false; // allowed (object reference stable)
```

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

