


// refacroring using toggle method
// old script.js
// --- OLD script.js ---
// const toggleButton = document.getElementById('toggleButton');
// const toggledText = document.getElementById('toggledText');

const { cos } = require("three/webgpu");

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