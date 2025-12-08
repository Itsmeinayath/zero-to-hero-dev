// 1 . we create an Async function to fetch data from an API

const getPost = async() =>{
    console.log("1.Asking the server for data...");

    const response = await fetch("https://jsonplaceholder.typicode.com/posts/1");

    const data = await response.json();
    console.log("2. Data received from server:");
    console.log("---- Data Display Section ----");
    console.log(data);
}

getPost(); // Call the async function
// console.log("4. Doing other tasks while waiting for post data...");