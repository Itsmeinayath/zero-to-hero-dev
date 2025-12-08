// --- 1. CONFIGURATION ---
const API_KEY = CONFIG.WEATHER_API_KEY;
const API_URL = 'https://api.openweathermap.org/data/2.5/weather';

// --- 2 DOM Selections ---

// we grab the elements we need from the HTML
const cityInput = document.querySelector('#cityInput')
const searchBtn = document.querySelector('#searchBtn')

// The container where we will display the weather info
const  weatherResult = document.querySelector('#weatherResult')
const errorMessage = document.querySelector('#errorMsg')

// The Specific text elements we will update 
const cityName = document.querySelector('#cityName')
const tempValue = document.querySelector('#tempValue')
const descValue = document.querySelector('#descValue')
const humidityValue = document.querySelector('#humidityValue')


// --- 3 Fetch Weather Data --- Teh core logic (Async/Await + Fetch API)

const checkWeather = async () => {

    const city = cityInput.value.trim();

    if (city === '') {
        errorMessage.textContent = 'Please enter a city name.';
        errorMessage.classList.remove('hidden');
        weatherResult.classList.add('hidden');
        return;
    }

    try {
        const fullUrl = `${API_URL}?q=${city}&appid=${API_KEY}&units=metric`;

        const response = await fetch(fullUrl);
        
        if(response.status === 404) {
            throw new Error('city not found');
        }
        const data = await response.json();

        // --- 4 Update DOM with Weather Data ---
        cityName.textContent = data.name;
        tempValue.textContent = Math.round(data.main.temp);
        descValue.textContent = data.weather[0].description;
        humidityValue.textContent = data.main.humidity;
        weatherResult.classList.remove('hidden');
        errorMessage.classList.add('hidden');

        
    } catch (error) {
        console.error('Error fetching weather data:', error);
        if (error.message === 'city not found') {
            errorMessage.textContent = 'City not found. Please try again.';
        } else {
            errorMessage.textContent = 'An error occurred. Please try again later.';
        }
        errorMessage.classList.remove('hidden');
        weatherResult.classList.add('hidden');
    }
}

// --- 5. EVENT LISTENERS ---
searchBtn.addEventListener('click', checkWeather);

cityInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        checkWeather();
    }
});