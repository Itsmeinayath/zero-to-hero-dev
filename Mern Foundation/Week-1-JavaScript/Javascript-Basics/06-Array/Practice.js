// What is an Array?
// An array is a special variable that can hold more than one value at a time.
// Think of it as a list of items stored in a single variable.
//  In JavaScript , array is heterogeneous, meaning it can hold different data types together.


// === Exercise 1: Create and Manipulate an Array ===
// 1. Create an array named 'fruits' containing "Apple", "Banana", and "Cherry".

const fruits  = ["Apple", "Bannana", "Cherry"];

console.log(fruits) // Output: ["Apple", "Banana", "Cherry"]
console.log(fruits.length) // Output: 3


// 2. Add "Orange" to the end of the 'fruits' array. Push () method adds one or more elements to the end of an array and returns the new length of the array.
fruits.push("Orange");
console.log(fruits) // Output: ["Apple", "Banana", "Cherry", "Orange"]

// 3. Remove the first item from the 'fruits' array. we use pop() to remove the last item
fruits.pop();
console.log(fruits) // Output: ["Apple", "Banana", "Cherry"]

// 4. Remove the first item from the 'fruits' array. we use shift() to remove the first item. shift means remove from the beginning. and it is slwoer than pop() because it has to re-index the array.
fruits.shift();
console.log(fruits) // Output: ["Banana", "Cherry"]

// 5. indexOf() method returns the first index at which a given element can be found in the array, or -1 if it is not present.
console.log(fruits.indexOf("Cherry")) // Output: 1

// 6. Check if "Mango" is in the 'fruits' array. includes() method determines whether an array includes a certain value among its entries, returning true or false as appropriate.
console.log(fruits.includes("Mango")) // Output: false
console.log(fruits.includes("Banana")) // Output: true

// 7. Find the length of the 'fruits' array.
console.log(fruits.length) // Output: 2

// 8. Reverse the order of items in the 'fruits' array. reverse() method reverses an array in place. The first array element becomes the last, and the last array element becomes the first.
fruits.reverse();
console.log(fruits) // Output: ["Cherry", "Banana"]

// 9. indexing and accessing elements
console.log(fruits[0]) // Output: "Cherry"
console.log(fruits[1]) // Output: "Banana"
console.log(fruits[fruits.length - 1]) // Output: "Banana" // Accessing the last element

const MarvelHeroes = [" Iron Man", " Captain America", " Thor", " Hulk", " Black Widow"];
console.log(MarvelHeroes);

MarvelHeroes.push(" Hawkeye");
console.log(MarvelHeroes);

MarvelHeroes.shift();
console.log(MarvelHeroes);

MarvelHeroes.pop();
console.log(MarvelHeroes);

console.log(MarvelHeroes[2]);

console.log(MarvelHeroes.includes(" Thor"));

console.log(MarvelHeroes.indexOf(" Thor")); // 1

