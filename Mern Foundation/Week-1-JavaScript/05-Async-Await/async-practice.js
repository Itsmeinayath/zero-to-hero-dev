// --- 1 Simulating a server
const getFakedata = () => {
    return new Promise((resolve) =>{
        setTimeout(() => {
            resolve("📦 Here is your pizza data!");
        }, 2000);
    })
}

// 2 the old way synchronous-ish promlem

console.log("1.Placing order for pizza...");

// --- 3 Async function to fetch the data
const orderPizza = async () =>{
    console.log("2. 🍕 Ordering pizza...");
    const food = await getFakedata();
    console.log("3. 🍽️ Received:", food);
}

orderPizza(); // Call the async function
console.log("4. Doing other tasks while waiting for pizza...");