// Importing Named Exports (Must use { curly braces } and exact names)
import { add, subtract } from './mathUtils.js';

// Importing Default Export (No braces, can name it whatever you want)
import multiplyTool from './mathUtils.js';

console.log("Adding:", add(5, 3));        // 8
console.log("Subtracting:", subtract(10, 2)); // 8
console.log("Multiplying:", multiplyTool(4, 4)); // 16