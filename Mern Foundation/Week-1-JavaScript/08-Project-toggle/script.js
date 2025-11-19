


// refacroring using toggle method
// old script.js
// --- OLD script.js ---
// const toggleButton = document.getElementById('toggleButton');
// const toggledText = document.getElementById('toggledText');

// const { cos } = require("three/webgpu");

// let isTextHidden = true;

// function toggleTheText() {
//     if (isTextHidden === true) {
//         toggledText.classList.remove('is-hidden');
//         isTextHidden = false;
//     } else {
//         toggledText.classList.add('is-hidden');
//         isTextHidden = true;
//     }
// }

// toggleButton.addEventListener('click', toggleTheText);

// --- NEW script.js ---
const toggleButton = document.getElementById('toggleButton');
const toggledText = document.getElementById('toggledText');

let isTextHidden = true;

const toggleTheText = () => {
    if (isTextHidden === true) {
        toggledText.classList.remove('is-hidden');
        isTextHidden = false;
    }
    else {
        toggledText.classList.add('is-hidden');
        isTextHidden = true;
    }
    console.log(`Text is now ${isTextHidden ? 'hidden' : 'visible'}`);
}

toggleButton.addEventListener('click', toggleTheText);

// --- DAY 3: DOM MANIPULATION (FORM) ---

// 1. VARIABLES (Find our new "actors")
// We use querySelector this time. It's flexible.
const nameForm = document.querySelector('#nameForm');
const nameInput = document.querySelector('#nameInput');
const displayName = document.querySelector('#displayName');

// 2. FUNCTION (The "recipe" for handling the form)
const handleSubmit = (event) => {
    // 3. PREVENT DEFAULT
    // This is CRITICAL. It stops the form from reloading the page.
    event.preventDefault();
    
    // 4. READ from the DOM
    // Get the text from the input box using .value
    const usersName = nameInput.value;

    // 5. VALIDATION
    // As per the plan, check if it's empty 
    if (usersName === "") {
        displayName.textContent = "Please enter a name!";
        // We can also style the text directly for errors
        displayName.style.color = "red";
    } else {
        // 6. WRITE to the DOM
        // Set the text of our <p> tag using .textContent
        displayName.textContent = `Hello, ${usersName}! Welcome.`;
        displayName.style.color = "#3498db"; // Reset color
    }

    // 7. Clear the input box for the next use
    nameInput.value = "";
};

// 5. THE CONNECTION (The "Cue")
// We listen for the 'submit' event on the FORM, not a 'click' on the button.
// This is the correct way, as it also works if the user presses "Enter".
nameForm.addEventListener('submit', handleSubmit);