// Destructuring example

const user = {
    name: 'Alice',
    level : 5,
    health: 80,
    email : "alice@example.com"
}

// the old way
let oldName = user.name;
let oldLevel = user.level;
let oldHealth = user.health;
console.log("the old way :",oldName, oldLevel, oldHealth); // Alice 5 80

// the new way: Destructuring

const { name, level, health } = user;
console.log("the new way :",name, level, health); // Alice 5 80