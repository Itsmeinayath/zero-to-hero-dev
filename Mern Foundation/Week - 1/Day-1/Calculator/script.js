// Calculator state
let currentOperation = 'add';
let history = [];

// Initialize calculator
document.addEventListener('DOMContentLoaded', function() {
    setupOperatorButtons();
    loadHistory();
    console.log('🧮 Beautiful Calculator loaded successfully!');
});

// Setup operator button functionality
function setupOperatorButtons() {
    const operatorButtons = document.querySelectorAll('.operator-btn');
    
    operatorButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            operatorButtons.forEach(btn => btn.classList.remove('active'));
            
            // Add active class to clicked button
            this.classList.add('active');
            
            // Update current operation
            currentOperation = this.getAttribute('data-op');
            
            // Update display
            updateOperationDisplay();
        });
    });
}

// Update operation display
function updateOperationDisplay() {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    const operationDisplay = document.getElementById('operation-display');
    
    if (num1 || num2) {
        const symbol = getOperationSymbol(currentOperation);
        operationDisplay.textContent = `${num1 || '?'} ${symbol} ${num2 || '?'} =`;
    }
}

// Get operation symbol for display
function getOperationSymbol(operation) {
    const symbols = {
        'add': '+',
        'subtract': '−',
        'multiply': '×',
        'divide': '÷'
    };
    return symbols[operation] || '+';
}

// Main calculate function
function calculate() {
    const num1Input = document.getElementById('num1');
    const num2Input = document.getElementById('num2');
    const resultDisplay = document.getElementById('result');
    
    // Get values
    const num1 = parseFloat(num1Input.value);
    const num2 = parseFloat(num2Input.value);
    
    // Validation
    if (isNaN(num1) || isNaN(num2)) {
        showError('Please enter valid numbers in both fields');
        return;
    }
    
    if (currentOperation === 'divide' && num2 === 0) {
        showError('Cannot divide by zero');
        return;
    }
    
    // Perform calculation
    let result;
    let operationText;
    
    switch (currentOperation) {
        case 'add':
            result = num1 + num2;
            operationText = `${num1} + ${num2}`;
            break;
        case 'subtract':
            result = num1 - num2;
            operationText = `${num1} - ${num2}`;
            break;
        case 'multiply':
            result = num1 * num2;
            operationText = `${num1} × ${num2}`;
            break;
        case 'divide':
            result = num1 / num2;
            operationText = `${num1} ÷ ${num2}`;
            break;
        default:
            showError('Invalid operation');
            return;
    }
    
    // Round result to avoid floating point issues
    result = Math.round(result * 100000000) / 100000000;
    
    // Update displays
    updateOperationDisplay();
    resultDisplay.textContent = result;
    resultDisplay.classList.add('result-animate');
    
    // Remove animation class after animation completes
    setTimeout(() => {
        resultDisplay.classList.remove('result-animate');
    }, 300);
    
    // Add to history
    addToHistory(operationText, result);
    
    // Success feedback
    console.log(`✅ Calculation: ${operationText} = ${result}`);
}

// Show error message
function showError(message) {
    const resultDisplay = document.getElementById('result');
    const operationDisplay = document.getElementById('operation-display');
    
    resultDisplay.textContent = 'Error';
    operationDisplay.textContent = message;
    
    // Clear error after 3 seconds
    setTimeout(() => {
        operationDisplay.textContent = '';
        resultDisplay.textContent = '0';
    }, 3000);
    
    console.log(`❌ Error: ${message}`);
}

// Clear all inputs and result
function clearAll() {
    document.getElementById('num1').value = '';
    document.getElementById('num2').value = '';
    document.getElementById('result').textContent = '0';
    document.getElementById('operation-display').textContent = '';
    
    // Reset to addition
    document.querySelectorAll('.operator-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    document.querySelector('[data-op="add"]').classList.add('active');
    currentOperation = 'add';
    
    console.log('🔄 Calculator cleared');
}

// Add calculation to history
function addToHistory(operation, result) {
    const historyItem = {
        operation: operation,
        result: result,
        timestamp: new Date().toLocaleTimeString()
    };
    
    history.unshift(historyItem); // Add to beginning
    
    // Limit history to 10 items
    if (history.length > 10) {
        history = history.slice(0, 10);
    }
    
    updateHistoryDisplay();
    saveHistory();
}

// Update history display
function updateHistoryDisplay() {
    const historyList = document.getElementById('history-list');
    const clearBtn = document.querySelector('.clear-history-btn');
    
    if (history.length === 0) {
        historyList.innerHTML = '<p class="no-history">No calculations yet</p>';
        clearBtn.style.display = 'none';
    } else {
        historyList.innerHTML = history.map(item => 
            `<div class="history-item">
                ${item.operation} = ${item.result}
                <small style="float: right; opacity: 0.6;">${item.timestamp}</small>
            </div>`
        ).join('');
        clearBtn.style.display = 'block';
    }
}

// Clear history
function clearHistory() {
    history = [];
    updateHistoryDisplay();
    saveHistory();
    console.log('🗑️ History cleared');
}

// Save history to localStorage
function saveHistory() {
    localStorage.setItem('calculator-history', JSON.stringify(history));
}

// Load history from localStorage
function loadHistory() {
    const saved = localStorage.getItem('calculator-history');
    if (saved) {
        history = JSON.parse(saved);
        updateHistoryDisplay();
    }
}

// Add input event listeners for real-time display updates
document.getElementById('num1').addEventListener('input', updateOperationDisplay);
document.getElementById('num2').addEventListener('input', updateOperationDisplay);

// Add Enter key support
document.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        calculate();
    }
});

// Add keyboard shortcuts
document.addEventListener('keydown', function(event) {
    switch(event.key) {
        case '+':
            setOperation('add');
            break;
        case '-':
            setOperation('subtract');
            break;
        case '*':
            setOperation('multiply');
            break;
        case '/':
            event.preventDefault(); // Prevent default browser search
            setOperation('divide');
            break;
        case 'Escape':
            clearAll();
            break;
    }
});

// Set operation via keyboard
function setOperation(operation) {
    currentOperation = operation;
    
    // Update button states
    document.querySelectorAll('.operator-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    document.querySelector(`[data-op="${operation}"]`).classList.add('active');
    
    updateOperationDisplay();
}