
## Day 2 – Modern JavaScript (ES6+) & Refactor
Timebox: ~3 hours  (Learning 60m • Refactor 45–60m • Enhancement 30–45m • Wrap 15m)

### Learning outcomes
By end of today you can:
- Write concise arrow functions & know when NOT to use them (this / constructor cases)
- Use array & object destructuring (incl. renaming + defaults)
- Use template literals for interpolation & multi‑line strings
- Apply spread (...) & rest parameters
- Use object property shorthand & computed keys
- Refactor legacy style code (var / concatenation / function declarations) into modern readable ES6+
- Organize small DOM scripts with clear function boundaries

---
## 1. Core ES6 Concepts (focus set)
Feature | Why it matters | Micro example
--------|----------------|--------------
let / const | Block scoping & intent (mutability) | `const PI = 3.14` 
Arrow functions | Short + lexical `this` | `nums.map(n => n*2)`
Template literals | Cleaner strings | ``Hello ${user}``
Destructuring (array/object) | Extract pieces clearly | `const {id,name} = user`
Default params | Remove defensive `if (!x)` | `function f(a=0){}`
Rest parameter | Variadic inputs | `(...args) => args.length`
Spread | Clone / merge / expand | `{...a, active:true}`
Object shorthand | Reduce repetition | `const user = {id, name}`
Computed keys | Dynamic prop names | `{[keyName]: 42}`

Keep it minimal: You do NOT need classes, modules, or async today.

### Quick console drills (type, don’t copy)
```js
// Arrow + default + template
const greet = (name = 'stranger') => `Hello, ${name}!`;

// Object destructuring + rename + default
const person = { name: 'Dev', age: 22 };
const { name: displayName, age, country = 'IN' } = person;

// Array destructuring + skip
const nums = [10, 20, 30, 40];
const [first, , third] = nums; // 10, 30

// Rest & spread
const sum = (...values) => values.reduce((a,b)=>a+b,0);
const clone = { ...person, role: 'student' };

// Computed property
const key = 'score';
const result = { [key]: 95 };

console.log(greet(displayName));
console.log(first, third, country, sum(1,2,3), clone, result);
```

### Reference (skim, not memorize)
MDN: Arrow functions • Destructuring assignment • Template literals • Spread syntax • Rest parameters

---
## 2. Refactor Yesterday’s Page (base feature parity)
Original (pre‑ES6) patterns to eliminate:
- Verbose function declarations for simple handlers
- Manual string concatenation with +
- Repeated DOM queries inside loops
- Classic counted loops where iteration over fixed list is clearer

Target improvements:
- Arrow function for simple event logic (no reliance on `this`)
- Template literals for messages
- Extract repeated DOM node(s) once
- Use array literal + `forEach` for simple fixed iteration

Refactored handler:
```js
const sayHello = () => {
  const name = prompt("What's your name?");
  if (!name) {
    alert('Please enter a name!');
    return;
  }
  alert(`Hello, ${name}!`);
  const p = document.querySelector('p');
  p.textContent = `Hello, ${name}! Welcome to my page.`;
  [1,2,3,4,5].forEach(n => console.log(`Button clicked: ${n}`));
};
```

Verification checklist:
- Prompt appears
- Alert uses template literal
- Paragraph updates with new string
- Console logs 1..5

---
## 3. Enhancement Feature (add value)
Add Reset button (restore original paragraph) + (optional) Live character count of paragraph content.

HTML fragment (within body):
```html
<p id="bio">Hi, I'm [YourName]! Click the button to say hello.</p>
<button id="helloBtn">Say Hello</button>
<button id="resetBtn">Reset</button>
<small id="charInfo"></small>
<script src="script.js"></script>
```

`script.js` additions:
```js
const paragraph = document.getElementById('bio');
const ORIGINAL = paragraph.textContent;

const sayHello = () => { /* as above, reuse paragraph */ };

const resetText = () => {
  paragraph.textContent = ORIGINAL;
  console.log('Text reset');
  updateCharInfo();
};

const updateCharInfo = () => {
  const info = document.getElementById('charInfo');
  info.textContent = `Length: ${paragraph.textContent.length}`;
};

document.getElementById('helloBtn').addEventListener('click', sayHello);
document.getElementById('resetBtn').addEventListener('click', resetText);
updateCharInfo(); // initial
```

Why this matters: Introduces event listeners (no inline `onclick`), constant original state, single source of DOM node, and small pure utility (`updateCharInfo`).

Stretch (pick one if time):
- Add Dark/Light toggle (store mode in localStorage)
- Add input field instead of `prompt()` (better UX)
- Disable Hello button if input empty

---
## 4. Debugging & DevTools
Tool | Use
-----|----
Console tab | See logs / errors
Elements tab | Inspect structure / confirm IDs
Sources tab | Set breakpoint inside `sayHello` line 2, step through
Network tab | (Empty today – confirm no accidental requests)

Common mistakes & fixes:
- Query before element exists → Move script to end of body OR use `defer`
- `undefined` in template → Destructure wrong property name
- Arrow used where `this` needed (not today, but note: don’t arrow methods if using `this`)

---
## 5. Pitfalls & Patterns
Pitfall | Better
--------|-------
Inline `onclick` attributes | `addEventListener` separation
Magic strings repeated | Extract to constants (e.g., ORIGINAL)
Concatenation chains | Template literals
Re-query same selector | Cache in variable
Verbose loops building small fixed sequences | Array literal + `forEach`

Naming rule of thumb: noun for DOM nodes (`paragraph`), verb for functions (`resetText`, `updateCharInfo`).

---
## 6. Mini Exercises (10–15 min)
1. Add a counter of how many times Hello clicked.
2. Add a timestamp each time reset occurs (append to a `<ul>`).
3. Replace `[1,2,3,4,5]` with dynamic generation: `Array.from({length:5}, (_,i)=>i+1)` – compare readability.
4. Refactor `sayHello` into early returns style (already partially). Try without nested `if`.
5. Add ES6 destructuring to extract `textContent` in one line (optional stylistic).

---
## 7. Cheat Sheet
Snippet | Purpose
--------|--------
`const fn = (a=0)=>a*2` | Arrow + default
`const {id:nameId=0} = obj` | Object destructure + rename + default
`const [a,,c] = arr` | Skip item
`const clone = {...obj}` | Shallow clone
`const combo = {...a, ...b}` | Merge objects (right wins)
`const arr2 = [...arr, 99]` | Append immutably
```strings
`Hello ${user}` multiline supported
```

---
## 8. Deliverables & Git
Files (new folder): `day-02/index.html`, `day-02/script.js`
Commit message suggestion: `Day 2: ES6 refactor + reset & metrics`

Validation checklist before commit:
- No console errors
- Both buttons work
- Character length updates
- Code uses `const` where no reassignment

---
## 9. Reflection (5 min)
Prompts:
- Which ES6 feature removed the most verbosity today?
- Did you overuse arrow functions anywhere? (Constructor / method cases?)
- One tiny improvement for Day 3 (e.g., switch from prompt to input).

Log one-liner: “Refactored to ES6, added reset + char length, practiced destructuring/spread.”

---
## 10. Preview – Day 3
Plan to introduce: DOM form input handling, basic validation, simple state object, and minimal styling toggle.

End of Day 2 guide.