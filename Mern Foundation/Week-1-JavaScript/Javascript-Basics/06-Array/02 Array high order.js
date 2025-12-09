const students = ["john", "peter", "susan", "anna", "bob", "mary"];


// Normal way of iterating an array
for (let i = 0; i < students.length; i++){
    console.log(students[i]);
}
console.log("--------------");

// Using forEach high order function
// Explanation: forEach takes a callback function that is executed for each element in the array.
// here the val means the current element being processed in the array.
// forEach does not return a new array, it simply executes the provided function once for each array element.
// forEach explanation : foreach method executes a provided function once for each array element in ascending order.
students.forEach((val) => console.log(val));
console.log("--------------");

// Using map high order function
// Explanation: map creates a new array populated with the results of calling a provided function on every element in the calling array.
// here the val means the current element being processed in the array.
// map returns a new array with the results of calling a provided function on every element in the calling array.
const studentsnames = students.map((val) => console.log(val));
console.log("--------------");

// Difference between forEach and map:
// forEach does not return a new array, it simply executes the provided function once for each array element.
// map returns a new array with the results of calling a provided function on every element in the calling array.
// Use forEach when you want to perform side effects (like logging) and don't need a new array.
// Use map when you want to transform each element and create a new array with the transformed elements.

// example of diffreence between forEach and map
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Using forEach to log each number
numbers.forEach((num) => console.log(num * 2)); // Logs: 2, 4, 6, 8, 10

// Using map to create a new array with doubled values
const doubledNumbers = numbers.map((num) => num * 2);
console.log(doubledNumbers); // Output: [2, 4, 6, 8, 10]

console.log("--------------");


//  .filter() high order function
// Explanation: filter method creates a new array with all elements that pass the test implemented by the provided function.
// here the val means the current element being processed in the array.

const newArr = numbers.filter((num) => num % 2 === 0);
console.log(newArr); // Output: [2, 4]
console.log("--------------");

//  .find() high order function
// Explanation: find method returns the value of the first element in the provided array that satisfies the provided testing function.
// here the val means the current element being processed in the array.

const studentFound = students.find((val) => val === "susan");
console.log(studentFound); // Output: susan
console.log("--------------");

// findindex() high order function
// Explanation: findIndex method returns the index of the first element in the array that satisfies the provided testing function. Otherwise, it returns -1, indicating that no element passed the test.
// here the val means the current element being processed in the array.
const studentIndex = students.findIndex((val) => val === "anna");
console.log(studentIndex); // Output: 3
console.log("--------------");

//  . slice() high order function
// Explanation: slice method returns a shallow copy of a portion of an array into a new array object selected from start to end (end not included) where start and end represent the index of items in that array. The original array will not be modified.
// it works on index (starting index , ending index(+1 because it is not included))
const slicedArr = students.slice(1, 4);
console.log(slicedArr); // Output: [ 'peter', 'susan', 'anna' ]
console.log("--------------");

// splice() high order function
// Explanation: splice method changes the contents of an array by removing or replacing existing elements and/or adding new elements in place.
// it works on index (starting index , number of elements to remove, elements to add)
const splicedArr = students.splice(2, 2, "george", "linda");
console.log(students); // Output: [ 'john', 'peter', 'george', 'linda', 'bob', 'mary' ]
console.log("--------------");

// .random() high order function
// Explanation: random method returns a floating-point, pseudo-random number in the range 0 to less than 1 (inclusive of 0, but not 1).
const randomNum = Math.random();
console.log(randomNum); // Output: a random number between 0 and 1
console.log("--------------");
