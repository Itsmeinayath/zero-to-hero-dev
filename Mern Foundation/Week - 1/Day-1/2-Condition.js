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
