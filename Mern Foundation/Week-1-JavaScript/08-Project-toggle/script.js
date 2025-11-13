// --- 1. VARIABLES (The "Actors") ---
// We find our HTML elements and store them in CONST variables.
// 'document.getElementById' is how JS finds an element by its ID.
const toggleButton = document.getElementById('toggleButton');
const toggledText = document.getElementById('toggledText');

// We create a LET variable to be our "memory".
// It needs to remember if the text is currently hidden or not.
// We start with 'true' because we added the 'is-hidden' class in the HTML.
let isTextHidden = true;

// --- 2. FUNCTION (The "Recipe") ---
// We create our "recipe" for toggling the text.
// This function contains all the logic.
function toggleTheText() {
    
    // --- 3. CONDITIONAL (The "Brain") ---
    // This is the "brain". It checks our memory variable.
    if (isTextHidden === true) {
        // If the text IS hidden, we want to SHOW it.
        // '.classList.remove' takes off the CSS "costume".
        toggledText.classList.remove('is-hidden');
        
        // IMPORTANT: We must update our memory!
        isTextHidden = false;
        
    } else {
        // If the text is NOT hidden, we want to HIDE it.
        // '.classList.add' puts the CSS "costume" on.
        toggledText.classList.add('is-hidden');
        
        // IMPORTANT: Update our memory!
        isTextHidden = true;
    }
}

// --- 4. THE CONNECTION (The "Cue") ---
// We tell our button to "listen" for a 'click'.
// When it hears a click, it must run our 'toggleTheText' function.
toggleButton.addEventListener('click', toggleTheText);