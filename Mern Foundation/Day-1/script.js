function sayHello() {
  let name = prompt("What's your name?");
  if (name) {
    alert("Hello, " + name + "!");
    document.querySelector("p").innerText = "Hello, " + name + "! Welcome to my page.";
    for (let i = 1; i <= 5; i++) {
      console.log("Button clicked, iteration:", i);
    }
  } else {
    alert("Please enter a name!");
  }
}