
## Topic 2 - Conditionals (if / else)

## 1 - What is a conditional?

A conditional lets your code choose different actions depending on whether a condition is true or false.

Analogy: a crossroads sign — the condition is the question ("Is it raining?"). If true, take one path ("Take an umbrella"); if false, take the other ("Wear sunglasses").

## 2 - Why they matter

Conditionals make programs dynamic: they allow behavior based on user input, game state, validation, and more.

Examples:

- Show profile if logged in; otherwise show login form
- If health <= 0 → show "Game Over"
- If form input is empty → show error; otherwise submit

## 3 - Comparison operators (quick)

- ===  equal (strict)
- !==  not equal (strict)
- >    greater than
- <    less than
- >=   greater than or equal
- <=   less than or equal

## 4 - if (single branch)

Run a block only when a condition is true.

```javascript
let hasMagicKey = true;

if (hasMagicKey === true) {
  console.log('You found the key! A new door has opened.');
}

console.log('You continue on your path...');
```

## 5 - if...else (two branches)

Choose between two alternatives.

```javascript
let userAge = 20;

if (userAge >= 18) {
  console.log('You are old enough to vote.');
} else {
  console.log('You are not old enough to vote yet.');
}
```

## 6 - if...else if...else (multiple choices)

Check conditions in order; the first true branch runs.

```javascript
let personAge = 10;
let ticketPrice;

if (personAge < 12) {
  ticketPrice = 5; // child
} else if (personAge >= 65) {
  ticketPrice = 7; // senior
} else {
  ticketPrice = 10; // regular
}

console.log(`Your ticket price is: $${ticketPrice}`);
```

## 7 - Ternary operator (short if/else)

```javascript
const isAdult = userAge >= 18 ? 'yes' : 'no';
console.log(isAdult);
```

## 8 - switch (many discrete cases)

```javascript
const day = 'Mon';
switch (day) {
  case 'Sat':
  case 'Sun':
    console.log('Weekend');
    break;
  case 'Mon':
    console.log('Start of week');
    break;
  default:
    console.log('Weekday');
}
```

## 9 - Truthy / falsy (quick)

Falsy values: false, 0, '', null, undefined, NaN. Everything else is truthy.

```javascript
if ('') console.log('will not run');
if (0) console.log('will not run');
if ('hello') console.log('this runs');
```

## 10 - Hands-on practice: Virtual Bouncer

Create `conditionals.js` and paste the example below.

```javascript
// --- Practice: The Virtual Bouncer ---
const personName = 'Ali';
let personAge = 22;
let isVip = false; // is on VIP list?

console.log(`A person named ${personName} approaches the door...`);

// Main rule: must be 21 or older, unless VIP
if (personAge >= 21) {
  console.log(`Welcome in, ${personName}! Have a great night.`);
} else if (isVip === true) {
  console.log(`Oh, you're on the VIP list, ${personName}. Go right in.`);
} else {
  console.log(`Sorry, ${personName}, I can't let you in. You must be 21.`);
}
```

7. Ternary operator (short if/else)

```javascript
const isAdult = userAge >= 18 ? 'yes' : 'no';
console.log(isAdult);
```

8. switch (many discrete cases)

```javascript
const day = 'Mon';
switch (day) {
  case 'Sat':
  case 'Sun':
    console.log('Weekend');
    break;
  case 'Mon':
    console.log('Start of week');
    break;
  default:
    console.log('Weekday');
}
```

9. Truthy / falsy quick note

Falsy values: false, 0, '', null, undefined, NaN — everything else is truthy.

```javascript
if ('') console.log('will not run');
if (0) console.log('will not run');
if ('hello') console.log('this runs');
```

10. Hands-on practice — Virtual Bouncer

Create `conditionals.js` and paste this example:

```javascript
// --- Practice: The Virtual Bouncer ---
const personName = 'Ali';
let personAge = 22;
let isVip = false; // is on VIP list?

console.log(`A person named ${personName} approaches the door...`);

// Main rule: must be 21 or older, unless VIP
if (personAge >= 21) {
  console.log(`Welcome in, ${personName}! Have a great night.`);
} else if (isVip === true) {
  console.log(`Oh, you're on the VIP list, ${personName}. Go right in.`);
} else {
  console.log(`Sorry, ${personName}, I can't let you in. You must be 21.`);
}
```

