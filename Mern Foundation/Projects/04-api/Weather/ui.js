// Select elements once
const cityName = document.querySelector('#cityName');
const tempValue = document.querySelector('#tempValue');
const descValue = document.querySelector('#descValue');
const humidityValue = document.querySelector('#humidityValue');
const weatherResult = document.querySelector('#weatherResult');
const errorMsg = document.querySelector('#errorMsg');

export const updateUI = (data) => {
    // Update text
    cityName.textContent = data.name;
    tempValue.textContent = Math.round(data.main.temp);
    descValue.textContent = data.weather[0].description;
    humidityValue.textContent = data.main.humidity;

    // Show result
    weatherResult.classList.remove('hidden');
    errorMsg.classList.add('hidden');
};

export const showError = (message) => {
    errorMsg.textContent = message;
    errorMsg.classList.remove('hidden');
    weatherResult.classList.add('hidden');
};