Topic 1 — Variables

1. Definition and meaning

A variable is a named container in your program's memory used to store a piece of data.

Analogy: Think of a variable as a labeled storage box. You can put something inside the box (for example, the number 10) and write a name on the outside (for example, score). Later you can ask for the box named score and you'll get the value 10.

2. Why variables?

Programs need to remember things. For example, a game needs to remember:

- Your username (e.g., "Mohammed")
- Your current health (e.g., 85)
- Whether you have a magic key (true/false)

Without variables the program would forget these values.

3. How to declare variables (examples)

In modern JavaScript we usually use `let` and `const`.

let — the changeable box

Use `let` for values that will change over time (like a player's score).

```javascript
// 1. Declare a variable called 'score' and set initial value to 0
let score = 0;
console.log(`Your starting score is: ${score}`);

// 2. Update the value later
score = 50;
console.log(`You found a treasure! Your new score is: ${score}`);

// 3. Update again
score = score + 10;
console.log(`You defeated a monster! Your final score is: ${score}`);
```

const — the permanent box

Use `const` when the value should not be reassigned.

```javascript
// Declare a constant
const birthYear = 1990;
console.log(`Your birth year is: ${birthYear}`);

// Attempting to reassign will throw an error:
// birthYear = 1991; // TypeError: Assignment to constant variable.

// For objects, const prevents reassigning the variable, but object properties can change:
const person = { name: 'Mona' };
person.name = 'Mina'; // allowed
console.log(person.name); // 'Mina'
```

What about `var`?

`var` is the older keyword that has function-scoped behavior and hoisting quirks. In modern code prefer `const` and `let`.

4. Hands-on practice — example program

Create a file named `variables.js` and paste the example below.

```javascript
// --- Practice: Player Profile ---

// Use 'const' for values that won't change
const playerName = 'Inayath';

// Use 'let' for values that will change
let currentScore = 100;
let playerLevel = 5;

console.log('--- Player Profile ---');
console.log(`Name: ${playerName}`);
console.log(`Level: ${playerLevel}`);
console.log(`Score: ${currentScore}`);
console.log('----------------------');

// The player completes a quest — update values
currentScore = currentScore + 50; // add 50 points
playerLevel = playerLevel + 1;    // level up

console.log('...Player leveled up!...');
console.log(`New Level: ${playerLevel}`);
console.log(`New Score: ${currentScore}`);
```

How to run the example (Windows / PowerShell)

```powershell
node variables.js
```

You should see the profile printed, then the updated profile after the simulated quest.

Tips and summary

- Use `const` by default. Switch to `let` when you need to reassign.
- Avoid `var` in new code.
- Use meaningful variable names (for example `playerScore`, `totalPrice`).

That's it — short, clear, and ready to use. Happy coding!