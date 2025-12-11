// index.js
import fs from 'fs';
import os from 'os';

console.log("--- STARTING NODE.JS SCRIPT ---");

const userInfo = os.userInfo();
const platform = os.platform(); 

console.log(`Hello, ${userInfo.username}!`);
console.log(`You are running on: ${platform}`);

const message = `
    Hello from Node.js!
    This file was created by JavaScript on your hard drive.
    User: ${userInfo.username}
    Time: ${new Date().toLocaleTimeString()}
`;

// This writes the file to your hard drive
fs.writeFileSync('my-new-file.txt', message);

console.log("✅ SUCCESS: Check your folder for 'my-new-file.txt'");