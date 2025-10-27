Topic 2: Conditionals (if / else)
1. Definition and Meaning
Definition: A conditional is a programming statement that performs different actions depending on whether a condition is true or false.

Analogy: Think of a conditional as a crossroads on a path with a sign.

The sign is the condition (e.g., "Is it raining?").

If the answer is true (it is raining), you go down one path (e.g., "Take an umbrella").

If the answer is false (it's not raining), you go down the other path (e.g., "Wear sunglasses").

Conditionals give your program a "brain" and allow it to make decisions.

2. The In-Depth Explanation (The "Why")
Without conditionals, a program would be a "dumb" list of instructions. It would do the exact same thing every single time.

With conditionals, your program can react to different situations.

Is the user logged in?

If true, show their profile page.

If false, show the login form.

Is the health bar at 0?

If true, show the "Game Over" screen.

If false, let the game continue.

Is the text box empty?

If true, show an error message.

If false, submit the form.

Conditionals are what make a program feel interactive and "smart." The most common conditional in JavaScript is the if...else statement.

3. The "How" — Writing Conditionals (Examples)
To create a condition, we need Comparison Operators:

=== : Is "equal to"? (e.g., age === 18)

!== : Is "not equal to"? (e.g., username !== "Admin")

> : Is "greater than"? (e.g., score > 100)

< : Is "less than"? (e.g., health < 10)

>= : Is "greater than or equal to"?

<= : Is "less than or equal to"?

Now let's use them.

if (The Single Path)
Use this when you only want to do something if the condition is true.

Example: You only care if the player finds a key.

JavaScript

let hasMagicKey = true;

if (hasMagicKey === true) {
  console.log("You found the key! A new door has opened.");
}

console.log("You continue on your path...");
If hasMagicKey was false, the "You found the key..." message would just be skipped.

if...else (The "Either/Or" Path)
This is the most common. The program must choose one of the two paths.

Example: Checking if a user is old enough to vote.

JavaScript

let userAge = 20;

if (userAge >= 18) {
  console.log("You are old enough to vote.");
} else {
  console.log("You are not old enough to vote yet.");
}
One of these two messages will always run.

if...else if...else (The "Multiple Choice" Path)
Use this when you have more than two options.

Example: Deciding a movie ticket price based on age.

JavaScript

let personAge = 10;
let ticketPrice;

if (personAge < 12) {
  ticketPrice = 5; // Child price
} else if (personAge >= 65) {
  ticketPrice = 7; // Senior price
} else {
  ticketPrice = 10; // Regular price
}

console.log(`Your ticket price is: $${ticketPrice}`);
JavaScript checks each if and else if in order until it finds one that is true. If none are true, it runs the final else block.

4. Hands-on Practice: The Virtual Bouncer
Let's write a small "program" to practice this.

Create a new file in your VS Code project called conditionals.js.

Type the following code into it. This program will act as a bouncer for a club.

JavaScript

// --- Practice: The Virtual Bouncer ---

// 1. Create variables for the person at the door.
const personName = "Ali";
let personAge = 22;
let isVip = false; // Are they on the VIP list?

console.log(`A person named ${personName} approaches the door...`);

// 2. Start our conditional check.
// The main rule is you must be 21 or older.
if (personAge >= 21) {
    // If they are 21 or older, they are allowed in.
    console.log(`Welcome in, ${personName}! Have a great night.`);

} else if (isVip === true) {
    // If they are NOT 21+, we check *else if* they are a VIP.
    // VIPs can get in even if they are underage.
    console.log(`Oh, you're on the VIP list, ${personName}. Go right in.`);

} else {
    // If they are not 21+ AND they are not a VIP, they are rejected.
    console.log(`Sorry, ${personName}, I can't let you in. You must be 21.`);
}
To run your code:

Open your terminal in VS Code.

Type node conditionals.js and press Enter.

Your Mission (to practice): Try changing the variables at the top of the file and run the program again.

What happens if you set personAge = 19 and isVip = false?

What happens if you set personAge = 19 and isVip = true?

What happens if you set personAge = 50 and isVip = true?