// Named Export: You can export multiple things
export const add = (a, b) => a + b;
export const subtract = (a, b) => a - b;

// Default Export: You can only have ONE default export per file
// (Usually used for the main thing the file does)
const multiply = (a, b) => a * b;
export default multiply;