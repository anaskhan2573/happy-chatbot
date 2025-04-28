async function sendMessage() {
    const input = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');

    const userText = input.value.trim();
    if (userText === "") return;

    // Add user message
    const userMessage = document.createElement('div');
    userMessage.className = 'user-message';
    userMessage.innerText = userText;
    chatBox.appendChild(userMessage);

    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    // Show loading spinner
    const loadingMessage = document.createElement('div');
    loadingMessage.className = 'bot-message';
    loadingMessage.innerText = 'Typing... ✨';
    chatBox.appendChild(loadingMessage);

    try {
        const response = await fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userText })
        });

        const data = await response.json();
        loadingMessage.innerText = data.response;
    } catch (error) {
        loadingMessage.innerText = "Oops! Unable to connect. 🌧️";
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}
