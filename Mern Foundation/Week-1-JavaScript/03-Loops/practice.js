// This is file is all about loops in JavaScript] 
// Loops are used to repeat a block of code multiple times until a certain condition is met.
// There are different types of loops in JavaScript, including for loop, For loop, and while loop.

// 1. For Loop
console.log("For Loop Example:");
for(let i = 1; i <= 5; i++){
    console.log(`Iteration number: ${i}`);
}

// 2. While Loop
// example of game ehre you need 100 gold to win the game. you start with 0 and find random amount of gold

let gold = 0;
let days = 0
console.log("While Loop Example:");
while(gold < 100){
    days = days + 1
    let goldFound = Math.ceil(Math.random() * 10) ; // find random amount of gold between 1 and 10
    gold = gold + goldFound
    console.log(`Day ${days}: Found ${goldFound} gold . Total gold: ${gold}`);
}
