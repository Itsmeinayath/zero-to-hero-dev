import { API_KEY } from './config.js';

const BASE_URL = "https://api.openweathermap.org/data/2.5/weather";

// This function takes a city name and returns the DATA object
export const fetchWeatherData = async (city) => {
    const url = `${BASE_URL}?q=${city}&appid=${API_KEY}&units=metric`;
    
    const response = await fetch(url);
    
    if (response.status === 404) {
        throw new Error("City not found");
    }
    
    return await response.json();
};