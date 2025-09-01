// 1. SELECTION: Find the HTML elements we need.
const toggleBtn = document.querySelector('#toggle-btn');
const body = document.querySelector('body');

// 2. LOGIC: Define the function that performs the action.
const toggleDarkMode = () => {
    // This powerful method adds the 'dark' class if it's missing,
    // and removes it if it's present.
    body.classList.toggle('dark');
    console.log("Dark mode toggled!"); // Add a log to see it working in the console
};

// 3. EVENT LISTENER: Connect the button to the function.
// This tells the button to "listen" for a 'click' and then
// run our toggleDarkMode function.
toggleBtn.addEventListener('click', toggleDarkMode);
