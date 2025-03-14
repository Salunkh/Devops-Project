function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (!userInput.trim()) return; // Ignore empty input

    let chatbox = document.getElementById("chatbox");

    // Display user message
    let userMessageDiv = document.createElement("div");
    userMessageDiv.className = "message user";
    userMessageDiv.innerText = userInput;
    chatbox.appendChild(userMessageDiv);

    // Send request to Flask backend
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        let botMessageDiv = document.createElement("div");
        botMessageDiv.className = "message bot";
        botMessageDiv.innerText = data.response || "Error getting response.";
        chatbox.appendChild(botMessageDiv);
    })
    .catch(error => console.error("Error:", error));

    document.getElementById("user-input").value = ""; // Clear input
}

function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

function clearChat() {
    document.getElementById("chatbox").innerHTML = ""; // Clears chat
}
