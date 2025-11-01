const sendBtn = document.getElementById("send-btn");
const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");

sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
});

function appendMessage(message, sender) {
    const msgDiv = document.createElement("div");
    msgDiv.classList.add(sender === "user" ? "user-message" : "bot-message");
    msgDiv.textContent = message;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    // Display user's message
    appendMessage(message, "user");
    userInput.value = "";

    // Show typing animation
    const typingDiv = document.createElement("div");
    typingDiv.classList.add("bot-message");
    typingDiv.textContent = "Typing...";
    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const response = await fetch("/get", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        // Remove typing message
        chatBox.removeChild(typingDiv);

        // Append bot response
        appendMessage(data.reply, "bot");
    } catch (error) {
        chatBox.removeChild(typingDiv);
        appendMessage("⚠️ Error: Could not connect to the server.", "bot");
    }
}
