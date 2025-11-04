Topic 3 — Loops

## 1 — What are loops?

Loops allow you to repeat a block of code multiple times. Instead of writing the same code over and over, you use a loop to execute it automatically.

## 2 — Why use loops?

Loops are essential for:
- Processing arrays or lists of data
- Repeating tasks a specific number of times
- Iterating until a condition is met

## 3 — Types of loops in JavaScript

### for loop
Used when you know how many times to repeat.

```javascript
for (let i = 0; i < 5; i++) {
  console.log(`Iteration ${i}`);
}
```

### while loop
Repeats while a condition is true.

```javascript
let count = 0;
while (count < 3) {
  console.log(`Count is ${count}`);
  count++;
}
```

### do...while loop
Executes at least once, then checks the condition.

```javascript
let num = 0;
do {
  console.log(`Number: ${num}`);
  num++;
} while (num < 3);
```

### for...of loop
Iterates over array values.

```javascript
const fruits = ['apple', 'banana', 'orange'];
for (const fruit of fruits) {
  console.log(fruit);
}
```

### for...in loop
Iterates over object properties.

```javascript
const person = { name: 'Ali', age: 25 };
for (const key in person) {
  console.log(`${key}: ${person[key]}`);
}
```

## 4 — Loop control statements

- `break` — exit the loop early
- `continue` — skip to next iteration

```javascript
for (let i = 0; i < 10; i++) {
  if (i === 5) break; // stop at 5
  if (i % 2 === 0) continue; // skip even numbers
  console.log(i);
}
```

## 5 — Common loop patterns

Print numbers 1 to 10:
```javascript
for (let i = 1; i <= 10; i++) {
  console.log(i);
}
```

Sum array values:
```javascript
const numbers = [1, 2, 3, 4, 5];
let sum = 0;
for (const num of numbers) {
  sum += num;
}
console.log(`Sum: ${sum}`);
```

## Practice exercises

See `practice.js` for hands-on examples and exercises.
