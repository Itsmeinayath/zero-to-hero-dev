import { fetchWeatherData } from './weatherAPI.js';
import { updateUI, showError } from './ui.js';

const searchBtn = document.querySelector('#searchBtn');
const cityInput = document.querySelector('#cityInput');

const handleSearch = async () => {
    const city = cityInput.value.trim();
    if (!city) return;

    try {
        // 1. Ask the API module for data
        const data = await fetchWeatherData(city);
        
        // 2. Give that data to the UI module
        updateUI(data);
        
    } catch (error) {
        // 3. If error, tell UI module to show it
        showError(error.message === "City not found" ? "Invalid City" : "Something went wrong");
    }
};

searchBtn.addEventListener('click', handleSearch);