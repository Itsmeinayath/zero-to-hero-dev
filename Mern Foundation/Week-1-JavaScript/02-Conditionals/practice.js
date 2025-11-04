// This practice exercise demonstrates the use of conditional statements in JavaScript.

// Lets take example of gameplay where a player has to score points to win a game.

// here is the code for if condition to check if player has won the game

let playerscore = 85
let winningScore = 100

if (playerscore >= winningScore) {
    console.log("Congratulations! You win the game!")
}
console.log("Game Over. Try Again!")

// In this code, we check if the player's score is greater than or equal to the winning score.
// If the condition is true, it prints a winning message. Regardless of the outcome, it prints "Game Over. Try Again!".
// You can change the value of playerscore to test different outcomes.

let playerscore1 = 90
if (playerscore1 >= winningScore) {
    console.log("Congratulations! You win the game!")
}
else{
    console.log("Sorry, you lost the game. Better luck next time!")

}

let playerscore2 = 100
if (playerscore2 >= winningScore) {
    console.log("Congratulations! You win the game!")
}
else{
    console.log("Sorry, you lost the game. Better luck next time!")
}

// the multiple conditions can also be checked using else if statement( called as laddering / nested if else)

let playerscore3 = 70
if (playerscore3 >= winningScore) {
    console.log("Congratulations! You win the game!")
}
else if (playerscore3 >= 50) {
    console.log("You scored more than 50 points. You qualify for the next round!")
}
else{
    console.log("Sorry, you lost the game. Better luck next time!")
}



// --- Practice: The Daily Planner ---

// 1. Create variables for the day and time (24-hour clock).
let isWeekend = true;
let time = 14; // 2:00 PM

console.log("Checking the planner...");

// 2. This is the OUTER conditional: Is it the weekend?
if (isWeekend === true) {
    console.log("It's the weekend!");
    
    // 3. This is the NESTED logic for the 'if' (weekend) block.
    if (time < 12) {
        console.log("Good morning! Time to relax or sleep in.");
    } else if (time >= 12 && time < 18) {
        console.log("Good afternoon! Maybe run some errands or see friends.");
    } else {
        console.log("Good evening! Time to watch a movie.");
    }

} else {
    // 4. This is the 'else' for the OUTER conditional.
    console.log("It's a weekday.");
    
    // 5. This is the NESTED logic for the 'else' (weekday) block.
    if (time < 9) {
        console.log("Good morning! Time to get ready for work.");
    } else if (time >= 9 && time < 17) {
        console.log("It's working hours. Time to focus.");
    } else {
        console.log("Work is over! Time to head home.");
    }
}