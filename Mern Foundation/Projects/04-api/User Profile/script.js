// --- 1 . Selection (The Hooks DOM Manipulation) ---

const userName  = document.querySelector('#userName')
const userEmail = document.querySelector('#userEmail')
const userCity = document.querySelector('#userCity')
const fetchBtn = document.querySelector('#fetchBtn')

// --- 2 . The Async Function (the Fetching Logic) ---

const getUser = async() =>{
    fetchBtn.textContent = 'Loading...'
    fetchBtn.disabled = true

    try {
        const RandomId = Math.floor(Math.random() * 10) + 1
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${RandomId}`)

        const data =  await response.json()

        console.log("User Data ", data)

        userName.textContent = data.name
        userEmail.textContent = data.email
        userCity.textContent = data.address.city
        
    } catch (error) {
        console.error('Error fetching user data:', error);
        userName.textContent = 'Error fetching data'
        userEmail.textContent = ''
        userCity.textContent = ''
        
    }

    fetchBtn.textContent = 'Load Random User'
    fetchBtn.disabled = false
}

fetchBtn.addEventListener('click', getUser)